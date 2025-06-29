from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.modules.media_keys import MediaKeys
from kmk.modules.oled import OLED
from kmk.modules.layers import Layers

import board
import displayio
from adafruit_display_text import label
import terminalio
import time
import usb_cdc

keyboard = KMKKeyboard()

# --- modules ---
keyboard.modules.append(MediaKeys())
keyboard.modules.append(EncoderHandler())
keyboard.modules.append(Layers())

# --- OLED setup ---
oled = OLED(
    oled_type=OLED.OLED_128x32,
    flip=True,
    update_interval=0.1,
    sda=board.D8,  # SDA = PA07
    scl=board.D7   # SCL = PB09
)
keyboard.modules.append(oled)

# --- track text + scrolling state ---
current_song_text = ["Now listening to:", "loading...", ""]
scroll_offsets = [0, 0]
scroll_speed = 1

def draw_oled(oled_obj, display, is_enabled):
    if not is_enabled:
        return

    display_group = displayio.Group()
    font = terminalio.FONT

    # song title
    title_label = label.Label(font, text=current_song_text[0], x=0, y=0)
    display_group.append(title_label)

    for i, text in enumerate(current_song_text[1:]):  # song, artist
        text_width = font.get_bounding_box()[0] * len(text)
        x_pos = -scroll_offsets[i] if text_width > 128 else 0

        scroll_label = label.Label(font, text=text, x=x_pos, y=10 + i * 12)
        display_group.append(scroll_label)

        if text_width > 128:
            scroll_offsets[i] += scroll_speed
            if scroll_offsets[i] > text_width:
                scroll_offsets[i] = -128
        else:
            scroll_offsets[i] = 0

    display.show(display_group)

oled.on_display = draw_oled

# --- key matrix pins ---
keyboard.col_pins = (board.D0, board.D1, board.D2, board.D3)  # SW1–SW4
keyboard.row_pins = (board.D4,)  # GND side of all buttons
keyboard.diode_orientation = keyboard.DIODE_COL2ROW

# --- Encoder Pins (A, B, Push) ---
keyboard.encoder_handler.pins = (
    (board.D5, board.D6, board.D4),  # A, B, PUSH
)
keyboard.encoder_handler.map = [
    ((KC.VOLD, KC.VOLU, KC.MUTE),)
]

# --- keymap ---
keyboard.keymap = [
    [
        KC.LGUI(KC.SPACE),  # SW1: launch spotify (actually spotlight search, im too lazy to find out how to actually do spotify)
        KC.MRWD,        # SW2: rewind
        KC.MPLY,        # SW3: play/Pause
        KC.MFFD         # SW4: forward
    ]
]


# --- SONG INFO GETS UPDATED FROM PYTHON SCRIPT RUNNING IN MY PC "send_to_macropad.py" ---

# --- serial song info update (usb_cdc) ---
def update_song_from_serial():
    global current_song_text
    if usb_cdc.console.in_waiting > 0:
        try:
            data = usb_cdc.console.read(128)
            lines = data.decode().strip().split("|")
            if len(lines) == 2:
                current_song_text = [
                    "Now listening to:",
                    lines[0].strip(),  # Song
                    lines[1].strip()   # Artist
                ]
        except UnicodeError:
            pass

# --- Main Loop ---
if __name__ == '__main__':
    keyboard.go(once=False)
    while True:
        update_song_from_serial()

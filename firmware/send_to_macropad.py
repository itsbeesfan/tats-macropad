import serial
import time
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth

# PLEASE update with your spotify credentials
sp = Spotify(auth_manager=SpotifyOAuth(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    redirect_uri="http://localhost:8888/callback",
    scope="user-read-playback-state"
))

# change to your device's serial port
SERIAL_PORT = "/dev/ttyACM0"  # or "COM3" on Windows
BAUDRATE = 115200

def get_current_song():
    try:
        playback = sp.current_playback()
        if playback and playback.get('item'):
            name = playback['item']['name']
            artist = ', '.join([a['name'] for a in playback['item']['artists']])
            return f"{name}|{artist}"
    except Exception as e:
        print("Error:", e)
    return None

def main():
    with serial.Serial(SERIAL_PORT, BAUDRATE, timeout=1) as ser:
        last_song = ""
        while True:
            song = get_current_song()
            if song and song != last_song:
                print("Sending:", song)
                ser.write((song + "\n").encode())
                last_song = song
            time.sleep(5)

if __name__ == "__main__":
    main()

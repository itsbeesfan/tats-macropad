# tats' super cool macropad
### for hack club's "hackpad" ysws (i genuinely couldn't think of a better name)

the main idea with this macropad is to be able to listen to music easily, and without disturbing any work or opening any
extra tabs.

## components (BOM)
- 4x cherry MX switches
- 1x XIAO RP2040
- 1x 0.91" OLED display
- 1x EC11 rotary encoder
- 4x blank DSA keycaps

## functionality
the top switch allows me to access spotify. the three bottom switches allow me to rewind, play/pause and forward (respectively).

spotify data is fetched using the spotify API, and the OLED displays the song i am listening to and the artist (it includes a 
cool scrolling animation if the artist/song name is too big!).

finally, the rotary encoder allows me to change the volume, and i can mute if i press on it. 


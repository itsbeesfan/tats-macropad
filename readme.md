# tats' super cool macropad
### for hack club's "hackpad" ysws (i genuinely couldn't think of a better name)

![image](https://github.com/user-attachments/assets/f586cf94-7a38-4b3e-b337-809dd3fd4d21)


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

schematic            |  PCB         |   case    |   plate
:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|
![image](https://github.com/user-attachments/assets/70454112-47b7-44a9-924e-3a8c53fec77a)| ![image](https://github.com/user-attachments/assets/64821e0e-4b6a-484d-ae4e-3a6258205c53) | ![image](https://github.com/user-attachments/assets/a95ea2d3-1d22-4550-b8a0-6cd00c639598)| ![image](https://github.com/user-attachments/assets/4ef1f4e7-3f43-4731-90da-4cbcf8023d87)


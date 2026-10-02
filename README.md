<img width="464" height="278" alt="image" src="https://github.com/user-attachments/assets/d6f810ba-1e63-4bf6-8102-fb860a8a5b86" />



# OrphBoard!!!!
### by Dhairya

## What is OrphBoard? 

OrphBoard is a custom RP2040 development board that I designed in EasyEDA.

Now you might be wondering what the "Orph" in OrphBoard means...

Orph stands for Orpheus, Hack Club's mascot.

So yeah, OrphBoard is a custom RP2040 devboard designed in the shape of a dancing dino featuring the GREAT ORPHEUS HIMSELF!!!

## The Features -> 

- Uses a RP2040 SoC as its microcontroller chip
- Dual-core ARM Cortex-M0+ processor
- Features USB-C, USB 1.1
- Features the GREAT ORPHEUS HIMSELF!!!
- 264 KB SRAM
- Winbond W25Q16JVZPIQ for the flash IC
- USB programming via RP2040 BOOTSEL
- 3.3 V Logic Voltage
- 5 V USB-C VBUS input power
- 1 boot button
- 2MB Flash
- 12 MHz crystal oscillator



## Repo Structure 

`/production` - the main folder with manufacturing files


`/production/CAD` - the 3d printing manufacturing files


`/production/PCB` - The PCB gerbers (production files)


`/src` - the source files are in this folder


`/src/EasyEDA` - the easyEDA source files


`/src/FreeCAD` - the freeCAD source files


`PCB.step` - the step file with the 3d model of the PCB


`PCB.stl` - the stl file with 3d model of the PCB


`assembly.step` - the step file with the 3d model of Case along with the PCB


`assembly.stl` - the .stl counterpart of `assembly.step`

***Firmware (this is just a small blinking LED script)***


`/LED blinking script` - This is the folder that contains a small `blink.py` micro python code that allows an LED plugged in to gpio15 via a 220-1k ohm resistor to blink in 0.5sec increments.


- `blink.py` - very tiny micro python code that allows an LED plugged in to gpio15 via a 220-1k ohm resistor to blink in 0.5sec increments.






## Firmware- 

There is a small micro python code file that allows an LED which is plugged in to gpio15 (GP15) of the devboard via a 220-1k ohm resistor to blink in 0.5 sec increments. 


**Here is the code (it is small enough to put into the readme itself too!!) ->** 

```
from machine import Pin
import time

LED = Pin(15, Pin.OUT)

while True:
    LED.on()
    time.sleep(0.5)

    LED.off()
    time.sleep(0.5)

```



***Note-> To change which GPIO Pin you attach the LED to you can just go ahead and change the line `LED = Pin(15, Pin.OUT)`  to `LED = Pin(Whatever GPIO Pin u are using, Pin.OUT)`***




## Schematic
<img width="607" height="353" alt="image" src="https://github.com/user-attachments/assets/6ddde897-305c-49bd-9f2b-889482562ed2" />
<img width="362" height="271" alt="image" src="https://github.com/user-attachments/assets/092218db-812f-49f9-baeb-46ab4b6a0ef4" />
<img width="275" height="285" alt="image" src="https://github.com/user-attachments/assets/81316212-4c52-4c03-9f1b-1ba1c71718ef" />





## PCB 


<img width="535" height="643" alt="image" src="https://github.com/user-attachments/assets/679898c2-2de4-4685-897f-3c26641e1b9f" />
<img width="1903" height="886" alt="image" src="https://github.com/user-attachments/assets/927eb713-5afd-42b0-977b-42fd5f598d80" />
<img width="610" height="598" alt="image" src="https://github.com/user-attachments/assets/9cab6b67-5702-473b-be4e-9bf3ab4b6525" />
<img width="308" height="317" alt="image" src="https://github.com/user-attachments/assets/2b5025e6-de66-4f4c-af4e-759d37e323b3" />


## CAD

<img width="1086" height="684" alt="image" src="https://github.com/user-attachments/assets/4179b569-4959-47d5-bcd7-8a2c32a2fb7c" />
<img width="928" height="733" alt="image" src="https://github.com/user-attachments/assets/f303675e-1d07-4807-9394-3b8246e8eab5" />
<img width="1915" height="981" alt="image" src="https://github.com/user-attachments/assets/a75235a8-b69f-44f9-a5c7-00c49a10c5ca" />




## License 
This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.



## Credits 

***I used the following for making this project***

- ***EasyEDA*** - For PCB design
- ***FreeCAD*** - For designing the Case
- ***JLCPCB*** - Will be using to manufacture the PCB
- **[APX HUB by @Gabouin](https://github.com/Gabouin/APX-USB-HUB)** - Readme template
- ***HACK CLUB*** - THE MOST CREDIT GOES TO HACK CLUB AS WITHOUT THEM I WOULD PROBABLY HAVE NEVER GOTTEN INTO PCB'S AND HARDWARE SO THANK U.


# Project : Digital clock
## Team members:
Member 1: GABLE Ludovic (responsible for ...)

Member 2: COULIBALY Alexandre (responsible for ...)

Member 3: TRICOT Guillaume (responsible for ...)

Member 4: GIRARDIN Loïc (responsible for ...)

## Goal :

Design and implement a digital clock using NeoPixel displays. The clock will display the current time, support alarms, and synchronize with network time servers (NTP) to ensure accurate timekeeping. Set up physical buttons or touch/proximity input to interact with the clock (e.g., set time, set alarms, snooze alarms). Implement basic functions to control the NeoPixel LEDs (e.g., setting color, brightness, and individual pixel control).

## Hardware description :

Components Used :

ESP32 Board :

Microcontroller with high performance, low power consumption and built-in Wi-Fi/Bluetooth capabilities, which can also enable future enhancements such as time synchronization via the internet.

---------------------------------------------------------------------------------------------------------------
Four 7-Segment Display :

8 digits, each made up of 14 LEDs 

Two central LEDs to separate the left and right groups (as in a digital clock).

![image](https://github.com/user-attachments/assets/23b65dbe-8a15-4b9d-ad10-8270bfe25553)



---------------------------------------------------------------------------------------------------------------
Buttons :

for user interaction:

Set the time/alarm

Enable/Disable the alarm

Change the led's color

Change the brigthness

Reset the system

Emits a sound to indicate an alarm or specific events

---------------------------------------------------------------------------------------------------------------
Key Features :

Time Display: The 7-segment display shows the time, with the central LEDs separating hours and minutes.

Button Control: Buttons allow for time configuration, alarm management and specific changes.

Sound Alarm: The buzzer produces a configurable sound for the alarm.

Connectivity (Optional): Extendable with Wi-Fi features and Time zone.

![image](https://github.com/user-attachments/assets/64eec7cb-6281-40d6-8717-3d1d4f2c6b2a)



## Software description :

## Instructions and photos :

Utilisation of buttons :

(photo des boutons et branchements sur la carte avec chiffre correspondant au bouton) 

---------------------------------------------------------------------------------------------------------------
1st mode : NORMAL MODE: 

  1 : Activate/Desactivate the Alarm
  
  2 : Switch to the mode SET TIME
  
  3 : Switch to the mode SET ALARM
  
  4 : Switch to the mode COLOR
  
  5 : Switch to the mode SET UTC
  
  6 : Reboot the ALARM and the sound when it goes to the set time

______________________________________________________________________________________________________________
2nd mode : SET TIME:
 
  1 :
 
  2 : Add 1 hour 
 
  3 : Add 1 minute
  
  4 : Validate changes and switch to NORMAL MODE
  
  5 : Cancel changes and switch to NORMAL MODE

  6 :

---------------------------------------------------------------------------------------------------------------
3rd mode : SET ALARM:
 
  1 :
 
  2 : Add 1 hour 
 
  3 : Add 1 minute
 
  4 : Validate changes and switch to NORMAL MODE
 
  5 : Cancel changes and switch to NORMAL MODE
 
  6 :

---------------------------------------------------------------------------------------------------------------
4th mode : SET COLOR:
 
  1 :
 
  2 : Change the color
 
  3 : Change the brigthness
  
  4 : Switch to the NORMAL MODE
  
  5 : Switch to the NORMAL MODE
  
  6 :
  
---------------------------------------------------------------------------------------------------------------
5th mode : SET UTC:
  
  1 :
 
  2 : Connexion to WIFI to change the clock 
 
  3 : Add 1 minute
 
  4 : Validate changes and switch to NORMAL MODE
  
  5 : Cancel changes and switch to NORMAL MODE
  
  6 :

  
## References and tools :



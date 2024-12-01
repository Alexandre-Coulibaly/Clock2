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

![image](https://github.com/user-attachments/assets/d35c2e6c-c947-4def-bcbb-e585f434bf03)


---------------------------------------------------------------------------------------------------------------
Key Features :

Time Display: The 7-segment display shows the time, with the central LEDs separating hours and minutes.

Button Control: Buttons allow for time configuration, alarm management and specific changes.

Sound Alarm: The buzzer produces a configurable sound for the alarm.

Connectivity (Optional): Extendable with Wi-Fi features and Time zone.

![image](https://github.com/user-attachments/assets/1350bd51-b984-4178-8997-7763c72f3778)




## Software description :

First we have the "[main](https://github.com/Alexandre-Coulibaly/Clock2/blob/main/main.py)", which represents the main loop where all program operations take place. It constantly monitors button inputs, updates the display and manages alarms:

Thanks to this, we can:

Flash the colon every 500 ms.

Check if a button is pressed and manage the corresponding actions.

Check whether the current time corresponds to the alarm time and trigger it if necessary.

Change display brightness at specific times.

Update the time display at each loop iteration.

Each function calls other classes to execute the corresponding operations.

---------------------------------------------------------------------------------------------------------------
Then we have the "[alarm](https://github.com/Alexandre-Coulibaly/Clock2/blob/main/alarm.py)" class, which initializes a button and a buzzer, plays a sound with the buzzer, checks whether the button is pressed, and executes an alarm management loop.
First we define the pins for the button and buzzer, then we initialize the button as input and the buzzer as PWM output.

The play_sound function sounds the buzzer for 0.5s.

The duty cycle is set to 50%, which activates the buzzer sound, but not to its maximum (100%).

The check_button_press function checks whether the button is pressed.
If the button is pressed (low state), a delay of 0.05 seconds is introduced to avoid errors.
Button pressure is checked again after the delay. If the button is still pressed, the function returns ```True``` and will then turn off the alarm.

The alarm_loop function manages the alarm loop. As long as the alarm is in progress, the function checks whether the button is pressed. If the button is pressed (previous function), the alarm stops.
If not, the buzzer sounds at regular 0.5-second intervals.
On leaving the loop, the buzzer is deactivated.

---------------------------------------------------------------------------------------------------------------


## Instructions and photos :

How to use buttons :

(photo des boutons et branchements sur la carte avec chiffre correspondant au bouton) 

---------------------------------------------------------------------------------------------------------------
1st mode : NORMAL MODE: 

  1 : Activate/Desactivate the Alarm
  
  2 : Switch to the mode SET TIME
  
  3 : Switch to the mode SET ALARM
  
  4 : Switch to the mode COLOR
  
  5 : Switch to the mode SET UTC
  
  6 : Reboot the ALARM and the sound when it goes to the set time


  ![image](https://github.com/user-attachments/assets/f6d6abd8-6e1e-4323-8d77-b3c2dc9729df)
_________________________________________________________________________________________________________
2nd mode : SET TIME:
 
  1 :
 
  2 : Add 1 hour 
 
  3 : Add 1 minute
  
  4 : Validate changes and switch to NORMAL MODE
  
  5 : Cancel changes and switch to NORMAL MODE

  6 :
  


![image](https://github.com/user-attachments/assets/bba1a103-32f6-440a-b7fb-65048f4def83)
---------------------------------------------------------------------------------------------------------------
3rd mode : SET ALARM:
 
  1 :
 
  2 : Add 1 hour 
 
  3 : Add 1 minute
 
  4 : Validate changes and switch to NORMAL MODE
 
  5 : Cancel changes and switch to NORMAL MODE
 
  6 :


![image](https://github.com/user-attachments/assets/4cedfb45-482f-4579-9691-948ba312cc88)
---------------------------------------------------------------------------------------------------------------
4th mode : SET COLOR:
 
  1 :
 
  2 : Change the color
 
  3 : Change the brigthness
  
  4 : Switch to the NORMAL MODE
  
  5 : Switch to the NORMAL MODE
  
  6 :


  ![image](https://github.com/user-attachments/assets/325b50f7-9a0d-431d-940e-ddc8a186bcb9)

---------------------------------------------------------------------------------------------------------------
5th mode : SET UTC:
  
  1 :
 
  2 : Connexion to WIFI to change the clock 
 
  3 : Add 1 minute
 
  4 : Validate changes and switch to NORMAL MODE
  
  5 : Cancel changes and switch to NORMAL MODE
  
  6 :


![image](https://github.com/user-attachments/assets/134238a4-4319-4908-9686-e9fe4afe1cc4)

## References and tools :



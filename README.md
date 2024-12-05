# Project : Digital clock
## Team members:
Member 1: GABLE Ludovic (responsible for grouping of all codes, main and buttons)

Member 2: COULIBALY Alexandre (responsible for the alarm and buttons)

Member 3: TRICOT Guillaume (responsible for the display and timer)

Member 4: GIRARDIN Loïc (responsible for the connection to internet and timer)

## Goal :

Design and implement a digital clock using NeoPixel displays. The clock will display the current time, support alarms, and synchronize with network time servers (NTP) to ensure accurate timekeeping. Set up physical buttons or touch/proximity input to interact with the clock (e.g., set time, set alarms, snooze alarms). Implement basic functions to control the NeoPixel LEDs (e.g., setting color, brightness, and individual pixel control).

## Hardware description :

Components Used :

ESP32 Board :

Microcontroller with high performance, low power consumption and built-in Wi-Fi/Bluetooth capabilities, which can also enable future enhancements such as time synchronization via the internet.

---------------------------------------------------------------------------------------------------------------
Four 7-Segment Display :

-8 digits, each made up of 14 LEDs 

-Two central LEDs to separate the left and right groups (as in a digital clock).

![image](https://github.com/user-attachments/assets/23b65dbe-8a15-4b9d-ad10-8270bfe25553)



---------------------------------------------------------------------------------------------------------------
Buttons :

for user interaction:

-Set the time/alarm

-Enable/Disable the alarm

-Change the led's color

-Change the brigthness

-Reset the system

-Emits a sound to indicate an alarm or specific events

![image](https://github.com/user-attachments/assets/d35c2e6c-c947-4def-bcbb-e585f434bf03)


---------------------------------------------------------------------------------------------------------------
Key Features :

-Time Display: The 7-segment display shows the time, with the central LEDs separating hours and minutes.

-Button Control: Buttons allow for time configuration, alarm management and specific changes.

-Sound Alarm: The buzzer produces a configurable sound for the alarm.

-Connectivity (Optional): Extendable with Wi-Fi features and Time zone.

![image](https://github.com/user-attachments/assets/1350bd51-b984-4178-8997-7763c72f3778)




## Software description :

First we have the "[main](https://github.com/Alexandre-Coulibaly/Clock2/blob/main/main.py)", which represents the main loop where all program operations take place. It constantly monitors button inputs, updates the display and manages alarms:

Thanks to this, we can:

-Flash the colon every 500 ms.

-Check if a button is pressed and manage the corresponding actions.

-Check whether the current time corresponds to the alarm time and trigger it if necessary.

-Change display brightness at specific times.

-Update the time display at each loop iteration.

-Each function calls other classes to execute the corresponding operations.

---------------------------------------------------------------------------------------------------------------
Then we have the "[alarm](https://github.com/Alexandre-Coulibaly/Clock2/blob/main/alarm.py)" class, which initializes a button and a buzzer, plays a sound with the buzzer, checks whether the button is pressed, and executes an alarm management loop.
First we define the pins for the button and buzzer, then we initialize the button as input and the buzzer as PWM output.

The ```play_sound``` function sounds the buzzer for 0.5s.

The duty cycle is set to 50%, which activates the buzzer sound, but not to its maximum (100%).

The ```check_button_press``` function checks whether the button is pressed.
If the button is pressed (low state), a delay of 0.05 seconds is introduced to avoid errors.
Button pressure is checked again after the delay. If the button is still pressed, the function returns ```True``` and will then turn off the alarm.

The ```alarm_loop``` function manages the alarm loop. As long as the alarm is in progress, the function checks whether the button is pressed. If the button is pressed (previous function), the alarm stops.
If not, the buzzer sounds at regular 0.5-second intervals.
On leaving the loop, the buzzer is deactivated.

---------------------------------------------------------------------------------------------------------------
Let's take a look at the “[button](https://github.com/Alexandre-Coulibaly/Clock2/blob/main/button.py)” class. 

First, the class initializes several variables to track the state of the clock, alarm, colors, brightness and time zones. Lists of time zones and cities are also initialized.

The handle_button_press function manages button actions according to the current clock mode, as described in the “Instructions” section.

The ``get_current_state`` function returns the current clock state for display.

Each button has a specific function depending on the current clock mode.

---------------------------------------------------------------------------------------------------------------
The “[display](https://github.com/Alexandre-Coulibaly/Clock2/blob/main/display.py)” class initializes and manages the LED display for a clock, controlling the colors, brightness and segments displayed for the hour and minute digits. It configures the overall color and brightness, and displays the hours, minutes and flashing colon between them.

LEDs are initialized using the ``neopixel'' library and pin configuration.
We also create a dictionary that defines which LED to switch on to display each digit from 0 to 9.

With ```display_digit``` we configure the LEDs to display the corresponding digit on the chosen display, avoiding the two dots in the middle.

```Display_minutes``` displays the tens and units of minutes on the respective displays.

```Display_hours``` displays tens and units of hours on the respective displays.

```Display_colon``` switches the LEDs of the two dots between hours and minutes on and off.

```set_color``` changes the display color and applies the new color to all LEDs.

```set_brightness``` changes the brightness and ensures that it remains within a valid range.

```apply_color_to_leds``` changes the color of all LEDs according to the brightness set.

``apply_brightness`` returns the current brightness value.

---------------------------------------------------------------------------------------------------------------

We will now take a look at the "[timer](https://github.com/Alexandre-Coulibaly/Clock2/blob/main/timer.py)" class. This class configures a stopwatch that tracks elapsed time in hundredths of a second, seconds, minutes and hours, and allows setting and viewing of the current time.

The function ```stopwatch_100ms``` is called every 100 milliseconds by the timer. It increments the tenths of a second (```tenths```). When it reaches 10, it resets to 0 and increments the seconds (```secs```). Similarly, it manages the incrementation of minutes (```mins```) and hours (```hours```), looping after 24 hours.

```set_current_time``` and ```set_current_time_wifi``` are used to manually update the current time. The second function also allows setting the seconds.

The function ```get_current_time``` returns the current hours and minutes.

Finally, all the necessary global variables are initialized, and the Timer is set up to call ```stopwatch_100ms``` every 100 milliseconds (period=100): 

```
tenths = 0
secs = 0
mins = 0
hours = 0
colon_state = True

tim = Timer(0)
tim.init(period=100, mode=Timer.PERIODIC, callback=stopwatch_100ms)
```
---------------------------------------------------------------------------------------------------------------

Finally, there is the "[wifi](https://github.com/Alexandre-Coulibaly/Clock2/blob/main/wifi.py)" class. This code connects the device to a specified Wi-Fi network and synchronizes the device's time using NTP.

First, we have to import modules like ```network``` for Wi-Fi functions, ```ntptime``` for getting the current time via NTP, and ```time``` for handling time-related functions.

```
WIFI_SSID = 'SSID'
WIFI_PASSWORD = 'PSWD'
```
These lines set the SSID and password for the Wi-Fi network we want to connect to.

Then, The function ```connect_wifi``` attempts to connect to the specified Wi-Fi network. It initializes the Wi-Fi module and tries to connect within a 30-second timeout period. It prints the connection status and IP address once connected.

```get_wifi_time``` synchronizes the current time using NTP. It retrieves the local time and returns the current hour, minute, and second. If there’s an error, it prints the error message and returns ```None```.

The function ```connect``` checks if the device is already connected to Wi-Fi. If not, it calls ```connect_wifi```to establish the connection.

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


![image](https://github.com/user-attachments/assets/9780860a-7095-458f-a40c-135fdf85c55f)

_________________________________________________________________________________________________________
2nd mode : SET TIME:
 
  1 :
 
  2 : Add 1 hour 
 
  3 : Add 1 minute
  
  4 : Validate changes and switch to NORMAL MODE
  
  5 : Cancel changes and switch to NORMAL MODE

  6 :
  


![image](https://github.com/user-attachments/assets/019bba5b-209b-4f68-86c4-f15e4b0d35b3)

---------------------------------------------------------------------------------------------------------------
3rd mode : SET ALARM:
 
  1 :
 
  2 : Add 1 hour 
 
  3 : Add 1 minute
 
  4 : Validate changes and switch to NORMAL MODE
 
  5 : Cancel changes and switch to NORMAL MODE
 
  6 :


![image](https://github.com/user-attachments/assets/1a78f72c-ee06-40c9-b1fd-e4da43d91065)

---------------------------------------------------------------------------------------------------------------
4th mode : SET COLOR:
 
  1 :
 
  2 : Change the color
 
  3 : Change the brigthness
  
  4 : Switch to the NORMAL MODE
  
  5 : Switch to the NORMAL MODE
  
  6 :


![image](https://github.com/user-attachments/assets/96fc6011-ab76-46b5-8325-741be86fddd2)

---------------------------------------------------------------------------------------------------------------
5th mode : SET UTC:
  
  1 :
 
  2 : Connexion to WIFI to change the clock 
 
  3 : Change Time Zone
 
  4 : Validate changes and switch to NORMAL MODE
  
  5 : Cancel changes and switch to NORMAL MODE
  
  6 :

  Disclaimer to change time zone you must first connect to the wifi to get the time reset to UTC 0.
  
![image](https://github.com/user-attachments/assets/bd4785e9-8bfd-41d3-9d6a-736390044f2e)


## References and tools :



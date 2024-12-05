from machine import Pin
from button_control import ButtonController
from display import display_hours, display_minutes, display_colon, set_brightness, get_BRIGHTNESS
from chrono import get_current_time, set_current_time
from alarm import alarm_loop
import time


# Initializing buttons
button_pins = {   #use in main
    1: Pin(25, Pin.IN, Pin.PULL_UP),  # Bouton 1 - On/off Alarm 
    2: Pin(26, Pin.IN, Pin.PULL_UP),  # Bouton 2 - settime
    3: Pin(27, Pin.IN, Pin.PULL_UP),  # Bouton 3 - setalarm
    4: Pin(13, Pin.IN, Pin.PULL_UP),  # Bouton 4 - setcolor
    5: Pin(5, Pin.IN, Pin.PULL_UP),  # Bouton 5 - setUTC
}

# Initializing buttons Controller()
button_controller = ButtonController()

# Variables to manage the display of the two points
colon_state = True  # The two dots are flashing
last_colon_toggle = time.ticks_ms()

def read_buttons():
    """
    verify if the button is pressed
    :return: number of the button pressed or None
    """
    for button, pin in button_pins.items():
        if not pin.value():  # Button pressed (value = 0 when pressed in PULL_UP)
            time.sleep(0.3)  # Anti-rebound
            return button
    return None

def update_display():
    """
    Updates the display of the LEDs according to the current mode and values.
    """
    state = button_controller.get_current_state()
    
   
    if state["mode"] == "set_time":
        # set time mode: Displays temporary values
        display_hours(button_controller.currenthold_hour)
        display_minutes(button_controller.currenthold_minute)
    elif state["mode"] == "set_alarm":
        # set alarm mode: Displays temporary values
        display_hours(button_controller.alarmhold_hour)
        display_minutes(button_controller.alarmhold_minute)
    elif state["mode"] == "set_UTC":
        # setUTC mode : Displays temporary values
        display_hours(button_controller.currenthold_hour)
        display_minutes(button_controller.currenthold_minute)
    else:
        # normal mode or setcolor: Displays the current time
        hours, minutes = get_current_time()
        display_hours(hours)
        display_minutes(minutes)


    # Displays the two flashing dots in all cases
    display_colon(colon_state)


# Main loop
while True:
    # flashing of the two dots
    if time.ticks_diff(time.ticks_ms(), last_colon_toggle) > 500:  # Change every 500 ms

        colon_state = not colon_state
        display_colon(colon_state)
        last_colon_toggle = time.ticks_ms()

    # verify if a button is pressed
    pressed_button = read_buttons()

    if pressed_button:
        print(f"Button {pressed_button} pressed")
        button_controller.handle_button_press(pressed_button)  # Manage button action
        update_display()  # Updates the display after an action
        print("Current states :", button_controller.get_current_state())
    
    if button_controller.alarm_active:  # If alarm activated
        current_hour, current_minute = get_current_time()  #Take current time
        if (current_hour == button_controller.alarm_hour and
            current_minute == button_controller.alarm_minute):
            print("alarm is triggered !")
            alarm_loop()  # Initiates the alarm loop
            button_controller.alarm_active = False  # Disables the alarm after triggering
    
    # Automatic brightness change
    current_hour, current_minute = get_current_time()  #Take current time
    BRIGHTNESS =get_BRIGHTNESS()
    if (current_hour == 21) and (current_minute == 01) and (BRIGHTNESS != 0.3): #look if time is matching
        set_brightness(0.3)
    elif (current_hour == 8) and (current_minute == 01) and (BRIGHTNESS != 0.7): #look if time is matching
        set_brightness(0.7)
    # Updates the display
    
    update_display()
   
    time.sleep(0.1)  # anti-rebound
    




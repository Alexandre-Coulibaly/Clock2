from machine import Pin, PWM
import time

# Pin Configuration
BUTTON_PIN = 2  # Pin connected to the button
BUZZER_PIN = 12  # Pin connected to the buzzer

button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_UP)

# Initializing the buzzer in PWM output
buzzer = PWM(Pin(BUZZER_PIN), freq=1000, duty=0)  #  Initial frequency at 1kHz, duty cycle at 0%

def play_sound(duration=0.5):
    """ the buzzer make sound for the specified amount of time."""
    buzzer.duty(512)  # Sets the duty cycle to 50%
    time.sleep(duration)
    buzzer.duty(0)    # Stop the sound

def check_button_press():
    """
    Checks if the button is pressed with software anti-bounce.
    :return: True if the button is pressed (low state), False otherwise.
    """
    if not button.value():  #  If the button is pressed (low state)
        time.sleep(0.05)  # Anti-kickback delay
        if not button.value():  # Check again after the delay
            return True
    return False

def alarm_loop():
    """Main loop to manage the alarm."""
    print("Alarm On. Press the button to stop.")
    alarm_running = True

    while alarm_running:
        try:
            if check_button_press():  # If the button is pressed
                print("Button pressed, alarm stop.")
                alarm_running = False
            else:
                play_sound(0.5)
                time.sleep(0.5)  
        except KeyboardInterrupt:
            print("Interrupt detected, alarm stopped.")
            alarm_running = False

  # Clean buzzer duty after exiting the loop
    buzzer.duty(0)
    print("Alarm Off.")









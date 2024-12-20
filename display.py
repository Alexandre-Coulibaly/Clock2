import utime
from machine import Pin
import neopixel

#Configuration
LED_PIN = 4  # Pin connected to the DO line of the LEDs
NUM_DISPLAYS = 4  # total of display (2 hours + 2 for minutes)
LEDS_PER_DISPLAY = 14  # number of LEDS per display
TOTAL_LEDS = NUM_DISPLAYS * LEDS_PER_DISPLAY + 2  # Total of LEDs (28 for the 4 display + 2 for the 2 dots)

#  Initializing LEDs
np = neopixel.NeoPixel(Pin(LED_PIN, Pin.OUT), TOTAL_LEDS)

# Segment map for every number (14 LEDs per digit)
SEGMENT_MAP = {
    0: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    1: [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    2: [0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1],
    3: [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1],
    4: [1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1],
    5: [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1],
    6: [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    7: [0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    8: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    9: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1],
}



# setting Brightness
BRIGHTNESS = 0.2  # Réglez la luminosité (0.0 = éteint, 1.0 = plein éclairage)
CURRENT_COLOR = (50, 50, 50)



# LED display management
def display_digit(digit, display_index):
    """Displays a number on a specific display."""
    config = SEGMENT_MAP[digit]
    # Compensates for the offset of the LEDs of the two flashing points
    start_index = display_index * LEDS_PER_DISPLAY
    if display_index >= 2:
        start_index += 2  # Offset of 2 LEDs to avoid the two dots

    if start_index + LEDS_PER_DISPLAY > TOTAL_LEDS:
        raise IndexError("The index exceeds the total number of configured LEDs.")


    for i in range(LEDS_PER_DISPLAY):
        # Turns the corresponding LED on or off with adjusted brightness
        color = CURRENT_COLOR if config[i] else (0, 0, 0)
        np[start_index + i] = apply_brightness(color)
    np.write()

def display_minutes(minutes):
    """Displays the minutes on both displays."""
    display_digit(minutes // 10, 2)  # Dizaine des minutes
    display_digit(minutes % 10, 3)  # Unité des minutes

def display_hours(hours):
    """Displays the times on both displays."""
    display_digit(hours // 10, 0)  # Dizaine des heures
    display_digit(hours % 10, 1)  # Unité des heures

def display_colon(state):
    """Displays the colon between the hours and minutes."""
    # Flashes the 2 LEDs of the dots (index 28 and 29)
    color = apply_brightness(CURRENT_COLOR) if state else (0, 0, 0)
    np[28] = color  # LED 1 pour le point
    np[29] = color  # LED 2 pour le point
    np.write()

# Color Setting
def set_color(color):
    """ Changes the overall color."""
    global CURRENT_COLOR
    CURRENT_COLOR = color
    apply_color_to_leds(color)
    print(f"New color : {CURRENT_COLOR}")

def set_brightness(level):
    """Changes the overall brightness."""
    global BRIGHTNESS
    BRIGHTNESS = max(0.1, min(level, 1.0))  # Keeps brightness within a valid range
    print(f"New Brightness : {BRIGHTNESS}")



def apply_color_to_leds(color):
    """
    Applies a color (adjusted in brightness) to all LEDs.
    :param color: Tuple RGB (for example, (50, 0, 0)).
    """
    for i in range(len(np)):
        np[i] = apply_brightness(color)
    np.write()

def apply_brightness(color):
    """Adjusts the brightness of an RGB color."""
    return tuple(int(c * BRIGHTNESS) for c in color)

def get_BRIGHTNESS():
    return BRIGHTNESS  #give the actual brightness




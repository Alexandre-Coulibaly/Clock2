from machine import Timer
from display import display_hours, display_minutes, display_colon

# Chronometer
def stopwatch_100ms(t):
    """Interrupt handler de Timer Run every 100 ms."""
    global tenths, secs, mins, hours, colon_state

    # Increments tenths of a second
    tenths += 1
    if tenths >= 10:
        tenths = 0
        secs += 1

        # Increments seconds
        if secs >= 60:
            secs = 0
            mins += 1

        # Increments minutes
        if mins >= 60:
            mins = 0
            hours += 1

        #  Increments hours
        if hours >= 24:  # Loop after 24 hours
            hours = 0

   

def set_current_time(new_hours, new_minutes):
    """Updates the Chronometer time."""
    global hours, mins, secs
    hours = new_hours % 24
    mins = new_minutes % 60
    secs = 0  # Reset seconds to 0
    
def set_current_time_wifi(new_hours, new_minutes, new_secondes):
    """Updates the Chronometer time with wifi time."""
    global hours, mins, secs
    hours = new_hours % 24
    mins = new_minutes % 60
    secs = new_secondes % 60  # Reset seconds to 0

def get_current_time():
    """Returns the current time as a tuple (hours, minutes)."""
    global hours, mins
    return hours, mins

# Initialization
tenths = 0  
secs = 0    # Seconds
mins = 0    # Minutes
hours = 0   # Hours
colon_state = True  # States of the two flashing dots

# Set the timer to 100ms
tim = Timer(0)
tim.init(period=100, mode=Timer.PERIODIC, callback=stopwatch_100ms)








from display import set_color, set_brightness, CURRENT_COLOR, BRIGHTNESS
from chrono import get_current_time, set_current_time, set_current_time_wifi
from wifi import connect, get_wifi_time



class ButtonController:
    def __init__(self):
        # Variables
        self.current_mode = "normal"  # Modes : "normal", "set_time", "set_alarm", "set_color"
        self.currenthold_hour = 0
        self.currenthold_minute =0
        self.currenthold_seconde =0 
        self.alarm_hour = 6
        self.alarm_minute = 0
        self.alarmhold_hour = 0
        self.alarmhold_minute = 0
        self.alarm_active = False
        self.current_color =0
        self.currenthold_brightness = BRIGHTNESS  
        self.current_timezone = 0
        self.timezones = [
            0,
            1,
            -6,
            3,
            9,
            -8
        ]
        
        self.city = [
            {"London"},
            {"Paris" },
            {"New York" },
            {"Moscow" },
            {"Tokyo" },
            {"Los Angeles" }
        ]


        # List of available colors
        self.AVAILABLE_COLORS = [
            (50, 50, 50), # white
            (50, 0, 0),  # Red
            (0, 50, 0),  # Green
            (0, 0, 50),  # Blue
            (50, 50, 0), # Yellow
            (50, 0, 50), # Magenta
            (0, 50, 50), # Cyan
        ]


    def handle_button_press(self, button):  
        """
        Manages button actions based on the current mode.

        :param button: Button number pressed (1 to 5)
        """
        if self.current_mode == "normal":
            if button == 1:
                self.alarm_active = not self.alarm_active  # Enable/Disable Alarm
                print(f"Alarm {'Enable' if self.alarm_active else 'Disable'}")
                
            elif button == 2:
                self.current_mode = "set_time"  # Pass to mode "Set Time"
                print("Entering Set Time Mode")
                hours, minutes = get_current_time()
                self.currenthold_hour = hours
                self.currenthold_minute = minutes
                
            elif button == 3:
                self.current_mode = "set_alarm"  # Pass to mode "Set Alarm"
                print("Entering Set Alarm Mode")
                self.alarmhold_hour = self.alarm_hour
                self.alarmhold_minute = self.alarm_minute
                
                
            elif button == 4:
                self.current_mode = "set_color"  # Pass to mode "Set Color"
                print("Entering Set Color Mode")
                
            elif button == 5:
                self.current_mode = "set_UTC"  # Passer en mode "Set UTC"
                print("Entering Set UTC Mode")
                hours, minutes = get_current_time()
                self.currenthold_hour = hours
                self.currenthold_minute = minutes
                
   
        elif self.current_mode == "set_time":
            if button == 2:
                self.currenthold_hour = (self.currenthold_hour + 1) % 24  # increase Hours
                print(f"New hours : {self.currenthold_hour}")
                 
            elif button == 3:
                self.currenthold_minute = (self.currenthold_minute + 1) % 60  # Increase minutes
                print(f"New Minutes : {self.currenthold_minute}")
                 
            elif button == 4:
                set_current_time(self.currenthold_hour, self.currenthold_minute)
                self.current_mode = "normal"  # Validate changes
                print("Time set, return to normal mode")
                 
            elif button == 5:
                self.current_mode = "normal"  # Cancel and return to normal mode
                print("Cancel changes, return to normal model")
                 

        elif self.current_mode == "set_alarm":
            if button == 2:
                self.alarmhold_hour = (self.alarmhold_hour + 1) % 24  #increase alarm hours
                print(f"Alarme - Hours : {self.alarmhold_hour}")
                 
            elif button == 3:
                self.alarmhold_minute = (self.alarmhold_minute + 1) % 60  # increase alarm minutes
                print(f"Alarm - Minutes : {self.alarmhold_minute}")
                 
            elif button == 4:
                self.alarm_hour = self.alarmhold_hour
                self.alarm_minute = self.alarmhold_minute
                self.current_mode = "normal"  # Validate changes
                print("Alarm set, back to normal mode")
                 
            elif button == 5:
                self.alarmhold_hour = self.alarm_hour
                self.alarmhold_minute = self.alarm_minute
                self.current_mode = "normal"  # Cancel and return to normal mode
                print("Cancel alarm settings, return to normal mode")
                 
               
             
               
               
        elif self.current_mode == "set_color":
            if button == 2:
                print(f"Change Color: {}")
                #color
                self.current_color = (self.current_color + 1) % len(self.AVAILABLE_COLORS)
                set_color(self.AVAILABLE_COLORS[self.current_color])  # Apply Color 

                 
            if button == 3:
                #brightness
                self.currenthold_brightness += 0.1
                if self.currenthold_brightness > 1.0:  #  If the brightness exceeds 1.0
                    self.currenthold_brightness = 0.2  # come back at 0.2
                set_brightness(self.currenthold_brightness)
                print(f"Changing Brightness {}")
                 
            if button == 4:
                #valide
                print(f"return: {}")
                self.current_mode = "normal"  #return to normal mode
                
                 
            if button == 5:
                #annule
                print(f"return: {}")
                self.current_mode = "normal" #return to normal mode
                 
               
               
               
               
        elif self.current_mode == "set_UTC":
            if button == 2:
                print("Attempting to sync over Wi-Fi")
                connect('T Moch', 'Pignoufs')
                self.currenthold_hour, self.currenthold_minute, self.currenthold_seconde  = get_wifi_time()
            
             
            
            if button == 3:
                self.current_timezone = (self.current_timezone + 1) % len(self.timezones)
                hours = self.timezones[self.current_timezone]
                city = self.city[self.current_timezone]

                # Adjusts the time for the time zone
                self.currenthold_hour = (self.currenthold_hour + hours) % 24
                
                print(f"Time zone changed : {city} ({hours:+}H)")
                print(f"Displayed time : {self.currenthold_hour:02}:{self.currenthold_minute:02}")
                 


    
    
            if button == 4:
                #validate
                print(f"Validation of the new wifi time")
                set_current_time_wifi(self.currenthold_hour, self.currenthold_minute, self.currenthold_seconde)
                self.current_mode = "normal"  # Validate and return to normal mode
                
                 
            if button == 5:
                #annule
                print(f"Cancel new wifi time")
                self.current_mode = "normal"  # Cancel and return to normal mode
                 
          

    def get_current_state(self):
        """
        Returns the current state of the clock for display or verification.
        """
        hours, minutes = get_current_time()
        return {
            "mode": self.current_mode,
            "current_time": f"{hours:02}:{minutes:02}",
            "alarm_time": f"{self.alarm_hour:02}:{self.alarm_minute:02}",
            "alarm_active": self.alarm_active,
        }






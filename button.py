from display import set_color, set_brightness, CURRENT_COLOR, BRIGHTNESS
from chrono import get_current_time, set_current_time, set_current_time_wifi
from wifi import connect, get_wifi_time



class ButtonController:
    def __init__(self):
        # Variables pour suivre l'état
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
        self.currenthold_brightness = BRIGHTNESS  # Luminosité 
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
            {"Londre"},
            {"Paris" },
            {"New york" },
            {"Moscou" },
            {"Tokyo" },
            {"Los Angeles" }
        ]


        # === Liste des couleurs disponibles ===
        self.AVAILABLE_COLORS = [
            (50, 50, 50), # Blanc
            (50, 0, 0),  # Rouge
            (0, 50, 0),  # Vert
            (0, 0, 50),  # Bleu
            (50, 50, 0), # Jaune
            (50, 0, 50), # Magenta
            (0, 50, 50), # Cyan
        ]


    def handle_button_press(self, button):
        """
        Gère les actions des boutons en fonction du mode actuel.

        :param button: Numéro du bouton pressé (1 à 5)
        """
        if self.current_mode == "normal":
            if button == 1:
                self.alarm_active = not self.alarm_active  # Activer/Désactiver l'alarme
                print(f"Alarme {'activée' if self.alarm_active else 'désactivée'}")
                
            elif button == 2:
                self.current_mode = "set_time"  # Passer en mode "Set Time"
                print("Entrée dans le mode réglage de l'heure")
                hours, minutes = get_current_time()
                self.currenthold_hour = hours
                self.currenthold_minute = minutes
                
            elif button == 3:
                self.current_mode = "set_alarm"  # Passer en mode "Set Alarm"
                print("Entrée dans le mode réglage de l'alarme")
                self.alarmhold_hour = self.alarm_hour
                self.alarmhold_minute = self.alarm_minute
                
                
            elif button == 4:
                self.current_mode = "set_color"  # Passer en mode "Set Alarm"
                print("Entrée dans le mode réglage de des couleurs")
                
            elif button == 5:
                self.current_mode = "set_UTC"  # Passer en mode "Set Alarm"
                print("Entrée dans le mode réglage du temps UTC")
                
   
        elif self.current_mode == "set_time":
            if button == 2:
                self.currenthold_hour = (self.currenthold_hour + 1) % 24  # Augmenter l'heure
                print(f"nouvelle Heure : {self.currenthold_hour}")
                 
            elif button == 3:
                self.currenthold_minute = (self.currenthold_minute + 1) % 60  # Augmenter les minutes
                print(f"nouvelle Minutes : {self.currenthold_minute}")
                 
            elif button == 4:
                set_current_time(self.currenthold_hour, self.currenthold_minute)
                self.current_mode = "normal"  # Valider les changements
                print("Heure réglée, retour au mode normal")
                 
            elif button == 5:
                self.current_mode = "normal"  # Annuler et revenir au mode normal
                print("Annulation des changements, retour au mode normal")
                 

        elif self.current_mode == "set_alarm":
            if button == 2:
                self.alarmhold_hour = (self.alarmhold_hour + 1) % 24  # Augmenter l'heure de l'alarme
                print(f"Alarme - Heure : {self.alarmhold_hour}")
                 
            elif button == 3:
                self.alarmhold_minute = (self.alarmhold_minute + 1) % 60  # Augmenter les minutes de l'alarme
                print(f"Alarme - Minutes : {self.alarmhold_minute}")
                 
            elif button == 4:
                self.alarm_hour = self.alarmhold_hour
                self.alarm_minute = self.alarmhold_minute
                self.current_mode = "normal"  # Valider les changements
                print("Alarme réglée, retour au mode normal")
                 
            elif button == 5:
                self.alarmhold_hour = self.alarm_hour
                self.alarmhold_minute = self.alarm_minute
                self.current_mode = "normal"  # Annuler et revenir au mode normal
                print("Annulation des réglages de l'alarme, retour au mode normal")
                 
               
             
               
               
        elif self.current_mode == "set_color":
            if button == 2:
                print(f"changement luminossité: {}")
                #color
                self.current_color = (self.current_color + 1) % len(self.AVAILABLE_COLORS)
                set_color(self.AVAILABLE_COLORS[self.current_color])  # Applique la couleur temporairement

                 
            if button == 3:
                #brightness
                self.currenthold_brightness += 0.1
                if self.currenthold_brightness > 1.0:  # Si la luminosité dépasse 1.0
                    self.currenthold_brightness = 0.2  # Revenir à la valeur minimale (0.1)
                set_brightness(self.currenthold_brightness)
                print(f"changement luminosité {}")
                 
            if button == 4:
                #valide
                print(f"retour: {}")
                self.current_mode = "normal"  # Annuler et revenir au mode normal
                
                 
            if button == 5:
                #annule
                print(f"retour: {}")
                self.current_mode = "normal"
                 
               
               
               
               
        elif self.current_mode == "set_UTC":
            if button == 2:
                print("Tentative de synchronisation via Wifi")
                connect('T Moch', 'Pignoufs')
                self.currenthold_hour, self.currenthold_minute, self.currenthold_seconde  = get_wifi_time()
            
             
            
            if button == 3:
                self.current_timezone = (self.current_timezone + 1) % len(self.timezones)
                hours = self.timezones[self.current_timezone]
                city = self.city[self.current_timezone]

                # Ajuste l'heure pour le fuseau horaire
                self.currenthold_hour = (self.currenthold_hour + hours) % 24
                
                print(f"Fuseau horaire changé : {city} ({hours:+}H)")
                print(f"Heure affichée : {self.currenthold_hour:02}:{self.currenthold_minute:02}")
                 


    
    
            if button == 4:
                #valide
                print(f"validation de l’heure wifi")
                set_current_time_wifi(self.currenthold_hour, self.currenthold_minute, self.currenthold_seconde)
                self.current_mode = "normal"  # Annuler et revenir au mode normal
                
                 
            if button == 5:
                #annule
                print(f"annulation de l’heure wifi")
                self.current_mode = "normal"  # Annuler et revenir au mode normal
                 
          

    def get_current_state(self):
        """
        Retourne l'état actuel de l'horloge pour affichage ou vérification.
        """
        hours, minutes = get_current_time()
        return {
            "mode": self.current_mode,
            "current_time": f"{hours:02}:{minutes:02}",
            "alarm_time": f"{self.alarm_hour:02}:{self.alarm_minute:02}",
            "alarm_active": self.alarm_active,
        }







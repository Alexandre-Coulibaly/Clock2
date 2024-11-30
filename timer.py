from machine import Timer
from display import display_hours, display_minutes, display_colon

# === Chronomètre ===
def stopwatch_100ms(t):
    """Interrupt handler de Timer exécuté toutes les 100ms."""
    global tenths, secs, mins, hours, colon_state

    # Incrémente les centièmes de seconde
    tenths += 1
    if tenths >= 10:
        tenths = 0
        secs += 1

        # Incrémente les secondes
        if secs >= 60:
            secs = 0
            mins += 1

        # Incrémente les minutes
        if mins >= 60:
            mins = 0
            hours += 1

        # Incrémente les heures
        if hours >= 24:  # Boucle après 24 heures
            hours = 0

   

def set_current_time(new_hours, new_minutes):
    """Met à jour l'heure du chronomètre."""
    global hours, mins, secs
    hours = new_hours % 24
    mins = new_minutes % 60
    secs = 0  # Réinitialiser les secondes à 0
    
def set_current_time_wifi(new_hours, new_minutes, new_secondes):
    """Met à jour l'heure du chronomètre."""
    global hours, mins, secs
    hours = new_hours % 24
    mins = new_minutes % 60
    secs = new_secondes % 60  # Réinitialiser les secondes à 0

def get_current_time():
    """Retourne l'heure actuelle sous forme de tuple (heures, minutes)."""
    global hours, mins
    return hours, mins

# === Initialisation ===
tenths = 0  # Centièmes de seconde
secs = 0    # Secondes
mins = 0    # Minutes
hours = 0   # Heures
colon_state = True  # État des deux points clignotants

# Définir le timer à 100ms
tim = Timer(0)
tim.init(period=100, mode=Timer.PERIODIC, callback=stopwatch_100ms)





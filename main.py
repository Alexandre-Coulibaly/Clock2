from machine import Pin
from button_control import ButtonController
from display import display_hours, display_minutes, display_colon, set_brightness, get_BRIGHTNESS
from chrono import get_current_time, set_current_time
from alarm import alarm_loop
import time


# Initialisation des broches pour les boutons
button_pins = {
    1: Pin(25, Pin.IN, Pin.PULL_UP),  # Bouton 1 - Allumer/Éteindre l'alarme
    2: Pin(26, Pin.IN, Pin.PULL_UP),  # Bouton 2 - Mode ou +1 Heure
    3: Pin(27, Pin.IN, Pin.PULL_UP),  # Bouton 3 - +1 Minute
    4: Pin(13, Pin.IN, Pin.PULL_UP),  # Bouton 4 - Valider
    5: Pin(5, Pin.IN, Pin.PULL_UP),  # Bouton 5 - Annuler
}

# Initialisation du contrôleur de boutons
button_controller = ButtonController()

# Variables pour gérer l'affichage des deux points
colon_state = True  # Les deux points clignotent
last_colon_toggle = time.ticks_ms()

def read_buttons():
    """
    Vérifie quel bouton est pressé.
    :return: Numéro du bouton pressé ou None
    """
    for button, pin in button_pins.items():
        if not pin.value():  # Bouton pressé (LOW = actif avec PULL_UP)
            time.sleep(0.3)  # Anti-rebond
            return button
    return None

def update_display():
    """
    Met à jour l'affichage des LEDs en fonction du mode et des valeurs en cours.
    """
    state = button_controller.get_current_state()
    
   
    if state["mode"] == "set_time":
        # Mode réglage de l'heure : Affiche les valeurs temporaires
        display_hours(button_controller.currenthold_hour)
        display_minutes(button_controller.currenthold_minute)
    elif state["mode"] == "set_alarm":
        # Mode réglage de l'alarme : Affiche les valeurs temporaires
        display_hours(button_controller.alarmhold_hour)
        display_minutes(button_controller.alarmhold_minute)
    elif state["mode"] == "set_UTC":
        # Mode réglage de l'heure : Affiche les valeurs temporaires
        display_hours(button_controller.currenthold_hour)
        display_minutes(button_controller.currenthold_minute)
    else:
    # Mode normal, set_color, etc : Affiche l'heure actuelle
        hours, minutes = get_current_time()
        display_hours(hours)
        display_minutes(minutes)


    # Affiche les deux points clignotants dans tous les cas
    display_colon(colon_state)


# Boucle principale
while True:
    # Clignotement des deux points
    if time.ticks_diff(time.ticks_ms(), last_colon_toggle) > 500:  # Changement toutes les 500 ms
        colon_state = not colon_state
        display_colon(colon_state)
        last_colon_toggle = time.ticks_ms()

    # Vérifie si un bouton est pressé
    pressed_button = read_buttons()

    if pressed_button:
        print(f"Bouton {pressed_button} pressé")
        button_controller.handle_button_press(pressed_button)  # Gérer l'action du bouton
        update_display()  # Met à jour l'affichage après une action
        print("État actuel :", button_controller.get_current_state())
    
    if button_controller.alarm_active:  # Si l'alarme est activée
        current_hour, current_minute = get_current_time()  # Récupère l'heure actuelle
        if (current_hour == button_controller.alarm_hour and
            current_minute == button_controller.alarm_minute):
            print("L'alarme est déclenchée !")
            alarm_loop()  # Lance la boucle d'alarme
            button_controller.alarm_active = False  # Désactive l'alarme après déclenchement
    
    current_hour, current_minute = get_current_time()
    BRIGHTNESS =get_BRIGHTNESS()
    if (current_hour == 21) and (current_minute == 01) and (BRIGHTNESS != 0.3):
        set_brightness(0.3)
    elif (current_hour == 8) and (current_minute == 01) and (BRIGHTNESS != 0.7):
        set_brightness(0.7)
# Met à jour l'affichage
    
    update_display()
   
    time.sleep(0.1)  # Anti-rebond simple

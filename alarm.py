from machine import Pin, PWM
import time

# Configuration des broches
BUTTON_PIN = 2  # Broche connectée au bouton
BUZZER_PIN = 12  # Broche connectée au buzzer

# Initialisation du bouton en entrée avec résistance pull-up interne
button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_UP)

# Initialisation du buzzer en sortie PWM
buzzer = PWM(Pin(BUZZER_PIN), freq=1000, duty=0)  # Fréquence initiale à 1kHz, duty cycle à 0%

def play_sound(duration=0.5):
    """Fait sonner le buzzer pendant la durée spécifiée."""
    buzzer.duty(512)  # Définit le duty cycle à 50%
    time.sleep(duration)
    buzzer.duty(0)    # Arrête le son

def check_button_press():
    """
    Vérifie si le bouton est pressé avec anti-rebond logiciel.
    :return: True si le bouton est pressé (état bas), False sinon.
    """
    if not button.value():  # Si le bouton est pressé (état bas)
        time.sleep(0.05)  # Délai pour anti-rebond
        if not button.value():  # Vérifie à nouveau après le délai
            return True
    return False

def alarm_loop():
    """Boucle principale pour gérer l'alarme."""
    print("Alarme active. Appuyez sur le bouton pour arrêter.")
    alarm_running = True

    while alarm_running:
        try:
            if check_button_press():  # Si le bouton est pressé
                print("Bouton pressé, arrêt de l'alarme.")
                alarm_running = False
            else:
                play_sound(0.5)  # Joue le son à intervalles
                time.sleep(0.5)  # Pause entre les sons
        except KeyboardInterrupt:
            print("Interruption détectée, arrêt de l'alarme.")
            alarm_running = False

    # Désactivation propre du buzzer après la sortie de la boucle
    buzzer.duty(0)
    print("Alarme désactivée.")






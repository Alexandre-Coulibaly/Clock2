import network
import ntptime
import utime
from machine import Pin
import neopixel

# === Configuration matériel ===
LED_PIN = 4  # Pin connecté à la ligne DO des LEDs
NUM_DISPLAYS = 4  # Total des afficheurs (2 pour l'heure + 2 pour les minutes)
LEDS_PER_DISPLAY = 14  # Nombre de LEDs par afficheur
TOTAL_LEDS = NUM_DISPLAYS * LEDS_PER_DISPLAY + 2  # Total de LEDs (28 pour les 4 afficheurs + 2 pour les points)

# Initialisation des LEDs
np = neopixel.NeoPixel(Pin(LED_PIN, Pin.OUT), TOTAL_LEDS)

# Segment map pour chaque chiffre (14 LEDs par chiffre)
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



# === Réglage de la luminosité ===
BRIGHTNESS = 0.2  # Réglez la luminosité (0.0 = éteint, 1.0 = plein éclairage)
CURRENT_COLOR = (50, 50, 50)



# === Gestion de l'affichage des LEDs ===
def display_digit(digit, display_index):
    """Affiche un chiffre sur un afficheur spécifique."""
    config = SEGMENT_MAP[digit]
    # Compense l'offset des LEDs des deux points clignotants
    start_index = display_index * LEDS_PER_DISPLAY
    if display_index >= 2:
        start_index += 2  # Décale de 2 LEDs pour éviter les deux points

    if start_index + LEDS_PER_DISPLAY > TOTAL_LEDS:
        raise IndexError("L'indice dépasse le nombre total de LEDs configurées.")


    for i in range(LEDS_PER_DISPLAY):
        # Allume ou éteint la LED correspondante avec luminosité ajustée
        color = CURRENT_COLOR if config[i] else (0, 0, 0)
        np[start_index + i] = apply_brightness(color)
    np.write()

def display_minutes(minutes):
    """Affiche les minutes sur les deux afficheurs."""
    display_digit(minutes // 10, 2)  # Dizaine des minutes
    display_digit(minutes % 10, 3)  # Unité des minutes

def display_hours(hours):
    """Affiche les heures sur les deux afficheurs."""
    display_digit(hours // 10, 0)  # Dizaine des heures
    display_digit(hours % 10, 1)  # Unité des heures

def display_colon(state):
    """Affiche les deux points entre les heures et les minutes."""
    # Clignote les 2 LEDs des points (indices 28 et 29)
    color = apply_brightness(CURRENT_COLOR) if state else (0, 0, 0)
    np[28] = color  # LED 1 pour le point
    np[29] = color  # LED 2 pour le point
    np.write()

# === Gestion de la couleur ===
def set_color(color):
    """Change la couleur globale."""
    global CURRENT_COLOR
    CURRENT_COLOR = color
    apply_color_to_leds(color)
    print(f"Nouvelle couleur : {CURRENT_COLOR}")

def set_brightness(level):
    """Change la luminosité globale."""
    global BRIGHTNESS
    BRIGHTNESS = max(0.1, min(level, 1.0))  # Garde la luminosité dans une plage valide
    print(f"Nouvelle luminosité : {BRIGHTNESS}")



def apply_color_to_leds(color):
    """
    Applique une couleur (ajustée en luminosité) à toutes les LEDs.
    :param color: Tuple RGB (par exemple, (50, 0, 0)).
    """
    for i in range(len(np)):
        np[i] = apply_brightness(color)
    np.write()

def apply_brightness(color):
    """Ajuste la luminosité d'une couleur RGB."""
    return tuple(int(c * BRIGHTNESS) for c in color)

def get_BRIGHTNESS():
    return BRIGHTNESS



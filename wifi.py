# Importation des modules nécessaires
import network
import ntptime
import time




# === Configuration Wi-Fi ===
WIFI_SSID = 'T Moch'
WIFI_PASSWORD = 'Pignoufs'




# === Gestion de la connexion Wi-Fi ===
def connect_wifi(ssid, password):
    """
    Connecte l'appareil au réseau Wi-Fi spécifié.
    """
    print("Connexion au réseau Wi-Fi...")
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    
    # Attendre que la connexion soit établie avec un timeout
    timeout = 30  # Limite de temps en secondes
    start_time = time.time()
        
        
    while not wlan.isconnected():
        if time.time() - start_time > timeout:
            print("Impossible de se connecter au Wi-Fi. Vérifiez les informations d'identification.")
            return False
        time.sleep(1)
        print("Connexion en cours...")
    
    print("Connecté au Wi-Fi:")
    print("Adresse IP:", wlan.ifconfig()[0])
    return True




# === Synchronisation de l'heure via NTP ===
def get_wifi_time():
    """
    Récupère l'heure actuelle via NTP et la retourne sous forme d'heures et minutes.
    """
    try:
        print("Synchronisation de l'heure via NTP...")
        ntptime.settime()  # Obtenir l'heure via NTP
        wifi_current_time = time.localtime()  # Récupérer l'heure locale
        wifi_hour = wifi_current_time[3]
        wifi_minute = wifi_current_time[4]
        wifi_seconde = wifi_current_time[5]
        print(f"Heure actuelle : {wifi_hour:02}:{wifi_minute:02}")
        return wifi_hour, wifi_minute, wifi_seconde
    except Exception as e:
        print("Erreur de synchronisation de l'heure NTP:", e)
        return None  # Valeur claire en cas d'erreur






def connect(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if wlan.isconnected():
        return
    else:
        connect_wifi(ssid, password)
        return






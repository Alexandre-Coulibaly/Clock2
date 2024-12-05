import network
import ntptime
import time




# Configuration Wi-Fi
WIFI_SSID = 'T Moch'
WIFI_PASSWORD = 'Pignoufs'




#  Management  of Wi-Fi Connection
def connect_wifi(ssid, password):
    """
    Connects the device to the specified Wi-Fi network.
    """
    print("Network Connection Wi-Fi...")
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    
    # Wait for the connection to be established with a timeout
    timeout = 30  # Time limit in seconds
    start_time = time.time()
        
        
    while not wlan.isconnected():
        if time.time() - start_time > timeout:
            print("Impossible to get connected to the wifi... Verify information.")
            return False
        time.sleep(1)
        print("Try to Connect...")
    
    print("Connected to the Wi-Fi:")
    print("IP Address :", wlan.ifconfig()[0])
    return True




# Time synchronization via NTP
def get_wifi_time():
    """
    Retrieves the current time via NTP and returns it as hours and minutes.
    """
    try:
        print("Time synchronization via NTP...")
        ntptime.settime()  # Get the time via NTP
        wifi_current_time = time.localtime()  # get local time
        wifi_hour = wifi_current_time[3]
        wifi_minute = wifi_current_time[4]
        wifi_seconde = wifi_current_time[5]
        print(f"Current Time : {wifi_hour:02}:{wifi_minute:02}")
        return wifi_hour, wifi_minute, wifi_seconde
    except Exception as e:
        print("NTP Time Sync Error:", e)
        return None 






def connect(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if wlan.isconnected():
        return
    else:
        connect_wifi(ssid, password)
        return

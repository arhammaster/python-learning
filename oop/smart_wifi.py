# Simple Wifi Which allow device internet connectivity 
# 
# The Wifi should have behavior to connect and disconnect
# 
# Wifi should also show max number of connections why show behavior 
# 
# The wifi connection rule is max connection is 3 
#  If more then 3 Device tries to connect it should throw an error 
#    "Max Limit Reached try again when connections is available"

class SmartWifi :

    def __init__(self,name:str):
        self.name:str = name

    wifi_connection_limit:int = 3

    wifi_live_connection:int = 0
    
    def connect (self):
        if SmartWifi.wifi_live_connection < SmartWifi.wifi_connection_limit :
            SmartWifi.wifi_live_connection += 1
            print(f"{self.name} is connected , current users are {SmartWifi.wifi_live_connection}")
        else :
            print(f"{self.name} Max Limit Reached try again when connections is available")

    def disconnect (self):
        SmartWifi.wifi_live_connection -= 1
        print(f"{self.name} is disconnected")
        
    
device1 = SmartWifi ("Device 1")
device2 = SmartWifi ("Device 2")
device3 = SmartWifi ("Device 3")
device4 = SmartWifi ("Device 4")
device5 = SmartWifi ("Device 5")

device1.connect()
device2.connect()
device3.connect()
device4.connect()
device5.connect()

device1.disconnect()

device4.connect()
device5.connect()
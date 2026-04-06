from smart_switch import SmartSwitch

class SmartHome :

    def __init__(self):
        self.switches: list[SmartSwitch] = []

    def add(self, name:str):
        self.switches.append(SmartSwitch(name))
    
    def turn_on_all_switch(self):
        for switch in self.switches:
            switch.on()

        return self.switches

    def turn_off_all_switch(self):
        for switch in self.switches:
            switch.off()

        return self.switches  

    def show_smart_home_all_switches(self) :
        for switch in self.switches:
            print (switch); 
        
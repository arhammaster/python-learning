from device import Device 

class SmartSwitch (Device) :

    def __init__(self, name:str):
        super().__init__(name)
        self.status:bool = False

    def on(self):
        self.status = True
        return self.status
    
    def off(self):
        self.status = False
        return self.status
    
    def __str__(self):
        return f"Smart switch - {self.name} : {self.status}"
    
    def __repr__(self):
        return self.__str__()
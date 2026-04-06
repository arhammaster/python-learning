from smart_home import SmartHome 

class GoogleHome :

    def __init__(self):
        self.home = SmartHome()
        self.home.add("Family Room Switch")
        self.home.add("Kitchen Switch")


    def tun_on_all_switch(self) : 
        self.home.turn_on_all_switch()

    def show(self) : 
        self.home.show_smart_home_all_switches()


okGoogle = GoogleHome()
okGoogle.show()
okGoogle.tun_on_all_switch()
okGoogle.show()
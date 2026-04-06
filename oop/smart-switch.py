class SmartSwitch:
    def __init__(self, state:bool):
        self.state:bool = state

    def turn_on_off(self):
        self.state = not self.state 
        if self.state == False:
            print("Switch is off")
        else:
            print("Switch is on")

# declaring family_room_switch with off state 
family_room_switch = SmartSwitch(False)

# this will on the switch
family_room_switch.turn_on_off()
# the switch is already on so this will off the switch
family_room_switch.turn_on_off()
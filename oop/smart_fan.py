
# Define Smart Fan class 
#
# Smart fan should be on and off
# Smart fan has increase speed behavior that increase speed by 1 
# Smart fan has decrease speed behavior that decrease speed by 1 
#
# Smart fan should has speed
#   Min Speed can be 1
#   Mxx Speed can be 3
#   When Fan On Speed is always 1


class SmartFan :

    def __init__(self) :
        self.state:bool = False
        self.speed:int = 0

    def turn_on_off(self):
        self.state = not self.state 
        if self.state == False:
            print("Switch is off")
        else:
            self.speed = 0
            print(f"Switch is on and Speed is {self.speed}")

    def increase_speed (self) :
        if self.state == True:
            if self.speed < 3 :
                self.speed += 1
            print(f"Fan speed increase to {self.speed}")
        else :
            print("Fan speed can not be increase because fan is off")

    def decrease_speed (self) :
        if self.state == True:
            if self.speed > 1 :
                self.speed -= 1
            print(f"Fan speed decrease to {self.speed}")
        else :
            print("Fan speed can not be decrease because fan is off")

family_room_fan = SmartFan()

#ON
family_room_fan.turn_on_off()

family_room_fan.increase_speed()
family_room_fan.increase_speed()
family_room_fan.increase_speed()
family_room_fan.increase_speed()
family_room_fan.increase_speed()

#OFF
family_room_fan.turn_on_off()
        
family_room_fan.decrease_speed()
family_room_fan.decrease_speed()
family_room_fan.decrease_speed()
family_room_fan.decrease_speed()
family_room_fan.increase_speed()
family_room_fan.increase_speed()
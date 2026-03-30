from person import Person 

class PhoneBook :

    def __init__(self):
        self.persons:list[Person] = []
        self.persons.append(Person("Jack",123455))
        self.persons.append(Person("Jill",345345))

    def search(self, person_name):
        person_name = person_name.title()
        found:bool = False
        for person in self.persons :
            if person.name.title() == person_name :
                 print(f"{person_name} phone number is {person.number}")
                 found = True
        if found is False : 
            print(f"{person_name} does not exist into Phone book")

    def add(self, name:str, number:int) :
        self.persons.append(Person(name, number))

    def update(self, name:str, number:int , new_number:int ) :
        self.persons.remove(name, number)
        self.persons.append(Person(name, new_number))

         

phone_book = PhoneBook ()

print("Test Data")
phone_book.search("Tom")
phone_book.search("jack")

print("After Adding Tom into Phone book")
phone_book.add("Tom", 456456)
phone_book.search("Tom")

print("After Update Tom into Phone book")
phone_book.update("Tom", 456456, 786786)
phone_book.search("Tom")

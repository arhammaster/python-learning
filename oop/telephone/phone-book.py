from person import Person 

class PhoneBook :

    def __init__(self):
        self.persons:list[Person] = []
        self.persons.append(Person("Jack",123455))
        self.persons.append(Person("Jill",345345))

    def search(self,name:str):
        for person in self.persons :
            if person.name.title() == name.title() :
                return person
        return None

    def add(self, name:str, number:int) :
        self.persons.append(Person(name, number))

    def update(self, name:str, new_number:int ) :
        person:Person = self.search(name)
        if person != None :
            self.persons.remove(person)
        self.add(name, new_number)
         

phone_book = PhoneBook ()

print("Test Data")
print(phone_book.search("Tom"))
print(phone_book.search("jack"))

print("After Adding Tom into Phone book")
phone_book.add("Tom", 456456)
print(phone_book.search("Tom"))

print("After Update Tom into Phone book")
phone_book.update("Tom", 786786)
print(phone_book.search("Tom"))



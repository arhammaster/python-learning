class Person :

    def __init__(self, name:str, number:int):
        self.name:str = name
        self.number:int = number

    def __str__(self):
        return f"{self.name} : {self.number}"

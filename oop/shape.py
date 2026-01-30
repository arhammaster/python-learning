class Shape :

    def __init__ (self,name,edges,angels):
        self.name = name
        self.edges = edges
        self.angels = angels
        
    def draw (self):
        print(f"I am a {self.name}")
        print(f"I have {self.edges} edges")
        print(f"I have {self.angels} angels")

triangle = Shape ("Triangle","3","3")
triangle.draw()

square = Shape ("Square","4","4")
square.draw()


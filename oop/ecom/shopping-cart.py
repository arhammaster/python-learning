from product import Product

class ShoppingCart :

    def __init__(self):
        self.products:list[Product] = []

    def add (self, product_add:Product) :
        self.products.append(product_add)
   
    def remove (self, product_remove:str) :
        is_removed:bool = False
        for product in self.products:
            if product.name.lower() == product_remove.lower():
                self.products.remove(product)
                is_removed = True
                print(f"{product.name} is removed from the cart")
        if (is_removed == False) : 
             print(f"{product.name} is not in the cart")

    def view (self) :
        for product in self.products :
            print(f"Name {product.name} Price {product.price} Quantity {product.quantity}")
        
    def check_out (self) :
        total:int = 0
        for product in self.products :
            total += (product.price * product.quantity)
        print(f"you pay ${total}")
    
# test

cart = ShoppingCart ()
cart.add(Product("Milk", 5, 2))
cart.add(Product("Apple", 1, 5))
cart.add(Product("Dragon fruit", 10, 2))
cart.add(Product("Banana", 1, 20))

print("------------------------------")
cart.view()
print("------------------------------")
cart.check_out()
print("------------------------------")
cart.remove("milk")
print("------------------------------")
cart.view()
print("------------------------------")
cart.check_out()
print("------------------------------")

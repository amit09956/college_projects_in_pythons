class item:
    def __init__(self,name,price ,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    def DisplayItem(self):
        print(f'''name-{self.name}"\n
              price-{self.price}\n
              quantity-{self.quantity}''')
class inventory:
    def __init__(self):
        items=[]
    def additems(self,name,newquality):
        for item in self.items:
            if name==item.name:
                print("element is alrady ")
                return
        self.items.append(item(self,name,newquality))
    def update_quality(self,name,changed_quantity):
        if name in self.items:
            pass
        else:
            name.quantity+=changed_quantity
        


       
            
    def displayItems(self):
        pass
inventory1=inventory()
inventory2=inventory()    
inventory1.additems("pen",18,3545)
inventory1.additems("pencil",18,3545)
inventory1.additems("colorPen",18,3545)
inventory1.additems("box",18,3545)



        
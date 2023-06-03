class Item:
    def __init__(self, name, price, available=True):
        self.name = name
        self.price = price
        self.available = available
    def __str__(self):
        availability = "available" if self.available else "Not available"
        return f'{self.name} is {self.price} TRY : [{availability}]'

class Menu:
    def __init__(self):
        self.menu = []
    def add_item(self, item):
        self.menu.append(item)
    def display(self):
        print("The Menu")
        if self.menu:
            for item in self.menu:
                print(item)
        else: print(" no items in the menu")
    def find_item(self, name):
        for item in self.menu:
            if item.name.lower() == name.lower():
                print(name + " is found at our restaurant :)")
                return item
        print(name + " is not found at our restaurant :(")
        return None
    def order_item(self, name):
        item = self.find_item(name)
        if item:
            if item.available == True:
                print("the food is  available, enjoy your meal :)")
                item.available = False
                return item
            else: print("the food is not available :(")
        else: print(" the found is not found in our restaurant!")
        return None
class Restaurant:
    def __init__(self, menu):
        self.menu = menu

class Order:
    def __init__(self, item, status):
        self.item = item
        self.status = status
    def showStatus(self):
        print(self.item.name + " : " + self.status)
    def changeStatus(self, newStatus):
        self.status = newStatus

item1 = Item("Steakhouse", "1250")
item2 = Item("Wooper", "1150")
item3 = Item("BigKing", "1050")

item4 = Item("Italiona Pizza", "1100")
item5 = Item("Classic Pizza", "1000")
item6 = Item("Special Pizza", "1200")

menu1 = Menu()
menu1.add_item(item1)
menu1.add_item(item2)
menu1.add_item(item3)
menu1.display()
menu1.find_item("Wooper")
menu1.find_item("KingChicken")

menu2 = Menu()
menu2.add_item(item4)
menu2.add_item(item5)
menu2.add_item(item6)
menu2.display()
menu2.find_item("Special Pizza")
menu2.find_item("Asdf Pizza")

restaurant1 = Restaurant(menu1)
restaurant2 = Restaurant(menu2)
restaurant1.menu.find_item("BigKing")
restaurant2.menu.find_item("Special Pizza")
restaurant2.menu.order_item("Italiona Pizza")

order1 = Order(restaurant2.menu.order_item("Special Pizza"), "New")
order1.showStatus()
order1.changeStatus("Delivered")
order1.showStatus()


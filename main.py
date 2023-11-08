from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()

print("Welcome to the Coffee Machine!")
print(f"The items available here are: {menu.get_items()}")
stillInMachine = True
while stillInMachine == True:
    item = input(f"Enter the type of drink you would like: ").lower()
    if item == "report":
        coffeeMaker.report()
        moneyMachine.report()
    elif item == "off":
        print("Turning off machine..")
        stillInMachine = False
    else:
        drink = menu.find_drink(item)     # gives output like drink = MenuItem(name=drink, water=200, milk=150, coffee=24, cost=2.5) etc - attributes are defined this way
        if drink != None:
            print(f"You have ordered a {drink.name}")

            if coffeeMaker.is_resource_sufficient(drink) == True:     # returns true or false
                print(f"The {drink.name} costs {drink.cost}$")
                moneyMachine.make_payment(drink.cost)
                coffeeMaker.make_coffee(drink)
        else:
            print("Item does not exist.")
        if input("Would you like to exit machine? If so, press 'n' : ") == 'n':         
            stillInMachine = False

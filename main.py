from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine



# moneyMachine = MoneyMachine()
menu = Menu()
coffeeMaker = CoffeeMaker()


print("Welcome to the Coffee Machine!")
print(f"The items available here are: {menu.get_items()}")
item = input(f"Enter the type of drink you would like: ").lower()

if item == "report":
    coffeeMaker.report()
elif item == "off":
    print("Turning off machine..")
else:
    drink = menu.find_drink(item)
    if drink != None:
        print(f"You have ordered a {drink.name}")

        if coffeeMaker.is_resource_sufficient() == True:
            print(f"The {drink.name} costs {drink.cost}$")

    else:
        print("Item does not exist.")


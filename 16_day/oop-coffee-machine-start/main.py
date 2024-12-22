from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffe_maker = CoffeeMaker()
menu = Menu()

is_on = True

money_machine.report()
coffe_maker.report()

while is_on:
    options = Menu().get_items()
    choise = input(f"what would you like? {options}: ")
    if choise =="off":
        is_on = False
    elif choise == "report":
        coffe_maker.report()
        money_machine.report()
    else: 
        drink = menu.find_drink(choise)
        print(drink)
        

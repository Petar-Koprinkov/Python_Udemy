from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

is_on = True

while is_on:
    drinks = [item for item in menu.get_items().split('/')]
    choice = input(f"What would you like to purchase {menu.get_items()}: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        money_machine.report()
        coffee_machine.report()
    elif choice in drinks:
        drink = menu.find_drink(choice)
        print(f'{drink.cost}{money_machine.CURRENCY}')
        if coffee_machine.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_machine.make_coffee(drink)
    else:
        print(f"Sorry {choice} is not a valid option")

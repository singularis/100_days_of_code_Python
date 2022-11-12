from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()

user_drink = None
while True:
    user_drink = input(f"What would you like? ({menu.get_items()}):")
    if user_drink == "report":
        coffee_machine.report()
        money_machine.report()
    elif user_drink == "off":
        print("Powering off")
        break
    else:
        menu_item = menu.find_drink(user_drink)
        if menu_item:
            if coffee_machine.is_resource_sufficient(menu_item) and money_machine.make_payment(menu_item.cost):
                coffee_machine.make_coffee(menu_item)
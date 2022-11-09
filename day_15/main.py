from data import MENU, resources as resources_init


def clear():
    lambda: print("")


def report(resources, money):
    print(resources)
    print("There is next resources left: \nWater: {}ml \nMilk: {}ml \nCoffee: {}g \nMoney: ${}"
          .format(resources["water"], resources["milk"], resources["coffee"], money))


def resources_checker(coffee_type, resources):
    for resource in resources:
        if resources.get(resource) < MENU.get(coffee_type).get("ingredients").get(resource):
            print("Sorry there is not enough {}.".format(resource))
            return False
    clear()
    return True


def coffee_maker(coffee_type, resources):
    for resource in resources:
        resources[resource] = (resources.get(resource) - MENU.get(coffee_type).get("ingredients").get(resource))
    return resources


def money_counter(coffee_type, resources):
    money = 0
    while money < MENU.get(coffee_type).get("cost"):
        quarters = int(input("how many quarters?: "))
        dimes = int(input("how many dimes?: "))
        nickles = int(input("how many nickles?: "))
        pennies = int(input("how many pennies?: "))
        money = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies
        if money < MENU.get(coffee_type).get("cost"):
            low_money = input("Sorry that's not enough money. Please add more. Or type 'exit to get refunded'")
            if low_money == "exit":
                print("Sorry that's not enough money. Money refunded.")
                break
    if money > MENU.get(coffee_type).get("cost"):
        print("Here is ${} dollars in change and cocking your {}".format((money - MENU.get(coffee_type).get("cost")),
                                                                         coffee_type))
        coffee_maker(coffee_type, resources)
    else:
        print("Cocking your drink {}".format(coffee_type))
        coffee_maker(coffee_type, resources)
    clear()
    return MENU.get(coffee_type).get("cost")


def machine_main(resources):
    money = 0
    coffee_type = None
    while coffee_type != "off":
        coffee_type = input("What would you like? (espresso/latte/cappuccino): ")
        if coffee_type == "report":
            report(resources, money)
        if coffee_type in MENU:
            if resources_checker(coffee_type, resources):
                print("Please insert coins.")
                money += money_counter(coffee_type, resources)


if __name__ == '__main__':
    machine_main(resources_init)
    print("Bye-Bye")
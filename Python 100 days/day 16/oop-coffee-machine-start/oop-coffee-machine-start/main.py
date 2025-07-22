from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine=MoneyMachine()
coffee_maker=CoffeeMaker()
menu=Menu()

# menu_item=MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5)






# MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
id_on=True

while id_on:

    options=menu.get_items()
    choose=input(f'plese select coffee {options}')

    if choose=="off":
        id_on = False
    elif choose=='report':
        print(money_machine.report())
        print(coffee_maker.report())

    else:
        items=menu.find_drink(choose)
        print(items)
        if coffee_maker.is_resource_sufficient(items) and money_machine.make_payment(items.cost):
                coffee_maker.make_coffee(items)
        else:
            print('resource not available')

        id_on=False
import menu
from menu import Menu
from menu import MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

should_start = True
menu_instance = Menu()
coffe_obj=CoffeeMaker()
money_machine=MoneyMachine()
def askuser():
    user = input(
        "Do you want to start the machine?\nDo you want to stop the machine?\nDo you want to see the menu?"
        "\n do ypou want a report?\n Do you want profit?\nstart/stop/menu/report/profit :").lower()
    if user == "start":
        print("WELCOME TO COFFEE MACHINE!")
        print("__________________________")
        should_start = True
    elif user == "stop":
        print("COFFEE MACHINE SWITCHED OFF!")
        should_start = False
    elif user == "menu":
        print("Available drinks:", menu_instance.get_items())
        askuser()
    elif user == "report":
        coffe_obj.report()
        askuser()
    elif user == "profit":
        money_machine.report()
        askuser()
    else:
        print("invalid entry")
        askuser()
def order():
    drink = input("what you want to drink? latte/espresso/cappuccino/").lower()
    if drink == "latte" or drink == "espresso" or drink == "cappuccino":
        juice = menu_instance.find_drink(drink)
        print(f"DRINK NAME : {juice.name}\nDRINK COST : {juice.cost}\nDRINK INGREDIENTS: {juice.ingredients}")
        if coffe_obj.is_resource_sufficient(juice):
            if money_machine.make_payment(juice.cost):
                coffe_obj.make_coffee(juice)
        again = input("want to order again?y/n: ").lower()
        if again == "y":
            order()
        else:
            print("THANKYOU")
            should_start == False

    else:
        print("invalid entry!")
        again = input("want to order again?y/n: ").lower()
        if again == "y":
            order()
        else:
            print("THANKYOU")
            should_start == False


askuser()
while should_start==True:
    order()









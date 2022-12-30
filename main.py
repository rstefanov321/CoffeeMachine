
from menu import MENU as coffees
from menu import resources

machine_on = True
treasury = 0


def calculate_inserted_coins(item):
    print("Please insert coins: ")
    pennies = int(input("How many pennies: ")) * 0.01
    dimes = int(input("How many dimes: ")) * 0.05
    nickels = int(input("How many nickels: ")) * 0.10
    quarters = int(input("How many quarters: ")) * 0.25
    total = pennies + dimes + nickels + quarters
    if total > coffees[item]["cost"]:
        change = total - coffees[chosen_coffee]["cost"]
        print(f"Here is your change: {round(change, 2)}")
        print(f"Here is your {item}. Enjoy!")
    else:
        print("Sorry not enough coins, add some more. Returning current coins...")
        total = 0
        calculate_inserted_coins(item)


while machine_on:
    
    chosen_coffee = input("What would you like? (espresso/latte/cappuccino): ")
    items_list = ["espresso", "latte", "cappuccino"]

    if chosen_coffee == "report":
        print(f"Water : {resources['water']}ml")
        print(f"Milk : {resources['milk']}ml")
        print(f"Coffee : {resources['coffee']}")
        print(f"Money :{treasury}")

    elif chosen_coffee == "espresso":
        if resources["water"] >= coffees["espresso"]["ingredients"]["water"] and resources["coffee"] >= coffees["espresso"]["ingredients"]["coffee"]:
            resources["water"] -= coffees["espresso"]["ingredients"]["water"]
            resources["coffee"] -= coffees["espresso"]["ingredients"]["coffee"]
            treasury += coffees["espresso"]["cost"]
            calculate_inserted_coins(chosen_coffee)

        elif resources["water"] < coffees["espresso"]["ingredients"]["water"]:
            print(f"Sorry, not enough water.")

        elif resources["coffee"] < coffees["espresso"]["ingredients"]["coffee"]:
            print(f"Sorry, not enough coffee.")

    elif chosen_coffee == "latte":
        if (resources["water"] >= coffees["latte"]["ingredients"]["water"] and
                resources["coffee"] >= coffees["latte"]["ingredients"]["coffee"] and
                resources["milk"] >= coffees["latte"]["ingredients"]["milk"]):

            resources["water"] -= coffees["latte"]["ingredients"]["water"]
            resources["coffee"] -= coffees["latte"]["ingredients"]["coffee"]
            resources["milk"] -= coffees["latte"]["ingredients"]["milk"]
            treasury += coffees["latte"]["cost"]
            calculate_inserted_coins(chosen_coffee)

        elif resources["water"] < coffees["latte"]["ingredients"]["water"]:
            print(f"Sorry, not enough water.")

        elif resources["coffee"] < coffees["latte"]["ingredients"]["coffee"]:
            print(f"Sorry, not enough coffee.")

        elif resources["milk"] < coffees["latte"]["ingredients"]["milk"]:
            print(f"Sorry, not enough milk.")

    elif chosen_coffee == "cappuccino":
        if (resources["water"] >= coffees["cappuccino"]["ingredients"]["water"] and
                resources["coffee"] >= coffees["cappuccino"]["ingredients"]["coffee"] and
                resources["milk"] >= coffees["cappuccino"]["ingredients"]["milk"]):
            resources["water"] -= coffees["cappuccino"]["ingredients"]["water"]
            resources["coffee"] -= coffees["cappuccino"]["ingredients"]["coffee"]
            resources["milk"] -= coffees["cappuccino"]["ingredients"]["milk"]
            treasury += coffees["cappuccino"]["cost"]
            calculate_inserted_coins(chosen_coffee)

        elif resources["water"] < coffees["cappuccino"]["ingredients"]["water"]:
            print(f"Sorry, not enough water.")

        elif resources["coffee"] < coffees["cappuccino"]["ingredients"]["coffee"]:
            print(f"Sorry, not enough coffee.")

        elif resources["milk"] < coffees["cappuccino"]["ingredients"]["milk"]:
            print(f"Sorry, not enough milk.")

    elif chosen_coffee == "off":
        print("Thank you, goodbye!")
        machine_on = False

    else:
        print("Please enter a valid option! Thank you!")

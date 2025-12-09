import sys

class CoffeeMachine:
    pass


def print_state(w, m, beans, cups, cash):
    print("The coffee machine has:")
    print(f"{w} ml of water")
    print(f"{m} ml of milk")
    print(f"{beans} g of coffee beans")
    print(f"{cups} disposable cups")
    print(f"${cash} of money")
    print()

def check(choice, w, m, beans, cups):
    if choice == "1":  # espresso
        if w < 250:
            return "water"
        if beans < 16:
            return "coffee beans"
        if cups < 1:
            return "cups"
    elif choice == "2":  # latte
        if w < 350:
            return "water"
        if m < 75:
            return "milk"
        if beans < 20:
            return "coffee beans"
        if cups < 1:
            return "cups"
    elif choice == "3":  # cappuccino
        if w < 200:
            return "water"
        if m < 100:
            return "milk"
        if beans < 12:
            return "coffee beans"
        if cups < 1:
            return "cups"
    return None

def buy(w, m, beans, cups, cash):
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    choice = input().strip()
    if choice == "back":
        return w, m, beans, cups, cash

    missing = check(choice, w, m, beans, cups)
    if missing:
        print(f"Sorry, not enough {missing}!\n")
        return w, m, beans, cups, cash

    if choice == "1":
        w -= 250; beans -= 16; cups -= 1; cash += 4
    elif choice == "2":
        w -= 350; m -= 75; beans -= 20; cups -= 1; cash += 7
    elif choice == "3":
        w -= 200; m -= 100; beans -= 12; cups -= 1; cash += 6

    print("I have enough resources, making you a coffee!\n")
    return w, m, beans, cups, cash

def fill(w, m, beans, cups, cash):
    print("Write how many ml of water you want to add:")
    w += int(input())
    print("Write how many ml of milk you want to add:")
    m += int(input())
    print("Write how many grams of coffee beans you want to add:")
    beans += int(input())
    print("Write how many disposable cups you want to add:")
    cups += int(input())
    return w, m, beans, cups, cash

def take(w, m, beans, cups, cash):
    print(f"I gave you ${cash}\n")
    cash = 0
    return w, m, beans, cups, cash

def main():
    water = 400
    milk = 540
    coffee_beans = 120
    disposable_cups = 9
    cash = 550

    while True:
        print("Write action (buy, fill, take, remaining, exit):")
        action = input().strip()
        if action == "buy":
            water, milk, coffee_beans, disposable_cups, cash = buy(
                water, milk, coffee_beans, disposable_cups, cash
            )
        elif action == "fill":
            water, milk, coffee_beans, disposable_cups, cash = fill(
                water, milk, coffee_beans, disposable_cups, cash
            )
        elif action == "take":
            water, milk, coffee_beans, disposable_cups, cash = take(
                water, milk, coffee_beans, disposable_cups, cash
            )
        elif action == "remaining":
            print_state(water, milk, coffee_beans, disposable_cups, cash)
        elif action == "exit":
            sys.exit()
        else:
            print("command not found\n")

if __name__ == "__main__":
    main()

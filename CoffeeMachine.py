class CoffeeMachine:

    def __init__(self, water=0, milk=0, beans=0, cups=0, money=0):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money

    def __str__(self):
        return f"""The coffee machine has:
        {self.water} of water
        {self.milk} of milk
        {self.beans} of coffee beans
        {self.cups} of disposable cups
        {self.money} of money"""

    resources = ['water', 'milk', 'beans', 'cups', 'money']

    espresso = [250, 0, 16, 1, 4]
    latte = [350, 75, 20, 1, 7]
    cappuccino = [200, 100, 12, 1, 6]

    def check_resources(self, coffee_type):
        if self.water >= coffee_type[0] and\
        self.milk >= coffee_type[1] and\
        self.beans >= coffee_type[2] and\
        self.cups >= coffee_type[3]:
            return 'True'
        elif self.water < coffee_type[0]:
            return 0
        elif self.milk < coffee_type[1]:
            return 1
        elif self.beans < coffee_type[2]:
            return 2
        elif self.cups < coffee_type[3]:
            return 3

    def take_resources(self, coffee_type):
        self.water -= coffee_type[0]
        self.milk -= coffee_type[1]
        self.beans -= coffee_type[2]
        self.cups -= coffee_type[3]
        self.money += coffee_type[4]


MyMachine = CoffeeMachine(400, 540, 120, 9, 550)
action = ''

while action != 'exit':
    print("Write action (buy, fill, take, remaining, exit) :")
    action = input()
    if action == 'buy':
        print("What do you want to buy) 1 - espresso, 2 - latte, 3 - cappuccino:")
        coffee_type = input()
        if coffee_type == 'back':
            continue
        elif coffee_type == '1':
            if MyMachine.check_resources(MyMachine.espresso) == 'True':
                print("I have enough resources, making you a coffee!")
                MyMachine.take_resources(MyMachine.espresso)
            else:
                print(f"Sorry, not enough {MyMachine.resources[MyMachine.check_resources(MyMachine.espresso)]}")
        elif coffee_type == '2':
            if MyMachine.check_resources(MyMachine.latte) == 'True':
                print("I have enough resources, making you a coffee!")
                MyMachine.take_resources(MyMachine.latte)
            else:
                print(f"Sorry, not enough {MyMachine.resources[MyMachine.check_resources(MyMachine.latte)]}")
        elif coffee_type == '3':
            if MyMachine.check_resources(MyMachine.cappuccino) == 'True':
                print("I have enough resources, making you a coffee!")
                MyMachine.take_resources(MyMachine.cappuccino)
            else:
                print(f"Sorry, not enough {MyMachine.resources[MyMachine.check_resources(MyMachine.cappuccino)]}")
    elif action == 'fill':
        print("Write how many ml of water do you want to add:")
        MyMachine.water += int(input())
        print("Write how many ml of milk do you want to add:")
        MyMachine.milk += int(input())
        print("Write how many grams of coffee beans do you want to add:")
        MyMachine.beans += int(input())
        print("Write how many disposable cups of coffee do you want to add:")
        MyMachine.cups += int(input())
    elif action == 'take':
        print(f"I gave you ${MyMachine.money}")
        MyMachine.money = 0
    elif action == 'remaining':
        print()
        print(MyMachine)

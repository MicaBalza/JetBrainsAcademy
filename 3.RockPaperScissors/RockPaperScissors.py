import random


class RPS:

    def __init__(self):
        self.options = []
        self.new_options = []
        self.user_hand = ''
        self.computer_hand = None
        self.ch_i = 0
        self.user_name = None
        self.ratings = None
        self.ratings_dict = {}
        self.user_rating = 0

    def user_choice(self):
        self.new_options = self.options[(self.options.index(self.user_hand) + 1):]
        self.new_options.extend(self.options[:self.options.index(self.user_hand)])

    def computer_choice(self):
        self.computer_hand = random.choice(self.options)

    def check_ratings(self):
        self.ratings = open('rating.txt', 'r')
        self.ratings_dict = {k: v for k, v in [line.split() for line in self.ratings.readlines()]}
        if self.user_name in self.ratings_dict.keys():
            self.user_rating = int(self.ratings_dict[self.user_name])
        else:
            self.user_rating = 0


myGame = RPS()
print("Enter your name: ", end='')
myGame.user_name = input()
print(f"Hello, {myGame.user_name}")
myGame.check_ratings()
myGame.options = input().split(',')
if myGame.options == ['']:
    myGame.options = ['rock', 'paper', 'scissors']
print("Okay, let's start")

while myGame.user_hand != '!exit':
    myGame.user_hand = input()
    myGame.computer_choice()
    if myGame.user_hand == '!rating':
        print("Your rating:", myGame.user_rating)
    elif myGame.user_hand in myGame.options:
        myGame.user_choice()
        if myGame.computer_hand == myGame.user_hand:
            print(f"There is a draw ({myGame.computer_hand})")
            myGame.user_rating += 50
        elif myGame.computer_hand in myGame.new_options[:len(myGame.new_options) // 2]:
            print(f"Sorry, but computer chose {myGame.computer_hand}")
        elif myGame.computer_hand in myGame.options[len(myGame.new_options) // 2:]:
            print(f"Well done. Computer chose {myGame.computer_hand} and failed")
            myGame.user_rating += 100
    elif myGame.user_hand == '!exit':
        break
    else:
        print("Invalid input")
print("Bye!")

import random
choices = ["rock","paper","scissors"]
computer = random.choice(choices)
print('Welcome to Rock-Paper-Scissors game :)')
user = input("rock or paper or scissors ? ")
if user in choices:
    def winner(x,y):
        if x == "paper" and y == "rock" or x == 'rock' and y == 'scissors' or x == 'scissors' and y == 'paper':
                return f"\nUser is Win\nuser : {x}\nComputer : {y}\n"
        elif y == "paper" and x == "rock" or y == 'rock' and x == 'scissors' or y == 'scissors' and x == 'paper':
                return f'\nComputer is Win\ncomputer : {y}\nUser : {x}\n'
        else:
                print('Computer and User are same ! Do again :)')
                computer = random.choice(choices)
                user = input("rock or paper or scissors ? ")
                return winner(user,computer)
    print(winner(user,computer))
else:
    print('You are type wrong ! do again :)')


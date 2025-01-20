import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]
#user pick
user_pick=int(input("Pick 0 for Rock, 1 for Paper, and 2 for Scissor.\n"))

if user_pick >= 0 and user_pick <= 2:
    print(game_images[user_pick])

#computer pick
comp_pick=random.randint(0,2)
print("Computer chose:")
print(game_images[comp_pick])

if user_pick >= 3 or user_pick < 0:
    print("You typed an invalid number. You lose!")
elif user_pick == 0 and comp_pick == 2:
    print("You win!")
elif comp_pick == 0 and user_pick == 2:
    print("You lose!")
elif comp_pick > user_pick:
    print("You lose!")
elif user_pick > comp_pick:
    print("You win!")
elif comp_pick == user_pick:
    print("It's a draw!")0
    
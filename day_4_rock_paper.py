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
'''
From there you will need to figure out: 
* How you will store the user's input.
* How you will generate a random choice for the computer.
* How you will compare the user's and the computer's choice to determine the winner (or a draw).
* And also how you will give feedback to the player.  
'''


#Write your code below this line 👇
shoot = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
if shoot == 0:
  shoot = rock
if shoot == 1:
  shoot = paper
if shoot == 2:
  shoot = scissors
print(shoot)

comp_turn =  random.randint(1,3)

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
'''
From there you will need to figure out: 
* How you will store the user's input.
* How you will generate a random choice for the computer.
* How you will compare the user's and the computer's choice to determine the winner (or a draw).
* And also how you will give feedback to the player.  
'''


#Write your code below this line 👇
shoot = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if shoot == 0:
  shoot = rock
if shoot == 1:
  shoot = paper
if shoot == 2:
  shoot = scissors
print(f'User enters {shoot}')

comp_turn = random.randint(0,2)
if comp_turn == 0:
  comp_turn = rock
if comp_turn == 1:
  comp_turn = paper
if comp_turn == 2:
  comp_turn = scissors
print(f'Computer chooses {comp_turn}')

if shoot == rock and comp_turn == scissors:
  print('Rock wins!')
if shoot == rock and comp_turn == paper:
  print('Paper wins!')
if shoot == scissors and comp_turn == paper: 
  print('Scisssors win!')
if shoot == scissors and comp_turn == rock:
  print('Rock wins!')
if shoot == paper and comp_turn == rock:
  print('Paper is the winner!')
if shoot == paper and comp_turn ==scissors:
  print('Scissors is the winner!')

if shoot == comp_turn:
  print('It is a tie! Try again.')
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
game_pics = [rock,paper,scissors]
shoot = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n")) 
if shoot >=3 or shoot <0:
  print('You entered an invalid number, you lose!')
elif shoot < 3 and shoot >= 0:
  print(game_pics[shoot])

  comp_turn = random.randint(0,2)
  print(f'Computer chooses {comp_turn}')
  print(game_pics[comp_turn])

  if shoot == 0 and comp_turn == 2:
      print('You win!')
  elif comp_turn == 0 and shoot ==2:
    print('You lose')
  elif comp_turn > shoot:
    print('You lose')
  elif shoot > comp_turn:
    print('You win!')
  elif shoot == comp_turn:
    print('It is a tie! Try again.')

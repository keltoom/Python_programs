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

#*****************************************
choise=int(input('what do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors\n'))
if choise==0:
    print(rock)
elif choise==1:
    print(paper)
elif choise==2:
    print(scissors)
else:
    print('wrong input')
#****************************************
computer_choise=random.randint(0,2)

print('computer choise:\n')
if computer_choise==0:
    print(rock)
elif computer_choise==1:
    print(paper)
elif computer_choise==2:
    print(scissors)



if choise==computer_choise:
    print('draw')
elif choise==0 and computer_choise==1 or choise==1 and computer_choise==2 or choise==2 and computer_choise==0:
    print('you lose')
elif choise==0 and computer_choise==2 or choise==1 and computer_choise==0 or choise==2 and computer_choise==1:
    print('you win!')


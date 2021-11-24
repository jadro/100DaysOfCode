import random

rock_paper_scissors = ["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]

selection = int(input("Select 0 for 'Rock', 1 for 'Paper' or 2 for 'Scissors' "))
computer = random.randint(0,2)

try:
    print(f"You selected\n{rock_paper_scissors[selection]}")
    print(f"Computer selected\n{rock_paper_scissors[computer]}")

    if selection == 2 and computer == 0:
        print ("You won.")
    elif selection < computer:
        print("You lose.")
    elif selection == computer:
        print("It's a draw.")
    else:
        print("You won.")

except IndexError:
    print("You selected wrong number. Game will end.")


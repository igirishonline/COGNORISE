import random
choices=("rock","paper","scissors")

running=True

while running:
  player=None
  computer=random.choice(choices)
  while player not in choices:
    player=input("enter a choice (rock,paper,scissors): ")

  print(f"player={player}")
  print(f"computer={computer}")

  if (player==computer):
    print("its a tie!")
  elif (player=='rock'and computer=='scissors'):
    print("player wins!")
  elif (player=='paper'and computer=='rock'):
    print("player wins!")
  elif (player=='scissors'and computer=='paper'):
    print("player wins!")
  else:
    print("computer wins!")

  if not input("play again..? (y/n)").lower()=='y':s
    running=False

print("Thanks for playing the game...!")

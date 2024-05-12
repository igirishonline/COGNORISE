
import random

# here i have used unicode character using the following below codes-->
print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

#● ┌ ─ ┐ │ └ ┘

"┌─────────┐"
"│         │"
"│         │"
"│         │"
"└─────────┘"

dice_roll = {
    1 :("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2 :("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3 :("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4 :("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5 :("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6 :("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

dice=[]
total=0
no_of_dice=int(input("enter how many dice..?:  "))
for die in range(no_of_dice):
  dice.append(random.randint(1,6))
for die in range(no_of_dice):
  for line in dice_roll.get(dice[die]):
    print(line)
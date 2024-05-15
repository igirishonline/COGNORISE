import random

print("welcome to hangman game")
print("------------------------")

word_dict=["sunflower","cricket","diamond","hero","badminton","chess","memes","college"]

random_word=random.choice(word_dict)

for a in random_word:
  print(" ",end="")

def print_hangman(wrong):
  if (wrong==0):
    print("\n+---+")
    print("    |")
    print("    |")
    print("    |")
    print("    |")
    print("   ===")
  elif (wrong==1):
    print("\n+---+")
    print("O   |")
    print("    |")
    print("    |")
    print("   ===")
  elif (wrong==2):
    print("\n+---+")
    print("O   |")
    print("|   |")
    print("    |")
    print("    |")
    print("   ===")
  elif (wrong==3):
    print("\n+---+")
    print(" O  |")
    print("/|  |")
    print("    |")
    print("   ===")
  elif (wrong==4):
    print("\n+---+")
    print(" O  |")
    print("/|\ |")
    print("    |")
    print("   ===")
  elif (wrong==5):
    print("\n+---+")
    print(" O  |")
    print("/|\ |")
    print("/   |")
    print("   ===")
  elif(wrong==6):
    print("\n+---+")
    print(" O  |")
    print("/|\ |")
    print("/ \ |")
    print("   ===")

def printword(guessed_letters):
  counter=0
  rightletters=0
  for char in random_word:
    if(char in guessed_letters):
      print(random_word[counter],end=" ")
      rightletters+=1
    else:
      print(" ",end=" ")
    counter+=1
  return rightletters

def printlines():
  print("\r")
  for char in random_word:
    print("\u203E",end=" ")
word_length_to_guess=len(random_word)
times_of_wrong_guess=0
current_guess_index=0
current_letters_guessed=[]
current_letters_right=0

while(times_of_wrong_guess != 6 and current_letters_right != word_length_to_guess):
  print("\nletters guessed so far: ")
  for letter in current_letters_guessed:
    print(letter,end=" ")
  ### prompt user for input
  letterguessed=input("\nguess a letter: ")
  ### user is right
  if(random_word[current_guess_index]== letterguessed):
    print_hangman(times_of_wrong_guess)
    ### print word
    current_guess_index+=1
    current_letters_guessed.append(letterguessed)
    current_letters_right=printword(current_letters_guessed)
    printlines()
  ### user was wrong
  else:
    times_of_wrong_guess+=1
    current_letters_guessed.append(letterguessed)
    ### update the drawing
    print_hangman(times_of_wrong_guess)
    ### print word
    current_letters_right=printword(current_letters_guessed)
    printlines()

print("game is over thanks for playing...:)")
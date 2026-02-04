from random import randint
guesses = 0
number = randint(1,10)
print("Guess a number between 1 and 10")
guess = int(input())
while guess != number and guesses < 2:
  print("Incorrect")
  guesses += 1
  print(guesses)
  if guess > number:
    print("Lower btw")
  elif guess < number:
    print("Higher btw")
  print("Guess a number between 1 and 10")
  guess = int(input())
if guess == number:
  guesses += 1
  print("Correct")
  if guesses != 1:
    print(f"You got it in {guesses} guesses")
  else:
    print(f"You got it in 1 guess")
else:
  print("You failed")
  print(f"The number is actualy {number}")
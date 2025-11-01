import random
import time

print("Generating number . . .")
time.sleep(0.2)
sol = random.randint(1, 100)
print("Random number has been generated.")
time.sleep(0.2)

guesses_remaining = 7
solved = False
while guesses_remaining > 0:
    if solved: 
        break

    guess = input("You have {} guesses left. What is your guess? ".format(guesses_remaining))
    
    try:
        guess = int(guess)
    except:
        print("That was not an integer. Please type an integer")
        continue

    if guess < 1 or guess > 100:
        print("That number was not between 1 and 100. Please make a reasonable guess.")
        continue

    if guess == sol:
        solved = True
        continue
    elif guess < sol:
        print("The solution is higher than that!")
    elif guess > sol:
        print("The solution is lower than that!")

    guesses_remaining -= 1

if solved:
    print("Congrats on solving it. You had {} guesses left!".format(guesses_remaining))
else:
    print("Better luck next time, you ran out of guesses. The solution was {}".format(sol))
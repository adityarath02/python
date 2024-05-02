# ### create a guessing game where the user has to guess a randomly generated number.Use branching, looping, and flow control statements to manage the game's flow
import random
import math
x = int(input("Enter the lower bound: "))
y = int(input("Enter the upper bound: "))
n = random.randint(x,y)
guess = None
attempts = 0
max_attempts = math.log(y-x,2)
print(f"You have {max_attempts} attempts to guess the number.")

while guess != n and attempts < max_attempts:
    guess = int(input(f"Enter your guess between {y} and {x} : "))
    attempts += 1
    if guess < n:
        print("Too low! Try again.")
    elif guess > n:
        print("Too high! Try again.")

if guess == n:
    print(f"Congratulations! You found the number in {attempts} attempts.")
else:
    print(f"Sorry, you didn't guess the number within {max_attempts} attempts. The number was.",n)
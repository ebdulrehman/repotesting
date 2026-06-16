import random

# The computer selects a random number between 1 and 20
secret_number = random.randint(1, 20)

print("I am thinking of a number between 1 and 20.")

# Loop until the player guesses correctly
while True:
    # Get user input and convert it to an integer
    guess = int(input("Take a guess: "))
    
    if guess == secret_number:
        print("Good job! You guessed my number!")
        break  # Exit the loop
    elif guess < secret_number:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")

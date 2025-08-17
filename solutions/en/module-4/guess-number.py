import random

secret = random.randint(1, 10)

for attempt in range(3):
    guess = int(input("Guess a number (1–10): "))
    if guess == secret:
        print("Correct! 🎉")
        break
    elif guess < secret:
        print("Too small!")
    else:
        print("Too big!")
else:
    print("Sorry, the number was", secret)

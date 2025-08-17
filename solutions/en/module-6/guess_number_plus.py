import random

wins = 0
losses = 0

while True:
    level = input("Level (easy/normal/hard): ").strip().lower()
    top = {"easy": 10, "normal": 20, "hard": 50}.get(level, 10)
    secret = random.randint(1, top)
    attempts = 5

    while attempts:
        try:
            guess = int(input(f"Guess (1–{top}), attempts {attempts}: "))
        except ValueError:
            print("Please enter a number.")
            continue

        if guess == secret:
            print("You win! 🎉")
            wins += 1
            break
        print("Too small!" if guess < secret else "Too big!")
        attempts -= 1
    else:
        print("You lose. The number was", secret)
        losses += 1

    again = input("Play again? (y/n): ").strip().lower()
    if again != "y":
        print("Wins:", wins, "Losses:", losses)
        break

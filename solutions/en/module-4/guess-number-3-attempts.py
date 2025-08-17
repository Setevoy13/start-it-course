import random
secret = random.randint(1, 20)  # adjustable range
attempts = 3
for _ in range(attempts):
    guess = int(input("Guess (1–20): "))
    if guess == secret:
        print("Correct! 🎉")
        break
    print("Too small!" if guess < secret else "Too big!")
else:
    print("Out of attempts. The number was", secret)

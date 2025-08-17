import random

secret = random.randint(1, 10)

for attempt in range(3):
    guess = int(input("Угадай число (1–10): "))
    if guess == secret:
        print("Верно! 🎉")
        break
    elif guess < secret:
        print("Слишком мало!")
    else:
        print("Слишком много!")
else:
    print("К сожалению, число было", secret)

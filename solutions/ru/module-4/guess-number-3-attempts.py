import random
secret = random.randint(1, 20)  # настраиваемый диапазон
attempts = 3
for _ in range(attempts):
    guess = int(input("Угадай (1–20): "))
    if guess == secret:
        print("Верно! 🎉")
        break
    print("Слишком мало!" if guess < secret else "Слишком много!")
else:
    print("Попытки закончились. Число было", secret)

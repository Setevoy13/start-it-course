import random

wins = 0
losses = 0

while True:
    level = input("Сложность (easy/normal/hard): ").strip().lower()
    top = {"easy": 10, "normal": 20, "hard": 50}.get(level, 10)
    secret = random.randint(1, top)
    attempts = 5

    while attempts:
        try:
            guess = int(input(f"Угадай (1–{top}), попыток {attempts}: "))
        except ValueError:
            print("Нужно ввести число.")
            continue

        if guess == secret:
            print("Победа! 🎉")
            wins += 1
            break
        print("Слишком мало!" if guess < secret else "Слишком много!")
        attempts -= 1
    else:
        print("Поражение. Число было", secret)
        losses += 1

    again = input("Сыграть ещё? (y/n): ").strip().lower()
    if again != "y":
        print("Побед:", wins, "Поражений:", losses)
        break

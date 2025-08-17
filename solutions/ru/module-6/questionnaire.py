profile = {}
profile["name"] = input("Имя: ")
profile["age"] = input("Возраст: ")
profile["city"] = input("Город: ")
profile["hobby"] = input("Хобби: ")
with open("profile.txt", "w", encoding="utf-8") as f:
    for k, v in profile.items():
        f.write(f"{k}: {v}\n")
print("Сохранено в profile.txt")

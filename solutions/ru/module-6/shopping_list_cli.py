items = []

while True:
    print("\n1) Добавить  2) Удалить  3) Показать  4) Сохранить  0) Выход")
    choice = input("Выбери: ").strip()
    if choice == "1":
        item = input("Что добавить: ").strip()
        if item:
            items.append(item)
    elif choice == "2":
        name = input("Что удалить: ").strip()
        if name in items:
            items.remove(name)
        else:
            print("Не найдено")
    elif choice == "3":
        print("\nТвой список:")
        for i, it in enumerate(items, start=1):
            print(f"{i}. {it}")
    elif choice == "4":
        with open("shopping.txt", "w", encoding="utf-8") as f:
            for it in items:
                f.write(it + "\n")
        print("Сохранено в shopping.txt")
    elif choice == "0":
        print("Пока!")
        break
    else:
        print("Неизвестный пункт — попробуй снова.")

items = []

while True:
    print("\n1) Add  2) Remove  3) Show  4) Save  0) Exit")
    choice = input("Choose: ").strip()
    if choice == "1":
        item = input("Item to add: ").strip()
        if item:
            items.append(item)
    elif choice == "2":
        name = input("Item to remove: ").strip()
        if name in items:
            items.remove(name)
        else:
            print("Not found")
    elif choice == "3":
        print("\nYour list:")
        for i, it in enumerate(items, start=1):
            print(f"{i}. {it}")
    elif choice == "4":
        with open("shopping.txt", "w", encoding="utf-8") as f:
            for it in items:
                f.write(it + "\n")
        print("Saved to shopping.txt")
    elif choice == "0":
        print("Bye!")
        break
    else:
        print("Unknown choice — try again.")

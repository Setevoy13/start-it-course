items = []
for _ in range(5):
    items.append(input("Товар: "))
for it in sorted(items):
    print("-", it)

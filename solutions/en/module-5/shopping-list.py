items = []
for _ in range(5):
    items.append(input("Item: "))
for it in sorted(items):
    print("-", it)

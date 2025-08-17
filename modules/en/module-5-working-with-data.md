# Module 5. Working with Data 📊

**Goal:** learn to group and structure information using **lists** and **dictionaries**.

---

## 📋 Lists
Create, access, update:
```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])       # apple
fruits.append("orange")  # add
fruits[1] = "pear"       # update
print(len(fruits))       # length
```
Looping:
```python
for item in fruits:
    print("-", item)
```

**Task 1:** create a list `movies` with 5 titles; print them one per line.

---

## 📖 Dictionaries
Key → value storage:
```python
person = {"name": "Alice", "age": 25, "city": "NY"}
print(person["name"])
person["email"] = "alice@example.com"  # add
person["age"] = 26                     # update
```
Looping:
```python
for key, value in person.items():
    print(key, "→", value)
```

**Task 2:** create `me` with keys `name`, `age`, `country`; print each pair.

---

## 🧮 Simple aggregations
```python
numbers = [3, 5, 7, 9]
print("sum:", sum(numbers))
print("min:", min(numbers), "max:", max(numbers))
print("avg:", sum(numbers)/len(numbers))
```

**Task 3:** ask the user for 5 numbers, store in a list, print the average.

---

## 🛒 Mini‑project: Shopping List
Requirements:
1. Ask the user to enter 5 items (use a loop).
2. Store them in a list.
3. Print them nicely (one per line).

Bonus ideas:
- Let the user **remove** an item by name.
- Sort the list alphabetically.

👉 Next: [Module 6. Mini‑Projects](module-6-mini-projects.md)

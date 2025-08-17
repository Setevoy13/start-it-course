# Module 3. Introduction to Python 🐍

**Goal:** run your first programs, understand `print`, variables, and input.

---

## 🔧 Install & Check
- Download from [python.org/downloads](https://www.python.org/downloads/).
- During install: **check** “Add Python to PATH”.
- Check in terminal:
```
python --version
```
Expected: `Python 3.x.x`

---

## 👋 Your first program
Create `hello-world.py`:
```python
print("Hello, World!")
```
Run:
```
python hello-world.py
```

**What happened?** `print(...)` shows text on the screen. Text inside quotes is a **string**.

---

## 💬 Comments
Use comments to explain code — Python ignores them:
```python
# This line prints a message
print("Hello")
```

---

## 📦 Variables & Types
Variables store values:
```python
name = "Alex"     # string
age = 30          # integer
height = 1.75     # float
```
Combine values:
```python
print(name, "is", age, "years old.")
```

---

## ⌨️ Input
`input()` asks the user:
```python
user = input("Your name: ")
print("Welcome,", user)
```

Numbers: convert text to int/float:
```python
year = int(input("Birth year: "))
print("You will be", 2025 - year, "years old (approx).")
```

---

## 📝 Tasks
1. `hello-world.py` — print a message.
2. `my-intro.py` — ask name and greet the user.
3. `age-in-5-years.py` — ask current age (number) and print age in 5 years.
4. Bonus: `sum-two.py` — ask two numbers and print their sum.

---

## 🎯 Example
```python
age = int(input("How old are you? "))
print("In 5 years you will be", age + 5)
```

👉 Next: [Module 4. Conditions & Loops](module-4-conditions-loops.md)

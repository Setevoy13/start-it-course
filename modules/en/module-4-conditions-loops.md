# Module 4. Conditions and Loops 🔄

**Goal:** make your programs *think* (conditions) and *repeat* (loops).

---

## ⚖️ Conditions: if / elif / else
```python
temp = int(input("Temperature: "))

if temp > 30:
    print("Hot")
elif temp >= 15:
    print("Warm")
else:
    print("Cold")
```
- `if` — first check
- `elif` — another check
- `else` — everything else

**Comparison operators:** `> >= < <= == !=`

---

## 🔁 Loops: for and while
**for** — repeat a known number of times:
```python
for i in range(1, 6):
    print(i)
```
**while** — repeat *while* a condition is true:
```python
count = 3
while count > 0:
    print("Countdown:", count)
    count -= 1
```

---

## 🧠 Boolean logic
- `and`, `or`, `not`:
```python
age = 20
has_id = True
if age >= 18 and has_id:
    print("Allowed")
```

---

## 🎲 Mini‑game: Guess the Number (3 attempts + hints)
```python
import random

secret = random.randint(1, 10)
attempts = 3

for _ in range(attempts):
    guess = int(input("Guess (1–10): "))
    if guess == secret:
        print("Correct! 🎉")
        break
    elif guess < secret:
        print("Too small!")
    else:
        print("Too big!")
else:
    print("Out of attempts. The number was", secret)
```

---

## 📝 Tasks
1. `even-odd.py` — ask a number; print **Even** or **Odd**.
2. `countdown.py` — print numbers 5..1 using `while`.
3. `multiplication-table.py` — print a table for a number (e.g., 3 → 3,6,9… up to 30).
4. Improve the **Guess** game: allow the user to choose the max number (e.g., 1..20).

👉 Next: [Module 5. Working with Data](module-5-working-with-data.md)

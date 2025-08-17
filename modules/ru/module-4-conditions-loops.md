# Модуль 4. Условия и циклы 🔄

**Цель:** научить программу *думать* (условия) и *повторять* (циклы).

---

## ⚖️ Условия: if / elif / else
```python
temp = int(input("Температура: "))

if temp > 30:
    print("Жарко")
elif temp >= 15:
    print("Тепло")
else:
    print("Холодно")
```
- `if` — первый проверяемый вариант
- `elif` — ещё одна проверка
- `else` — всё остальное

**Операторы сравнения:** `> >= < <= == !=`

---

## 🔁 Циклы: for и while
**for** — когда заранее известно число повторений:
```python
for i in range(1, 6):
    print(i)
```
**while** — пока условие истинно:
```python
count = 3
while count > 0:
    print("Обратный отсчёт:", count)
    count -= 1
```

---

## 🧠 Логика (булевы значения)
- `and`, `or`, `not`:
```python
age = 20
has_id = True
if age >= 18 and has_id:
    print("Можно")
```

---

## 🎲 Мини‑игра: Угадай число (3 попытки + подсказки)
```python
import random

secret = random.randint(1, 10)
attempts = 3

for _ in range(attempts):
    guess = int(input("Угадай (1–10): "))
    if guess == secret:
        print("Верно! 🎉")
        break
    elif guess < secret:
        print("Слишком мало!")
    else:
        print("Слишком много!")
else:
    print("Попытки закончились. Число было", secret)
```

---

## 📝 Задания
1. `even-odd.py` — спроси число; выведи **Чётное** или **Нечётное**.
2. `countdown.py` — выведи числа 5..1 с помощью `while`.
3. `multiplication-table.py` — выведи таблицу умножения для числа (например, 3 → 3,6,9… до 30).
4. Улучши игру «Угадай»: пусть пользователь сам выбирает максимальное число (например, 1..20).

👉 Далее: [Модуль 5. Работа с данными](module-5-working-with-data.md)

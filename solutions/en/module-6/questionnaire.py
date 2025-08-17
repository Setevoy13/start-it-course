profile = {}
profile["name"] = input("Name: ")
profile["age"] = input("Age: ")
profile["city"] = input("City: ")
profile["hobby"] = input("Hobby: ")
with open("profile.txt", "w", encoding="utf-8") as f:
    for k, v in profile.items():
        f.write(f"{k}: {v}\n")
print("Saved to profile.txt")

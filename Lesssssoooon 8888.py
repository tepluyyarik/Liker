result = []

def divider(a, b):
    try:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Обидва аргументи мають бути числами")
        if a < b:
            raise ValueError("a має бути більше, ніж r дорівнює bo")
        if b > 100:
            raise IndexError("b Повинно бути 100 або менше")
        return a / b
    except Exception as e:
        print(f"Помилка: {e}")
        return None


data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}  # "123": 4, 18: 0, []: 15, 8 : 4

for key, value in data.items():
    try:
        res = divider(key, value)
        if res is not None:
            result.append(res)
    except Exception as e:
        print(f"Ексепція до коду {key}: {e}")

print(result)
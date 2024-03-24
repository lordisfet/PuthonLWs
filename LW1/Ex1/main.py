def InPut():
    a = float(input("Введіть a: "))
    b = float(input("Введіть b: "))
    while a <= 0 or b <= 0:
        print("Невірні значення! Повторіть введення.")
        a = float(input("Введіть a: "))
        b = float(input("Введіть b: "))
    return a, b

def FoundX(a, b):
    if a > b:
        return (b * a) + 1
    elif a == b:
        return -10
    elif a < b:
        return (a - 5) / b

a, b = InPut()
x = FoundX(a, b)
print(f"Значення X: {x}")

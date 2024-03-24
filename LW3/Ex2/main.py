def max_digit(n):
    return int(max(str(n)))

n = int(input("Введіть чотерьох значне число: "))
print(f"Найбільша цифра в числі {n} дорівнює", max_digit(n))

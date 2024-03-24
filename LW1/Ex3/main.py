def print_pattern(n):
  if not 1 < n < 9:
    print("Неправильне значення n. n має бути в діапазоні від 1 до 9.")
    return

  for i in range(2 * n + 1):
    for j in range(abs(n - i)):
      print(n, end="")

    if not n == i:
        print()

n = int(input("Введіть n: "))
print_pattern(n)
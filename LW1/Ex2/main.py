def sum_even_product_odd(n):
  sum_even = 0
  product_odd = 1

  for i in range(0, n + 1):
    if i % 2 == 0:
      sum_even += i
    else:
      product_odd *= i
  return sum_even, product_odd

for i in range(0, 20):
  sum_even, product_odd = sum_even_product_odd(i)
  print(f"Сума парних чисел всіх чисел до {i}: {sum_even}")
  print(f"Добуток непарних чисел до числа {i}: {product_odd}\n")
def sum_even_product_odd(n):
  sum_even = 0
  product_odd = 1

  for i in range(n + 1):
    if i % 2 == 0:
      sum_even += i
    else:
      product_odd *= i

  print(f"Сума парних чисел: {sum_even}")
  print(f"Добуток непарних чисел: {product_odd}")


sum_even_product_odd(20)

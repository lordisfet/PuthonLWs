def input_array(arr, n):
    for i in range(n):
        arr.append(int(input(f"Введіть {i} елемент списку: ")))
    return arr

def found_even_n_odd(arr):
    even_numbers = []
    odd_numbers = []

    for num in arr:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
    return even_numbers, odd_numbers

def outout_array(even_numbers, odd_numbers):
    print("Парні числа:", even_numbers)
    print("Непарні числа:", odd_numbers)

n = int(input("Введіть кількість елментів в списку: "))

arr = []
arr = input_array(arr, n)
even_numbers, odd_numbers = found_even_n_odd(arr)
outout_array(even_numbers, odd_numbers)
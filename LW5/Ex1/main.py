def sum_even_index_elements():
    n = int(input("Введіть кількість елементів масиву: "))
    array = []
    for i in range(n):
        array.append(int(input(f"Введіть елемент {i+1}: ")))

    sum_even_index = 0
    for i in range(0, n, 2):
        sum_even_index += array[i]
    return sum_even_index

print("Сума елементів з парним індексом: ", sum_even_index_elements())

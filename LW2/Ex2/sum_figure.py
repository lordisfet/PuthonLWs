def sum_figure(n):
    sum = 0
    while not (n == 0):
        sum += (n % 10)
        n = n//10
    return sum
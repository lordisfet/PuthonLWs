n = 7
array = [[] for i in range(n)]

for i in range(n):
    for j in range(n):
        array[i].append(1 if (i + j) % 2 == 0 else 0)

print("\n".join(f"{row}" for row in array))

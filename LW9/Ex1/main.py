# а) створює текстовий файл TF12_1 із символьних рядків різної довжини
with open('TF12_1.txt', 'w') as f:
    for i in range(1, 12):
        f.write('a' * i + '\n')

# б) читає вміст файла TF12_1 і записує його у файл TF12_2
with open('TF12_1.txt', 'r') as f1, open('TF12_2.txt', 'w') as f2:
    lines = f1.readlines()
    for i, line in enumerate(lines, start=1):
        f2.write(line[:i] + '\n')

# в) читає вміст файла TF12_2 і друкує його по рядках
with open('TF12_2.txt', 'r') as f:
    print(f.read())
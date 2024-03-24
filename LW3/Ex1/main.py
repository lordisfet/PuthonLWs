def get_every_third_char(s):
    return s[3:19:3]

s = "Це строка для тесту зрізів в Python"
print("Строка до зрізу:", s)
print("Строка після зрізу", get_every_third_char(s))
def shortest_word_length(sentence):
    words = sentence.split()
    return min(len(word) for word in words)

sentence = 'Це ваше речення для тестування'
print(f"Найкорше речення строки \"{sentence}\" має довжину", shortest_word_length(sentence), "символи")

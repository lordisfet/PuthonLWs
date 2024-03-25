def find_word(word_list, word_to_find):
    if word_to_find in word_list:
        return f"Слово \"{word_to_find}\" знайдено в списку"
    else:
        return f"Слово \"{word_to_find}\" не знайдено в списку"

words = ['яблуко', 'банан', 'вишня', 'гранар']
print(find_word(words, 'банан'))
print(find_word(words, 'диня'))

import nltk
from nltk.corpus import gutenberg
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import string
import matplotlib.pyplot as plt

# Імпортування бібліотеки NLTK та завантаження необхідних ресурсів
nltk.download('gutenberg')
nltk.download('stopwords')
nltk.download('punkt')

# Завантаження тексту
text = gutenberg.raw('chesterton-ball.txt')

# Токенізація тексту
tokens = nltk.word_tokenize(text)

# Визначення кількості слів у тексті
print(f"Кількість слів у тексті: {len(tokens)}")

# Знаходження 10 найбільш вживаних слів
fdist = FreqDist(tokens)
most_common_words = fdist.most_common(10)

# Виведення 10 найбільш вживаних слів
print("10 найбільш вживаних слів у тексті:")
print(most_common_words)

# Побудова стовпчастої діаграми для 10 найбільш вживаних слів
words, frequency = zip(*most_common_words)
plt.figure(figsize=(10, 5))
plt.bar(words, frequency)
plt.title('10 найбільш вживаних слів у тексті')
plt.show()

# Видалення стоп-слів та пунктуації
stop_words = set(stopwords.words('english') + list(string.punctuation))
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

# Знаходження 10 найбільш вживаних слів після видалення стоп-слів
fdist_filtered = FreqDist(filtered_tokens)
most_common_words_filtered = fdist_filtered.most_common(10)

# Виведення 10 найбільш вживаних слів після видалення стоп-слів
print("10 найбільш вживаних слів у тексті після видалення стоп-слів:")
print(most_common_words_filtered)

# Побудова стовпчастої діаграми для 10 найбільш вживаних слів після видалення стоп-слів
words_filtered, frequency_filtered = zip(*most_common_words_filtered)
plt.figure(figsize=(10, 5))
plt.bar(words_filtered, frequency_filtered)
plt.title('10 найбільш вживаних слів у тексті після видалення стоп-слів')
plt.show()

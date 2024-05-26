import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer, PorterStemmer
from nltk.corpus import stopwords
import string

# Імпортування бібліотеки NLTK та завантаження необхідних ресурсів
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

# Читання тексту з файлу
with open('apollo_description.txt', 'r') as file:
    text = file.read()

# Токенізація по словам
tokens = word_tokenize(text)

# Лемматизація та стеммінг
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()
lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
stemmed_tokens = [stemmer.stem(token) for token in tokens]

# Видалення стоп-слів та пунктуації
stop_words = set(stopwords.words('english') + list(string.punctuation))
filtered_tokens = [word for word in lemmatized_tokens if word.lower() not in stop_words]

with open('processed_apollo_description.txt', 'w') as file:
    file.write(' '.join(filtered_tokens))

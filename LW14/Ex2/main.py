import matplotlib.pyplot as plt
import pandas as pd

# Завантаження даних з файлу CSV
data = pd.read_csv('DataBase.csv')

# Вилучення унікальних назв країн
unique_countries = data['Country Name'].dropna().unique()


# Побудова графіків для всіх країн
def plot_all_countries_data():
    plt.figure(figsize=(10, 5))

    # Ітерація по кожній країні та побудова графіка
    for country in unique_countries:
        country_data = data[data['Country Name'] == country]
        years = country_data.columns[4:]
        values = country_data.iloc[0, 4:]
        plt.plot(years, values, label=country)

    plt.title('Динаміка показника для всіх країн')
    plt.xlabel('Рік')
    plt.ylabel('Значення показника')
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


plot_all_countries_data()

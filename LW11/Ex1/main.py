import csv

try:
    with open('DataBase.csv', 'r', newline='') as file:
        reader = csv.DictReader(file, delimiter=',')

        print("Population for Ukraine (1991-2019):")
        for row in reader:
            if row['Country Name'] == 'Ukraine':
                for year in range(1991, 2020):
                    col_name = f"{year} [YR{year}]"
                    print(f"{year}: {row[col_name]}")
                break

    with open('DataBase.csv', 'r', newline='') as file:
        reader = csv.DictReader(file, delimiter=',')
        data = list(reader)

    population_values = [float(data[0][f"{year} [YR{year}]"]) for year in range(1991, 2020)]

    min_population = min(population_values)
    max_population = max(population_values)

    print(f"\nMin Population: {min_population}")
    print(f"Max Population: {max_population}")

    with open('Population_results.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Statistic", "Value"])
        writer.writerow(["Min Population", min_population])
        writer.writerow(["Max Population", max_population])

except FileNotFoundError:
    print("File 'DataBase.csv' not found.")
except Exception as e:
    print(f"An error occurred: {e}")

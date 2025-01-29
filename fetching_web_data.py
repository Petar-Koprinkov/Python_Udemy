import requests
from bs4 import BeautifulSoup
import json
import os

my_url = "https://en.wikipedia.org/wiki/ASEAN"


def fetch_data():
    web_content = requests.get(my_url).content
    table = BeautifulSoup(web_content, 'html.parser').find('table', {
        'class': 'sortable wikitable plainrowheaders'})

    return table


def extract_urban_data(soup):
    table = soup

    data_rows = []
    for row in table.find_all('tr')[1:]:
        th_columns = row.find_all('th')
        core_city = th_columns[1].text.strip()
        columns = row.find_all('td')
        if len(columns) >= 4:
            country = columns[2].text.strip()
            area = columns[1].text.strip()
            population = columns[0].text.strip()

            data_rows.append({
                'country': country,
                'core_city': core_city,
                'population': population,
                'area': area,
            })

    return data_rows


def create_countries_dict(data_rows):
    countries_dict = {}

    for entry in data_rows:
        country = entry['country']
        core_city = entry['core_city']
        population = entry['population']
        area = entry['area']

        try:
            population = int(population.replace(",", ""))
        except ValueError:
            population = None

        try:
            area = float(area.replace(" km²", "").replace(",", ""))
        except ValueError:
            area = None

        if country not in countries_dict:
            countries_dict[country] = []

        countries_dict[country].append({
            'city': core_city,
            'population': population,
            'area': area,
            'population_density': None
        })

    for country, cities in countries_dict.items():
        for city in cities:
            if city['population'] is not None and city['area'] is not None:
                population_density = city['population'] / city['area']
                city['population_density'] = round(population_density, 2)
    return countries_dict


def save_to_file(countries_dict, filename='countries_data.json'):
    with open(filename, 'w') as file:
        json.dump(countries_dict, file, indent=4)


def compare_and_save(countries_dict, filename='countries_data.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            old_data = json.load(file)

        if countries_dict != old_data:
            print("New data detected. Updating the file.")
            save_to_file(countries_dict, filename)
        else:
            print("No new data. File remains unchanged.")
    else:
        print("No previous data found. Saving new data.")
        save_to_file(countries_dict, filename)


def main():
    try:
        soup = fetch_data()
        data_rows = extract_urban_data(soup)
        countries_dict = create_countries_dict(data_rows)
        compare_and_save(countries_dict)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()

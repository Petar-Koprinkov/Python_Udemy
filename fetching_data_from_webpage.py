import requests
from bs4 import BeautifulSoup
import json
import os

my_url = 'https://en.wikipedia.org/wiki/List_of_European_Union_member_states_by_population'

my_file = 'my_file'


def fetch_population_data():
    web_content = requests.get(my_url).content

    table = BeautifulSoup(web_content, 'html.parser').find('table', {'class': 'wikitable sortable static-row-numbers static-row-header-text sort-under-center hover-highlight'})

    data_rows = table.find_all('tr')[1:-1]

    countries_dict = {}

    for row in data_rows:
        cols = row.find_all('td')
        country = cols[0].text.strip()
        population_text = cols[1].text.strip().replace(',', '')
        population = int(population_text)

        countries_dict[country] = {'country_population': population}

    return countries_dict


def calculate_population_percentage(countries_dict):
    total_population = sum(country['country_population'] for country in countries_dict.values())

    for country, data in countries_dict.items():
        percentage = (data['country_population'] / total_population) * 100
        countries_dict[country]['country_population_percentage'] = round(percentage, 1)

    return countries_dict, total_population


def save_data_to_file(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


def load_data_from_file(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return None


def main():
    latest_data = fetch_population_data()
    latest_data, total_population = calculate_population_percentage(latest_data)
    old_data = load_data_from_file(my_file)
    if old_data != latest_data:
        save_data_to_file(latest_data, my_file)

    for country, data in latest_data.items():
        print(
            f"{country}: Population = {data['country_population']}, Percentage = {data['country_population_percentage']}%")


if __name__ == '__main__':
    main()

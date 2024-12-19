import requests
import json
import os

# Получаем данные стран, говорящих на нужных языках
languages = ['spanish', 'portuguese', 'german']
countries_data = []

# Функция для запроса данных по языку
def get_countries_by_language(language):
    url = f'https://restcountries.com/v3.1/lang/{language}'
    response = requests.get(url)
    return response.json()

# Создание папки для сохранения флагов
os.makedirs('flags', exist_ok=True)

# Собираем данные по всем языкам
for language in languages:
    countries = get_countries_by_language(language)
    for country in countries:
        # Фильтрация по площади > 100000
        area = country.get('area', 0)
        if area > 100000:
            countries_data.append({
                'name': country.get('name', {}).get('common'),
                'capital': country.get('capital', [])[0] if country.get('capital') else 'N/A',
                'area': area,
                'population': country.get('population', 0),
                'flag': country.get('flags', {}).get('png', ''),
                'language': language
            })

# Сохраняем данные в файл results.json
with open('results.json', 'w', encoding='utf-8') as f:
    json.dump(countries_data, f, ensure_ascii=False, indent=4)

# Выводим страну с наибольшей площадью для каждого языка
max_area_country = {language: None for language in languages}

for data in countries_data:
    language = data['language']
    if not max_area_country[language] or data['area'] > max_area_country[language]['area']:
        max_area_country[language] = data

for language, country in max_area_country.items():
    print(f"Страна с наибольшей площадью на {language}: {country['name']} ({country['area']} кв. км)")

# Загружаем флаги и сохраняем их как .png
for data in countries_data:
    flag_url = data['flag']
    if flag_url:
        flag_response = requests.get(flag_url)
        flag_filename = f"flags/{data['name']}_{data['language']}.png"
        with open(flag_filename, 'wb') as flag_file:
            flag_file.write(flag_response.content)


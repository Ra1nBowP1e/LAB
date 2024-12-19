import requests
from bs4 import BeautifulSoup
import csv
import time

def get_top_results(gender, discipline, year, retries=3):
    url = f"https://worldathletics.org/records/toplists/{discipline}/{gender}/{year}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

    for _ in range(retries):
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                
                table = soup.find('table', {'class': 'records__table'})
                if not table:
                    print(f"Не найдена таблица на странице {url}")
                    return None
                
                rows = table.find_all('tr')[1:]  
                
                results = []
                for row in rows:
                    cols = row.find_all('td')
                    if len(cols) < 5:
                        continue
                    
                    name = cols[1].get_text(strip=True)  # Имя спортсмена
                    country = cols[2].get_text(strip=True)  # Страна
                    result = cols[3].get_text(strip=True)  # Результат (например, высота, длина)
                    date = cols[4].get_text(strip=True)  # Дата соревнования
                    
                    results.append([year, name, country, result, date])
                
                return results
            else:
                print(f"Ошибка при запросе {url}. Статус код: {response.status_code}")
                time.sleep(2)
        except Exception as e:
            print(f"Ошибка запроса: {e}. Повторяю...")
            time.sleep(2)
    
    print(f"Не удалось получить данные с {url} после {retries} попыток.")
    return None


def collect_results():
    disciplines = ['high-jump', 'pole-vault', 'long-jump', 'triple-jump']
    genders = ['men', 'women']
    years = range(2001, 2025)
    
    all_results = []
    
 
    for gender in genders:
        for discipline in disciplines:
            for year in years:
                print(f"Сбор данных для {gender} в дисциплине {discipline} за {year} год...")
                results = get_top_results(gender, discipline, year)
                if results:
                    all_results.extend(results)
                time.sleep(2) 
    
  
    with open('top_results.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Year', 'Athlete', 'Country', 'Result', 'Date'])
        writer.writerows(all_results)
    print("Данные успешно сохранены в top_results.csv")


collect_results()

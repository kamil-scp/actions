# my_script.py

import requests
import pandas as pd

def fetch_users():
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    response.raise_for_status()  # podniesie wyjątek jeśli status != 200
    return response.json()

def process_users(data):
    df = pd.DataFrame(data)
    # Zostawiamy tylko imię i miasto
    result = df[['name', 'address']].copy()
    # 'address' to słownik, wyciągamy 'city'
    result['city'] = result['address'].apply(lambda x: x['city'])
    result = result.drop(columns=['address'])
    return result

if __name__ == "__main__":
    data = fetch_users()
    df = process_users(data)
    print(df)

import requests

def get_exchange_rate(currency_code):
    api_url = f'https://minfin.com.ua/api/currency/rates/banks/{currency_code.lower()}/?page=1&cpp=30&city=kiev'

    try:
        response = requests.get(api_url)
        response.raise_for_status()

        data = response.json()

        # Проверка, что есть данные в ответе
        if 'data' in data and data['data']:
            print(f"Exchange rates for {currency_code}:", data['data'])
        else:
            print(f"No exchange rate data found for {currency_code}.")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Тестирование для валюты EUR (евро)
    get_exchange_rate("EUR")

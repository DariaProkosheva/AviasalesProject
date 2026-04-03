import requests
from config import (
    API_TOKEN,
    POPULAR_ROUTES_API_URL,
    MONTH_MATRIX_API_URL,
    CURRENCY
)


def get_popular_routes(origin_city: str):
    payload = {
        'origin': origin_city,
        'currency': CURRENCY,
        'token': API_TOKEN
    }

    response = requests.get(POPULAR_ROUTES_API_URL, params=payload)
    if response.status_code != 200:
        print(
            f"  Ошибка при запросе популярных маршрутов для {origin_city}: "
            f"{response.status_code} {response.text}"
        )
        return []

    return response.json().get('data', {}).keys()


def get_month_matrix(origin_city: str, destination: str, month_str: str):
    payload = {
        'origin': origin_city,
        'destination': destination,
        'currency': CURRENCY,
        'month': month_str,
        'token': API_TOKEN
    }

    response = requests.get(MONTH_MATRIX_API_URL, params=payload)
    if response.status_code != 200:
        print(
            f"      Ошибка при запросе {month_str}: "
            f"{response.status_code} {response.text}"
        )
        return []

    return response.json().get('data', [])
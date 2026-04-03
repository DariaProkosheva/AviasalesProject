from config import YEAR
from api import get_popular_routes, get_month_matrix


def collect_city_data(origin_city: str):
    print(f"Обработка данных для города {origin_city}...")
    print("  Получение популярных направлений...")

    popular_routes = get_popular_routes(origin_city)
    if not popular_routes:
        print(f"  Нет популярных маршрутов для города {origin_city}.")
        return []

    print(f"  Популярные направления из {origin_city}: {', '.join(popular_routes)}")

    city_data = []

    for destination in popular_routes:
        print(f"    Сбор данных за {YEAR} год для направления {destination}...")
        for month in range(1, 13):
            month_str = f"{YEAR}-{month:02d}-01"
            data = get_month_matrix(origin_city, destination, month_str)
            city_data.extend(data)
            print(f"      Месяц {month_str}: {len(data)} записей.")

    return city_data
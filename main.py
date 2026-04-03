from config import YEAR, POPULAR_ORIGIN_CITIES
from collector import collect_city_data
from storage import save_csv, save_json


def main():
    all_city_data = []

    for origin_city in POPULAR_ORIGIN_CITIES:
        city_data = collect_city_data(origin_city)
        all_city_data.extend(city_data)

        city_output_file = f"{origin_city}_routes_{YEAR}.csv"
        if city_data:
            save_csv(city_output_file, city_data)
            print(f"  Данные для {origin_city} успешно записаны в {city_output_file}.")
        else:
            print(f"  Нет данных для записи для {origin_city}.")

    print("Сохранение общих данных...")

    save_json(f"all_cities_routes_{YEAR}.json", all_city_data)

    if all_city_data:
        save_csv(f"all_cities_routes_{YEAR}.csv", all_city_data)
        print(f"Общие данные успешно записаны в all_cities_routes_{YEAR}.csv.")
    else:
        print("Нет данных для записи.")

    print(f"Всего записей собрано: {len(all_city_data)}")


if __name__ == "__main__":
    main()
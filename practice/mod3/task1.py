import requests


API_KEY = "7d44db20f0b22feac520c126ef2287fa"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def wind_message(speed: float) -> str:
    if speed < 0.3:
        return "Штиль"
    elif speed < 5:
        return "Слабый ветер"
    elif speed < 10:
        return "Умеренный ветер"
    elif speed < 15:
        return "Сильный ветер"
    elif speed < 20:
        return "Очень сильный ветер"
    else:
        return "Штормовой ветер"


def pressure_mmhg(hpa: int) -> float:
    """Перевод давления из гПа в мм рт. ст."""
    return hpa * 0.75006


def get_weather(city: str, api_key: str) -> dict:
    """API запрос к openweathermap"""
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",
        "lang": "ru",
    }

    response = requests.get(BASE_URL, params=params, timeout=10)
    response.raise_for_status()
    return response.json()


def print_weather(data: dict) -> None:
    """Красиво выводит данные о погоде"""
    city_name = data.get("name", "Неизвестный город")
    country = data.get("sys", {}).get("country", "")

    main = data.get("main", {})
    weather_list = data.get("weather", [])
    weather = weather_list[0] if weather_list else {}
    wind = data.get("wind", {})
    clouds = data.get("clouds", {})

    temp = main.get("temp")
    feels_like = main.get("feels_like")
    pressure = main.get("pressure")
    humidity = main.get("humidity")
    description = weather.get("description", "нет данных")
    wind_speed = wind.get("speed", 0)
    cloudiness = clouds.get("all", 0)

    print(f"\nПогода в городе: {city_name}, {country}")
    print("-" * 40)
    print(f"Температура: {temp} °C")
    print(f"Ощущается как: {feels_like} °C")
    print(f"Ветер: {wind_speed} м/с — {wind_message(wind_speed)}")
    print(f"Давление: {pressure} гПа ({pressure_mmhg(pressure):.0f} мм рт. ст.)")
    print(f"Влажность: {humidity} %")
    print(f"Состояние: {description}")
    print(f"Облачность: {cloudiness} %")

    # Дополнительно
    visibility = data.get("visibility")
    if visibility is not None:
        print(f"Видимость: {visibility / 1000:.1f} км")

    temp_min = main.get("temp_min")
    temp_max = main.get("temp_max")
    if temp_min is not None and temp_max is not None:
        print(f"Мин/макс сегодня: {temp_min} °C / {temp_max} °C")


def main():
    city = input("Введите название города: ").strip()

    if not city:
        print("Ошибка: название города не введено.")
        return

    try:
        data = get_weather(city, API_KEY)
        print_weather(data)

    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            print("Город не найден. Проверьте правильность названия.")
        elif e.response.status_code == 401:
            print("Неверный API-ключ OpenWeather.")
        else:
            print(f"Ошибка HTTP: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Ошибка сети: {e}")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")


if __name__ == "__main__":
    main()
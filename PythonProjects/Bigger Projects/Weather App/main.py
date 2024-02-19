from weather_api import get_weather, get_weather_details, Weather


def main():
    # Ask the user for their city
    user_city = input('Enter a city: ')

    # Get the current weather details
    current_weather = get_weather(user_city, mock=True)
    weather_details = get_weather_details(current_weather)

    # Get the current days
    dfmt = '%d/%m/%y'
    days = sorted({date.date.strftime(dfmt) for date in weather_details})

    for day in days:
        print(day)
        print('---')

        # Group the weather data by date to make it easier to read
        grouped = [current for current in weather_details if current.date.strftime(dfmt) == day]
        for element in grouped:
            print(element)

        print()  # An empty line


if __name__ == '__main__':
    main()

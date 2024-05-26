# import the module
import python_weather
import datetime

import asyncio
import os
import requests

def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]


def get_location():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    city = response.get("city")
    return city


async def getweather():
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime('%Y-%m-%d %I:%M %p')
    # declare the client. the measuring unit used defaults to the metric system (celcius, km/h, etc.)
    async with python_weather.Client(unit=python_weather.METRIC) as client:
        # fetch a weather forecast from a city
        location = get_location()
        weather = await client.get(location)

        # Print current location, date and temperature
        print(f"Location : {location}")
        print(f"Date : {formatted_datetime}")
        print(f"Celcius : {weather.temperature}")

        # Print the forecast for tomorrow
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        print("\nTomorrows forecast:")
        for daily in weather.daily_forecasts:
            if daily.date == tomorrow:
                print(f"Temperature: {daily.temperature}")
                for hourly in daily.hourly_forecasts:
                    print(
                        f"Time: {hourly.time},\nTemperature: {hourly.temperature},\nDescription: {hourly.description},\nKind: {hourly.kind}")
                break

if __name__ == '__main__':
    # see https://stackoverflow.com/questions/45600579/asyncio-event-loop-is-closed-when-getting-loop
    # for more details
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    asyncio.run(getweather())

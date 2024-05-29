import python_weather
import datetime
import asyncio
import os
import requests
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from time import sleep

console = Console()

def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]

def get_location():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    city = response.get("city")
    return city

def create_weather_table(weather):
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Time", style="dim", width=12)
    table.add_column("Thu 14. Apr", justify="center")
    table.add_column("Fri 15. Apr", justify="center")
    table.add_column("Sat 16. Apr", justify="center")

    times = ["Morning", "Noon", "Evening", "Night"]
    forecasts = []
    for day in weather.daily_forecasts[:3]:
        day_forecast = [
            f"Sunny\n{hourly.temperature} °C\n{hourly.description}\n{hourly.wind_speed} km/h"
            for hourly in day.hourly_forecasts[:4]
        ]
        forecasts.append(day_forecast)

    for i in range(len(times)):
        table.add_row(times[i], forecasts[0][i], forecasts[1][i], forecasts[2][i])

    return table

async def getweather():
    async with python_weather.Client(unit=python_weather.METRIC) as client:
        location = get_location()
        weather = await client.get(location)
        current_datetime = datetime.datetime.now()
        formatted_datetime = current_datetime.strftime('%Y-%m-%d %I:%M %p')

        console.print(Panel.fit(f"Weather for City: {location}, United States of America", style="bold blue"))
        console.print(f"Date: {formatted_datetime}", style="bold green")
        console.print(f"Current Temperature: {weather.current.temperature} °C", style="bold yellow")

        table = create_weather_table(weather)
        console.print(table)

        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        console.print("\nTomorrow's forecast:", style="bold red")
        for daily in weather.daily_forecasts:
            if daily.date == tomorrow:
                console.print(f"Temperature: {daily.temperature} °C")
                for hourly in daily.hourly_forecasts:
                    console.print(
                        f"Time: {hourly.time}, "
                        f"Temperature: {hourly.temperature} °C, "
                        f"Description: {hourly.description}, "
                        f"Kind: {hourly.kind}"
                    )
                break

        # Pause for 1 second before fetching and printing the next weather update
        sleep(1)

if __name__ == '__main__':
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    asyncio.run(getweather())

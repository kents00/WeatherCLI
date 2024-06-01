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

    today = datetime.datetime.now()
    for i in range(3):
        date = (today + datetime.timedelta(days=i)).strftime("%a %d %b")
        table.add_column(date, justify="center")

    forecasts = []
    times = ["06:00 AM", "12:00 PM", "03:00 PM", "06:00 PM"]
    time_filters = ["06:00 AM", "12:00 PM", "03:00 PM", "06:00 PM"]

    for day in list(weather.daily_forecasts)[:3]:
        day_forecast = []
        for hourly in day.hourly_forecasts:
            time = hourly.time.strftime("%I:%M %p")
            if time in time_filters:
                forecast = f"{hourly.description} \n{hourly.temperature} °C\n{hourly.wind_speed} km/h\n"
                day_forecast.append((time, forecast))
        day_forecast = sorted(
            day_forecast, key=lambda x: time_filters.index(x[0]))
        forecasts.append(day_forecast)

    for time in times:
        row = [time]
        for day_forecast in forecasts:
            forecast = next((f[1] for f in day_forecast if f[0] == time), "")
            row.append(forecast)
        table.add_row(*row)

    return table


async def getweather():
    async with python_weather.Client(unit=python_weather.METRIC) as client:
        location = get_location()
        weather = await client.get(location)
        current_datetime = datetime.datetime.now()
        formatted_datetime = current_datetime.strftime('%Y-%m-%d %I:%M %p')
        ip_address = get_ip()

        console.print(Panel.fit(f"City: {location}", style="bold blue"))
        console.print(f"Date: {formatted_datetime}", style="bold green")
        console.print(
            f"Current Temperature: {weather.temperature} °C", style="bold yellow")
        console.print(f"IP Address: {ip_address}", style="bold magenta")

        table = create_weather_table(weather)
        console.print(table)
        sleep(1)

if __name__ == '__main__':
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(getweather())

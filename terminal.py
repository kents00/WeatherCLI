from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()


def create_weather_table():
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Time", style="dim", width=12)
    table.add_column("Thu 14. Apr", justify="center")
    table.add_column("Fri 15. Apr", justify="center")
    table.add_column("Sat 16. Apr", justify="center")

    times = ["Morning", "Noon", "Evening", "Night"]
    day_1 = [
        "Sunny\n32 - 39 °F\n↓ 7 - 14 mph\n6 mi\n0.0 in | 0%\n",
        "Sunny\n46 - 51 °F\n↙ 8 - 9 mph\n6 mi\n0.0 in | 0%\n",
        "Sunny\n59 - 62 °F\n← 6 - 7 mph\n6 mi\n0.0 in | 0%\n",
        "Clear\n46 - 50 °F\n← 7 - 12 mph\n6 mi\n0.0 in | 0%\n"
    ]
    day_2 = [
        "Sunny\n41 - 44 °F\n↙ 4 - 6 mph\n6 mi\n0.0 in | 0%\n",
        "Sunny\n57 - 59 °F\n← 7 - 8 mph\n6 mi\n0.0 in | 0%\n",
        "Sunny\n62 - 66 °F\n← 8 - 9 mph\n6 mi\n0.0 in | 0%\n",
        "Clear\n53 - 55 °F\n← 5 - 8 mph\n6 mi\n0.0 in | 0%\n"
    ]
    day_3 = [
        "Sunny\n44 °F\n↙ 1 - 3 mph\n6 mi\n0.0 in | 0%\n",
        "Sunny\n59 - 60 °F\n← 6 - 7 mph\n6 mi\n0.0 in | 0%\n",
        "Sunny\n69 °F\n← 5 - 6 mph\n6 mi\n0.0 in | 0%\n",
        "Clear\n53 - 55 °F\n← 4 - 10 mph\n6 mi\n0.0 in | 0%\n"
    ]

    for i in range(len(times)):
        table.add_row(times[i], day_1[i], day_2[i], day_3[i])

    return table


def main():
    console.print(Panel.fit(
        "Weather for City: Pittsburgh, United States of America", style="bold blue"))
    console.print(create_weather_table())


if __name__ == "__main__":
    main()

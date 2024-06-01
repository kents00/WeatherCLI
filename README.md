# WeatherCLI
This is a Python script that fetches the current weather and forecasts for the next three days. It uses the python_weather library to interact with the OpenWeatherMap API and the rich library for formatting and displaying the output. The script also includes functions to get the user's IP address and location.

![Weather](https://github.com/kents00/WeatherCLI/assets/69900896/02f3b01a-e29e-4d84-8127-8c62e0b353d7)

The primary purpose of this project is to provide a simple and user-friendly way to access current weather conditions and forecasts. It can be used to stay updated on the weather without needing to manually check multiple sources.

### **Key Features**

- **Current Weather Information**:
  - Fetches the current temperature and other weather details for the user's location.
- **Forecast for the Next Three Days**:
  - Displays the weather forecast for the next three days, including temperature, wind speed, and description.
- **User-Friendly Interface**:
  - Uses the **`rich`** library to format and display the output in a visually appealing way.
- **Location Detection**:
  - Automatically detects the user's location using their IP address.

### **Additional Features**

- **IP Address Detection**:
  - Uses the **`requests`** library to fetch the user's IP address and determine their location.
- **Error Handling**:
  - Includes error handling to handle cases where the API is unavailable or the user's location cannot be determined.

### **Prerequisites**

- Python 3.8 or higher
- **`python_weather`** library
- **`rich`** library

### **Installation Steps**

1. **Install Python**:
    - If you don't have Python installed, download and install it from the official [Python website](https://www.python.org/downloads/).
2. Install the necessary dependencies by running `pip install -r requirements.txt`

### **Running the Script**

1. **Save the Script**:
    - Save the provided script in a file named **`weather.py`**.
2. **Run the Script**:
    - Open a terminal or command prompt.
    - Navigate to the directory where you saved the script.
    - Run the command **`python weather.py`** to execute the script.

### **Compatibility**

- **Windows**:
  - Use **`asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())`** to ensure compatibility on Windows systems.

### Issues

If you're having trouble integrating this code into your machine, [open a new issue](https://github.com/kents00/WeatherCLI/issues). As the module continues to develop, it will be easier for more developers to integrate updates and improve the overall user performance!

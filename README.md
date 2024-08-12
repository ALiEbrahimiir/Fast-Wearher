
# Weather API with FastAPI

This project is a Python application built using FastAPI that provides a weather API. It leverages the Weather.town API along with requests, BeautifulSoup, and datetime to offer detailed weather information. The API includes endpoints to retrieve weather data for cities

### Retrieve weather data including:

*    Name of the city
*    Time of last update
*    Current temperature
*    Morning temperature
*    Noon temperature
*    Evening temperature
*    Night temperature
*    Wind speed
*    Humidity

Built with FastAPI for high performance
Utilizes requests and BeautifulSoup for data retrieval and parsing

### Project Structure

*   City.py: Handles retrieval of city list and weather data.
*   Province.py: Manages weather data for provinces.
*   Country.py: Retrieves weather information for countries.
*    Main.py: The main script to run the program and start the FastAPI server.
## Installation
1. Clone the repository:
```bash
https://github.com/ALiEbrahimiir/Fast-Weather.git
```
2. Navigate to the project directory:
```bash
Cd Fast-Weather
```
3. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
4. Install the required packages:
```bash
pip install requests beautifulsoup4 "fastapi[standard]"
```

## Usage
1. Start the FastAPI server:
```bash
uvicorn Main:app --reload
or 
fastapi dev Main.py
```
Access the API endpoints in your browser or using a tool like curl or Postman:

*   For find Country name's : http://127.0.0.1:8000/weather/
*   for find province name's : http://127.0.0.1:8000/weather/{country_name}/
*   for find city name's : http://127.0.0.1:8000/weather/{country_name}/{province_name}/

#### Simple 
*   https://weather.town/forecast/united-states/california/los-angeles/


### Example API Response


    "city_name": "City Name",
    "last_update": "2024-08-12T14:00:00Z",
    "current_temperature": "25°C",
    "morning_temperature": "18°C",
    "noon_temperature": "25°C",
    "evening_temperature": "22°C",
    "night_temperature": "20°C",
    "wind_speed": "10 km/h",
    "humidity": "60%"


## Contributing

Contributions are always welcome!

    1.   Fork the repository
    2.   Create a new branch
    3.   Make your changes
    4.   Submit a pull request





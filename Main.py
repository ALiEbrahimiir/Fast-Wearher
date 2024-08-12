from fastapi import FastAPI
from bs4 import BeautifulSoup # type: ignore
import requests # type: ignore
import datetime
from Province import province # type: ignore
from Country import country # type: ignore
from City import city # type: ignore

app = FastAPI()

@app.get('/')
async def root():
    return {'Help': ''}

@app.get('/weather')
async def get_countries():
    locations = country()
    return {'Help': '', 'locations': locations}

@app.get('/weather/{cname}')
async def get_provinces(cname: str):
    locations = province(cname)
    return {'Help': '', 'locations': locations}

@app.get('/weather/{cname}/{pname}')
async def get_cities(cname: str, pname: str):
    locations = city(cname, pname)
    return {'Help': '', 'locations': locations}

@app.get('/weather/{cname}/{pname}/{tname}')
async def get_city_weather(cname: str, pname: str, tname: str):
    url = f'https://weather.town/forecast/{cname}/{pname}/{tname}/'
    
    try:
        http_url = requests.get(url).text
        soup = BeautifulSoup(http_url, 'html.parser')

        time = datetime.datetime.now()
        c_temp = soup.find(id="infTemperature").get_text(strip=True)
        Morning = soup.find(id='infTempMorning').get_text(strip=True)
        Day = soup.find(id='infTempDay').get_text(strip=True)
        Evening = soup.find(id='infTempEvening').get_text(strip=True)
        Night = soup.find(id='infTempNight').get_text(strip=True)
        wind = soup.find(id="windValue").get_text(strip=True)
        humidity = soup.find(id="humidityValue").get_text(strip=True)
        
        return {
            'نام شهر': tname,
            'زمان آخرین بروزرسانی': time,
            'دمای فعلی': c_temp,
            'دمای صبح': Morning,
            'دمای ظهر': Day,
            'دمای عصر': Evening,
            'دمای شب': Night,
            'سرعت باد': wind,
            'رطوبت': humidity
        }
    
    except Exception as e:
        return {'error': str(e)}

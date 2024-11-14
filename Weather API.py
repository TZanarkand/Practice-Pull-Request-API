import requests
import datetime

# https://openweathermap.org/

apikey = 'e95320a3af61de4afbd475614858c2cf'
city = input("Enter City: ")

url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}'

# ดึงข้อมูลจาก API
data = requests.get(url).json()

# สกัดข้อมูล 
weather_des = data['weather'][0]['description'] # description
temp = data['main']['temp'] - 273.15 # tranform Kelvin to Celsius 

# set date
# %y แสดง ค.ศ. 2 หลัก
# ถ้าไม่ได้ใช้ from datetime import datetime ต้องเขียนแบบด้านล่าง คือ datetime.datetime จะสื่อถึงการเรียก datetime (โมดูล) และเรียก datetime (คลาส)
today = datetime.datetime.now().strftime("%Y-%m-%d || %H:%M:%S")
um = datetime.datetime.now()

# output
print("-----------------------------")
print(today)
print(f'The weather in {city} is: {weather_des}')
print(f'The temperature in {city} is: {temp}')
print("-----------------------------")


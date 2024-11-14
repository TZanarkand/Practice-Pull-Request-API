import requests

# source from [ https://www.iqair.com/th-en/ ]
# มี API Collection ใน POSTMAN สามารถดูได้ว่ารองรับประเทศไหนบ้าง
apikey = 'c6c3d7a8-3957-441d-a4ec-80cf81cd418e'
city = 'Bangkok'
state = 'Bangkok'
country = 'Thailand'

url = f'http://api.airvisual.com/v2/city?city={city}&state={state}&country={country}&key={apikey}'

payload = {}
headers = {}

# optional -> data = requests.get(url).json()
response = requests.request("GET", url, headers=headers, data=payload)
data = response.json()

# exact data
pollution_aqi = data['data']['current']['pollution']['aqius']

print(str(pollution_aqi) + " AQI_TH")

# อ้างอิงระดับจาก [ https://www.researchgate.net/publication/358283929/figure/fig2/AS:1119451349041154@1643909408778/Air-quality-index-AQI.png ]
if pollution_aqi > 300:
    print("Air Pollution Level: Hazardous")

elif pollution_aqi >= 201:
    print("Air Pollution Level: Very Unhealthy")

elif pollution_aqi >= 151:
    print("Air Pollution Level: Unhealthy")

elif pollution_aqi >= 101:
    print("Air Pollution Level: Unhealthy for Sensitive Groups")

elif pollution_aqi >= 51:
    print("Air Pollution Level: Moderate")

else:
    print("Air Pollution Level: Good")
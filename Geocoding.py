from opencage.geocoder import OpenCageGeocode
import requests
# ลง pip3 install opencage ก่อน

### จาก IQAir
def get_pm(lat, lng):

    key = 'c6c3d7a8-3957-441d-a4ec-80cf81cd418e'
    url = f"http://api.airvisual.com/v2/nearest_city?lat={lat}&lon={lng}&key={key}"

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.json()
    pm = data['data']['current']['pollution']['aqius']
    return pm

### จาก OpenCage
# address = "888 21 หมู่ 3 Tambon Thung Suk La, Si Racha District, Chon Buri 20110"
def get_geocoding(address):

    key = 'f3755d0e27df4fddb44da7dffd9c1ac9'
    geocoder = OpenCageGeocode(key)

    results = geocoder.geocode(address)
    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']
    
    return lat, lng

# latitude, longitude = get_geocoding(address)
# print("Latitude:", latitude)
# print("Longitude:", longitude)

def main():
    # 888 21 หมู่ 3 Tambon Thung Suk La, Si Racha District, Chon Buri 20110
    # address = input()

    lat, lng = get_geocoding("888 21 หมู่ 3 Tambon Thung Suk La, Si Racha District, Chon Buri 20110")
    print(lat, lng)

    pm = get_pm(lat, lng)
    print("-------------------------")
    print(str(pm) + " AQI_TH")

    if pm > 300:
        print("Air Pollution Level: Hazardous")

    elif pm >= 201:
        print("Air Pollution Level: Very Unhealthy")

    elif pm >= 151:
        print("Air Pollution Level: Unhealthy")

    elif pm >= 101:
        print("Air Pollution Level: Unhealthy for Sensitive Groups")

    elif pm >= 51:
        print("Air Pollution Level: Moderate")

    else:
        print("Air Pollution Level: Good")

# เรียกใช้ main() ให้โค้ดทำงาน
if __name__ == "__main__":
    main()



# url  = f"https://api.opencagedata.com/geocode/v1/json?q={address}&key={key}"
#  address = "888 21 หมู่ 3 Tambon Thung Suk La, Si Racha District, Chon Buri 20110"

# response = requests.request("GET", url)

# data = response.json()

# geom = data['results'][0]['geometry']

# print(geom['lat'], geom['lng'])

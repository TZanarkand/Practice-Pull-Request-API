import requests

# https://newsapi.org/ 

country = input("Country: ")
print("Which category are you interested in?\n1. Business\n2. Entertainment\n3. General\n4. Health\n5. Science\n6. Technology")
category = input("Enter here: ")

# url_country = f'https://newsapi.org/v2/top-headlines/sources?country={country}&apiKey=14166acef7394826bf77d5325dea268f'
# url_category = f'https://newsapi.org/v2/top-headlines/sources?category={category}&apiKey=14166acef7394826bf77d5325dea268f'

# ใส่ api key ของตัวเอง
url = f'https://newsapi.org/v2/top-headlines?country={country}&category={category}&apiKey=14166acef7394826bf77d5325dea268f'

res = requests.get(url).json()

for i in range(3):
    news_from = res['articles'][i]['source']['name']
    title = res['articles'][i]['title']
    des = res['articles'][i]['description']
    more = res['articles'][i]['url']

    print("---------------")
    print("ข่าวจาก: " + news_from)
    print("หัวข้อข่าว: " + title)
    print("รายละเอียด: " + des)
    print("เพิ่มเติม: " + more)
    print("---------------")

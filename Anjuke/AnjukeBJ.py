import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
link = "https://beijing.anjuke.com/sale/p"

for i in range(1,11):
    r = requests.get(link + str(i),headers=headers)

    soup = BeautifulSoup(r.text, 'lxml')
    house_list = soup.find_all("li", class_='list-item')

    for house in house_list:
        name = house.find('div', class_='house-title').a.text.strip()
        price = house.find('span', class_='price-det').text.strip()
        price_area = house.find('span', class_='unit-price').text.strip()

        selector = house.find("div",class_='details-item')
        no_room = selector.span.text
        area = selector.contents[3].text
        floor = selector.contents[5].text
        year = selector.contents[7].text

        broker = house.find("span", class_="brokername").text
        broker = broker[1:]
        address = house.find("span", class_='comm-address')["title"]
        tag_list = house.find_all('span', class_='item-tags tag-others')
        tags = [i.text for i in tag_list]
        print(name, price, price_area, no_room, area, floor, year, broker, address, tags)

        filename = "AnjukeBJ" + ".txt"
        
        with open(filename, 'a+', encoding='utf-8') as f:
            f.write("%s \t %s \t %s \t %s \t %s \t %s \t %s \t %s \t %s \t %s \t \r\n"
                    % (name, price, price_area, no_room, area, floor, year, broker, address, tags))

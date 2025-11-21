import requests
from bs4 import BeautifulSoup

limit = int(input("Сколько токенов показать? "))
tokens =[]
total_pages = 49
base_url = "https://etherscan.io/tokens"
headers = {
            "User-Agent": (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/127.0.0.0 Safari/537.36"
            ),
            "Accept-Language": "en-US,en;q=0.9",
            }
for page in range(1, total_pages + 1):
    if page == 1:
        url = base_url
    else:
        url = f"{base_url}?p={page}"
    try:
        response = requests.get(url, headers=headers, timeout=10)
        
        
    except requests.exceptions.RequestException as e:
        print(e)
    soup = BeautifulSoup(response.text, 'html.parser')
    tbody = soup.find('tbody')
    rows = tbody.find_all("tr")
    for row in rows:
        cells = row.find_all("td")
        name_cell = cells[1].find('a')
        token_name = name_cell.find("div", class_='hash-tag').text.strip()
        token_url = "https://etherscan.io" + name_cell.get('href')
        price_cell = cells[3].find("div", class_ = 'd-inline').text.strip()
        token_price = float(price_cell[1:].replace(',', ''))
        tokens.append({
                        'name': token_name,
                        'price': token_price,
                        'url': token_url
                    })  
tokens_sorted = sorted(tokens, key=lambda x: x['price'], reverse=True) 
print(tokens_sorted[:limit])




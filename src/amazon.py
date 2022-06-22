import requests
from bs4 import BeautifulSoup


def search(query):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-GB,en;q=0.9',
        'device-memory': '8',
        'dnt': '1',
        'downlink': '10',
        'dpr': '1',
        'ect': '4g',
        'referer': 'https://www.amazon.co.uk/',
        'rtt': '50',
        'sec-ch-device-memory': '8',
        'sec-ch-dpr': '1',
        'sec-ch-viewport-width': '1920',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
        'viewport-width': '1920'
    }
    url = f'https://www.amazon.co.uk/gp/aw/s/ref=nb_sb_noss_1?k={query.replace(" ", "+")}'

    html = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(html.text, 'html.parser')
    item = soup.find_all('div', {'data-component-type': 's-search-result'})[0]

    data = {
        'title': item.find('h2', {'class': 'a-size-mini a-spacing-none a-color-base s-line-clamp-3'}).text,
        'price': item.find('span', {'class': 'a-offscreen'}).text,
        'img': item.find('img', {'class': 's-image'})['src'],
        'rating': item.find('div', {'class': 'a-row a-size-mini'}).find('span', {'class': 'a-icon-alt'}).text,
        'number_of_ratings': item.find('span', {'class': 'a-size-mini a-color-base s-light-weight-text'}).text,
        'url': item.find('a', {'title': 'product-detail'})['href'],
    }
    return data

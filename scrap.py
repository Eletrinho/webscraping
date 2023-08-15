from bs4 import BeautifulSoup 
import requests

def scrap():

    url = 'https://www.kabum.com.br/hardware/processadores/processador-amd?page_number=1&page_size=60&facet_filters=&sort=most_searched'
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}

    response = requests.get(url, headers=header)

    produtos = {}

    if response.status_code == 200:
        x = 61
        soup = BeautifulSoup(response.content, 'html.parser')
        todos = soup.find_all('div', attrs={'class': 'productCard'})
        for i in todos:
            # print(i)
            # print(i.find('a').find('img').get('alt')[0:30])
            prod = i.find('a').find_all('div')[1].find('span').string
            name = prod[:29]
            description = prod[31:]
            # print(name)
            preco = float(i.find('span', attrs={'class': 'priceCard'}).string[2:].replace('.', '').replace(',', '.'))
            # print(preco)
            # print('-------------------------')
            produtos[x] = [name, preco, description]
            x += 1
    else:
        print(response.status_code)

    return produtos

# p = scrap()
# print(scrap())
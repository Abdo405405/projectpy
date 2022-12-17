import requests
import bs4
counter = 0

url = f'https://web.vodafone.com.eg/en/stores-locations'
page = requests.get(url)

soup = bs4.BeautifulSoup(page.content, "html.parser")
funds = []



funds = soup.findAll('div', {'class': "card__content"})


for j in range(len(funds)):

        counter += 1

        funds.append(print(f'"Investment Funds :"  {funds[j].text}\n'))

        print()

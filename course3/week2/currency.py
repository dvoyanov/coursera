from bs4 import BeautifulSoup
from decimal import Decimal
import requests


def convert(amount, cur_from, cur_to, date, requests):
    response = requests.get("https://www.cbr.ru/scripts/XML_daily.asp?date_req="+date)  # Использовать переданный requests
    soup = BeautifulSoup(response.content, 'xml')
    valute_dic = {'RUR': (Decimal(1), 1)}
    for valute in soup.find_all("Valute"):
        valute_dic[valute.CharCode.string] = (Decimal(valute.Value.string.replace(',', '.')), int(valute.Nominal.string))
    result = amount * valute_dic[cur_from][0] * valute_dic[cur_to][1] / valute_dic[cur_from][1] / valute_dic[cur_to][0]
    return result.quantize(Decimal('.0001'))


if __name__ == "__main__":
    convert(Decimal("1000.1000"), 'RUR', 'JPY', "17/02/2005", requests)
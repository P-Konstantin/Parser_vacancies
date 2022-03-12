from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
import json


url = 'https://pythonworld.ru/vacancies'


def getData(url):
    try:
       html = urlopen(url)
    except HTTPError as e:
        return None
    except URLError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read())
        url_begin = 'https://pythonworld.ru'
        title_list = []
        link_list = []
        for child in bsObj.findAll('h2'):
            title_list.append(child.text)
            link_list.append(url_begin + child.a.get('href'))
            data = dict(zip(title_list, link_list))
    except AttributeError as e:
        return None
    return data


def saveData(data):
    with open('data.txt', 'w') as outfile:
        json.dump(data, outfile, ensure_ascii=False)


result = getData(url)
if result == None:
    print('Data could not be found')
else:
    saveData(result)



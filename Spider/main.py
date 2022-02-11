"""
从https://www.bbiquge.net/爬取小说
"""

import requests
from bs4 import BeautifulSoup


def get_soup(url_func):
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X '
                             '10_15_7) AppleWebKit/537.36 (HTML, '
                             'like Gecko) Chrome/92.0.4515.131 '
                             'Safari/537.36'}
    req = requests.get(url_func, headers=headers)
    req.encoding = req.apparent_encoding
    soup_func = BeautifulSoup(req.text, 'lxml')
    return soup_func


base_url = 'https://www.bbiquge.net/book_16/'
base_soup = get_soup(base_url)
char_list = base_soup.find('dl').find_all('a')
for i in range(1, 300):
    title = char_list[i].text
    href = char_list[i]['href']
    url = base_url + href
    soup = get_soup(url)
    content = soup.find('div', id='content')
    text = content.text.replace(" 笔趣阁 www.bbiquge.net，最快更新完美世界最新章节！     (《》)", '')
    text = text.replace("    ", '\n').replace(' ', '')
    text = text.replace("笔趣阁www.bbiquge.net，最快更新完美世界最新章节！", '')
    print('\n'+title+text)

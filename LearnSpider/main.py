# coding=utf-8
import requests  # 用来爬取网页
from bs4 import BeautifulSoup  # 用来解析网页

# 我们的种子
seds = ["https://www.ustc.edu.cn/"]
sum = 0
# 我们设定终止条件为：爬取到10000个页面时，就不玩了
while sum < 1000:
    if sum < len(seds):
        r = requests.get(seds[sum])
        sum = sum + 1
        soup = BeautifulSoup(r.content, 'lxml')
        with open('test.txt', 'w+') as f:
            f.write(r.content)
        urls = soup.find_all("href")  # 解析网页所有的链接
        for url in urls:
            seds.append(url)
    else:
        break


print sum

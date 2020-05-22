import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.ncyu.edu.tw/csie/itemize_list.aspx?site_content_sn=58775'
res = requests.get(url, timeout =130)
print(res)
soup = BeautifulSoup(res.text,'html.parser')

tags = soup.find_all('a',href=re.compile('sn=58775'), limit = 4)

for tag in tags[:]:
    print(tag.text)

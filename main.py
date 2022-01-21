
import requests
import csv
from bs4 import BeautifulSoup
from random import randint
from time import sleep

# URL = 'https://www.hackthebox.com/members?page='
#
# req = requests.get(URL,headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
# soup = BeautifulSoup(req.text, 'html.parser')
#
# pnames = soup.find_all('p', attrs={'class', 'font-size15 font-weight500 color-white mb-0'})
# pids = soup.find_all('p', attrs={'class', 'font-size13 line-height-18 mb-0'})
# pprourls = soup.find_all('a', attrs={'class', 'text-decoration-none'})
#
# print(pnames[0].text)
# print(pids[0].text)
# print(pprourls[0]['href'])
#
#
# data = [pnames[0].text,pids[0].text, pprourls[0]['href']]
#
# fields = ['pnames', 'pid', 'pprourls']
#
#
# with open('pinfo', 'w') as f:
#     write = csv.writer(f)
#
#     write.writerow(fields)
#     write.writerows([data])
fields = ['pnames', 'pid', 'pprourls']

for page in range(741, 926):
    x = randint(2, 8)
    print(f'Sleeping {x} seconds')
    sleep(x)

    URL = 'https://www.hackthebox.com/members?page='
    req = requests.get(URL + str(page) ,headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})

    soup = BeautifulSoup(req.text, 'html.parser')
    print(f'On Page {page}')

    pnames = soup.find_all('p', attrs={'class', 'font-size15 font-weight500 color-white mb-0'})
    pids = soup.find_all('p', attrs={'class', 'font-size13 line-height-18 mb-0'})
    pprourls = soup.find_all('a', attrs={'class', 'text-decoration-none'})
    data = []
    for i in range(0, 21):
        data.append([pnames[i].text,pids[i].text, pprourls[i]['href']])
    with open('pinfo', 'a', encoding='utf-8') as f:
        write = csv.writer(f)
        write.writerow("PAGE-" + str(page))
        write.writerows(data)
        print(f'Wrote Page {page}')
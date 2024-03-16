import pandas as pd
from bs4 import BeautifulSoup
import requests

root = 'https://www.timeout.com'
website ='https://www.timeout.com/film/best-movies-of-all-time'
result = requests.get(website)
content = result.text

soup = BeautifulSoup(content, 'lxml')
box = soup.find_all('article', class_='tile _article_kc5qn_1')
#print(movies)

links = []

for temp in box:
    ll = temp.find('a',href=True)
    links.append(ll)

ls = []
for link in links:
    if link['href'] != '/movies':
        ls.append(link['href'])

desc = []
for link in ls:
    website = root+link
    result = requests.get(website)
    content = result.text
    soup = BeautifulSoup(content, 'lxml')

    box = soup.find('div', id='content').get_text()
    desc.append(box)

df = {'link':ls, 'description':desc}
pd.DataFrame(df).to_csv('test.csv',index=False)


#
# mlist = []
# for movie in movies:
#     name = movie.find('h3').get_text()
#     mlist.append(name)
#
# with open('test.txt', 'w') as file:
#     for m in mlist:
#         file.write(m + '\n')



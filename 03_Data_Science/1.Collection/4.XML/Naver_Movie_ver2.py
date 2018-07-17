import os
import urllib.request
from bs4 import BeautifulSoup
from pandas import DataFrame

rank = 0
name_list = []
range_list = []
up_down_list = []

movie_list = []

html = urllib.request.urlopen('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=cnt&tg=0&date=20180709')
soup = BeautifulSoup(html, 'html.parser')


def create_dir():
    dir_name = "naver_ranking" + str(int(int(count) / 3 + 1))
    if os.path.isdir("V2_BigData/naver_ranking" + str(int(int(count) / 3 + 1))) is False:
        os.makedirs("V2_BigData/naver_ranking" + str(int(int(count) / 3 + 1)))
    return dir_name


def create_file():
    file_name = "movie" + str(int(count)+1) + ".csv"
    return file_name


if os.path.isdir("V2_Bigdata") is False:
    os.makedirs("V2_BigData")
if os.path.isdir("V2_BigData/naver_ranking1") is False:
    os.makedirs("V2_BigData/naver_ranking1")
if os.path.isfile("V2_BigData/naver_ranking1/.*") is False:
    file_name = "movie1.csv"
    count = 0

tbody = soup.find("tbody")
divs_movie = tbody.find_all('div')
imgs_movie = tbody.find_all('img', attrs={'class': 'arrow'})
range_ac_movie = tbody.find_all('td', attrs={'class': 'range ac'})

for num in range_ac_movie:
    up_down_range = num.attrs
    up_down_list.append(up_down_range.text)

for arrow in imgs_movie:
    range_movie = arrow.attrs
    range_list.append(range_movie["alt"])

for div in divs_movie:
    a_movie = div.find('a').text
    name_list.append(a_movie)

dir_list = []
file_list = []

result = {'rank': range(1, 51), 'name': name_list, 'range': range_list, 'up_down': up_down_list}
result_table = DataFrame(result, columns=['rank', 'name', 'range', 'up_down'])
result_table.to_csv("V2_BigData/%s/%s" % (create_dir(), create_file()), encoding="cp949", mode='w', index=False)
print(result_table)
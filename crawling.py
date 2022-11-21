import requests
from bs4 import BeautifulSoup

def get_movie():
    ret_list = []
    url = 'https://movie.naver.com/movie/sdb/rank/rmovie.naver'

    response = requests.get(url)

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        ul = soup.select_one('table.list_ranking')
        titles = ul.select('div > a')
        for rank, title in enumerate(titles):
            # print(f"{rank+1}위 {title.get_text()}")
            ret_list.append((rank+1, title.get_text()))
    else : 
        print(response.status_code)

    return ret_list
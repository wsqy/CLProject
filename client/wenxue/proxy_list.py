import re
import json
import datetime
import requests
from pyquery import PyQuery as pq

base_url = "https://t66y.com/thread0806.php?fid=20&page=1"
api_url = "http://123.206.210.196:8000/websites/1/categorys/2/articles/"


def transform_date(date_str):
    if '今天' in date_str:
        date_str = datetime.datetime.now()
    elif '昨天' in date_str:
        date_str = datetime.datetime.now() + datetime.timedelta(days=-1)
    elif date_str.startswith('20'):
        date_str =  datetime.datetime.strptime(date_str, "%Y-%m-%d")
    else:
        date_str = datetime.datetime.now()
    return date_str.date()


def transform_url(site=r'http://t66y.com', url=''):
    if url.startswith('http'):
        return url
    elif url.startswith(r'/'):
        return site + url
    else:
        return site + r'/' + url


def get_content(url):
    r = requests.get(url)
    r.encoding = 'gbk'
    return r.text

def analysis_data(r_text):
    d = pq(r_text)
    per_list = d.find('.tr3.t_one.tac').items()
    count = 0
    for per in per_list:
        if count > 20:
            return
        # print(per)
        # title
        title = per('.tal h3 a')
        title_name = title.text()
        title_href = transform_url(url=title.attr('href'))
        # 用户
        user = per('.bl')
        user_name = user.text()
        user_href = transform_url(url=user.attr('href'))
        user_info = {
            'name': user_name,
            'href': user_href
        }
        dic = {
            'title': title_name,
            'url': title_href,
            'author': json.dumps(user_info)
        }
        # 时间
        # time = transform_date(per('.f12 .s3').text())
        time = per('.f12 .s3').text()
        # if '今天' in time:
        #     print(title_name)
        #     r = requests.post(api_url, data=dic)
        #     print(r.status_code)
        # else:
        #     return
        count += 1
        r = requests.post(api_url, data=dic)
        print(r.status_code)
        if str(r.status_code) != '201':
            print(r.text)

r_text = get_content(base_url)
data = analysis_data(r_text)
print(data)

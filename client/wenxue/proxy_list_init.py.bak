import re
import json
import datetime
import requests
from pyquery import PyQuery as pq

base_url = "https://t66y.com/thread0806.php?fid=20&page="

proxies = {
    "http": "http://127.0.0.1:40573",
    "https": "http://127.0.0.1:40573",
}

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
    print(url)
    r = requests.get(url, proxies=proxies)
    r.encoding = 'gbk'
    return r.text

def analysis_data(r_text):
    d = pq(r_text)
    per_list = d.find('.tr3.t_one.tac').items()
    data_list = []
    for per in per_list:
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
        # 时间
        time = transform_date(per('.f12 .s3').text())

        dic = {
            'title': title_name,
            'url': title_href,
            'author': json.dumps(user_info)
        }
        data_list.append(dic)
    return data_list

# r_text = get_content(base_url + '1')
# data = analysis_data(r_text)
# print(data)

data_list = []
for i in range(1, 26):
    r_text = get_content(base_url + str(i))
    data_list.extend(analysis_data(r_text))

print(json.dumps(data_list))
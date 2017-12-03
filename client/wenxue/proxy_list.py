import requests

base_url = "https://t66y.com/thread0806.php?fid=20&page="

proxies = {
    "http": "http://127.0.0.1:40573",
    "https": "http://127.0.0.1:40573",
}

def get_content(url):
    r = requests.get(url, proxies=proxies)
    print(r.encoding)
    r.encoding = 'gbk'
    print(r.encoding)
    print(r.text)

get_content(base_url + '1')
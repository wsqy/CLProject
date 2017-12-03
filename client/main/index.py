import requests
proxies = {
    "http": "http://127.0.0.1:40573",
    "https": "http://127.0.0.1:40573",
}

r = requests.get('https://t66y.com/index.php', proxies=proxies)
r.encoding = 'gbk'
print(r.text)
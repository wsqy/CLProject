import json
import requests
url = "http://127.0.0.1:8000/websites/1/categorys/2/articles/"

with open('all_arc.json') as f:
    data_json = json.loads(f.read())
    print(len(data_json))
    r = requests.post(url, data=data_json[0])
    print(r.status_code)
    # for d in data_json:
    #     r = requests.post(url, data=d)
    #     print(r.status_code)
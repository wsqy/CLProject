import re
import requests
from pyquery import PyQuery as pq

other_url = "https://t66y.com/read.php?tid=%s&page=%s"
base_url = "https://t66y.com/htm_data/20/1712/2565732.html"
# base_url = "https://t66y.com/read.php?tid=2793716&page=2"
proxies = {
    "http": "http://127.0.0.1:40573",
    "https": "http://127.0.0.1:40573",
}

def analysis_data(f, r_text):
    data_list = []
    d = pq(r_text)
    # 查找楼层
    per_list = d.find('.t.t2').items()
    for per in per_list:
        # 解析回复正文
        con = per('.tpc_content').text()
        # 只有内容超过200 并且 不是针对某楼层的回复时才保存
        if len(con) > 200 and con.find('Quote') != '-1':
            # 解析是否包含章节名
            title = per('h4').text()

            post_text = per('.tr1').text()
            # 解析章节所在楼层
            lou_id = post_text[post_text.find('回'):][1:-1]
            if lou_id == '樓':
                lou_id = 0
            # 解析文章保存时间
            lou_time = re.search(r'Posted:(.*?) \| ', post_text).group(1)
            print(lou_time)
            data_list.append({
                'title': title,
                'con': con,
                'lou_id': lou_id,
                'lou_time': lou_time
            })
    return data_list

def get_content(url):
    print(url)
    r = requests.get(url, proxies=proxies)
    r.encoding = 'gbk'
    return r.text

def get_first_page(url):
    print('string...')
    # 网页请求
    r_text = get_content(url)
    d = pq(r_text)
    # 提取总页数
    total_page = d("#last").attr('href').split('=')[-1]
    print(total_page)

    # 文章的唯一id
    tid = url[-12:-5]

    # 解析文章名
    article_content = d.text()
    article_title = re.search(r'本頁主題: (.*?) ', article_content).group(1)
    # print(article_title)

    # 按文章名保存成txt
    f = open(article_title+'.txt', 'a+')

    # 写入第一页内容
    analysis_data(f, r_text)

    # 解析文章的后面的页面
    # for i in range(2, int(total_page)+1):
    #     analysis_data(f, get_content(other_url %(tid, str(i))))

    f.close()

get_first_page(base_url)
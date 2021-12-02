import datetime
import requests
from lxml import etree
from lxml.html import tostring
import re
# from pywchat import Sender
 
 
 
def get_url(url):
    # 抓取url
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36",
        "Host": "mrxwlb.com",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
    }
    date_time = (datetime.date.today() + datetime.timedelta(-1)).strftime("%Y-%#m-%#d").replace('-', '{}').format('年','月') + "日新闻联播文字版"
    
    url = url + "/{}".format(date_time)
    try:
        rsp = requests.get(url, headers=header, timeout=5)
        rsp.raise_for_status()
        rsp.encoding = rsp.apparent_encoding
        # print(rsp.text)
        return rsp.text
    except requests.RequestException as error:
        print(error)
 
 
def data_handle(data):
    # 提取标签中的html格式
    etr = etree.HTML(data)
    news_content = etr.xpath('//div[@class="posts-wrapper"]/article')[0]
 
    news_contens = tostring(news_content, encoding='utf-8').decode('utf-8')
    # print(news_contens)
    # print("*"*10)
    news_text = re.sub("————–<br>[\\s\\S]*", "", news_contens)
 
    # 增加对敏感字符的处理
    # news_text = re.sub('习近平', "习大大", news_text)
    #
    # print(news_text)

    # #设置企业微信发送消息
    # cid='ww8661fac8750ba9d9'
    # secret='vnkoEYUQ_QBpeJgbL1axWfkdO9QdcfcI9v6YG7eqzfY'
    # agentid=1000003
    # app = Sender(cid,secret,agentid)
    # app.send_text(news_text)

    #设置邮件推送
    with open('email.txt','w',encoding="utf-8") as f:
        f.write(news_text)
 
 


uri = "http://mrxwlb.com"
 
rsp = get_url(uri)
news_content = data_handle(rsp)




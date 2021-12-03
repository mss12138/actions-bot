import re
import requests
from lxml import etree
import time
# import yagmail
 
 
 
# 设置请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4651.0 Safari/537.36',
}
# 获取日期
timeStruct = time.localtime()
strTime = time.strftime("%Y%m%d", timeStruct)
str_time = int(strTime)-1    #  如果是上午8点以后推送的，括号外的“-1”要删除
 
# 获取新闻
def hq_news():
 
    news = []
    url = f'https://tv.cctv.com/lm/xwlb/day/{str_time}.shtml'
    response = requests.get(url, headers=headers)
    response.encoding = 'RGB'
    resp = response.text
    # print(resp)
    etr = etree.HTML(resp)
    # print(etr)
    titles = etr.xpath("//div[@class='title']/text()")
    # print(titles)
    hrefs = etr.xpath("//li/a/@href")
    for title, href in zip(titles, hrefs):
        news_response = requests.get(href, headers=headers)
        news_response.encoding = 'RGB'
        news_resp = news_response.text
        # print(news_resp)
        news_gz = '.*(<div class="cnt_bd"><!--repaste.body.begin-->.*?</div>).*'
        news_zw = re.findall(news_gz, news_resp)
        # print(news_zw)
        news_th = news_zw[0]
        # print(news_th)
        news.append(f"<font color='#000079'><b>{title}</b></font>\n{news_th}视频地址：{href}\n\n\n")
    # return news
    print(news)
 
# 邮箱推送
# def main(event, context):
#     username = 'xxxxxxxx@163.com'
#     password = 'xxxxxxxx'
#     yag = yagmail.SMTP(user=username, password=password, host='smtp.163.com', port=465)
#     content = hq_news()
#     yag.send(to=['xxxxxxxx@qq.com'], subject=f'{str_time}新闻联播推送', contents=content)
#     return '邮件发送成功'



if __name__=='__main__':
    a=hq_news()

'''
早报
早报地址：https://www.163.com/dy/media/T1603594732083.html
'''
import requests
from lxml import etree

def main():
    url="https://www.163.com/dy/media/T1603594732083.html"
    rsp=requests.get(url)
    html=etree.HTML(rsp.text)
    today_url=html.xpath("//h2[@class='media_article_title']/a/@href")[0]
    rsp=requests.get(today_url)
    html=etree.HTML(rsp.text)
    news_list=html.xpath("//div[@class='post_body']/p[2]//text()")
    news_list=news_list[1:]
    con=''
    for i in news_list[1:]:
        con=con+i
    #设置server酱微信推送
    # api = "https://sc.ftqq.com/SCT66142TZBrDGxwOIWErfCWnWV0z719x.send"
    title = news_list[0]
    print(title)
    # content = con
    # data = {
    # "text":title,
    # "desp":content
    # }
    # req = requests.post(api,data = data)

    #设计邮件推送
    with open('email.txt','w',encoding="utf-8") as f:
        f.write(con)    
    
if __name__ == "__main__":
    main()
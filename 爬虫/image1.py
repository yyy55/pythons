# https://www.jdlingyu.com/tag/少女
# https://www.bilibili.com/video/BV1qJ411S7F6?p=2&vd_source=713bcfe12546c14d7ca38c2cda87861a


import requests
import parsel

url = 'https://www.jdlingyu.com/tag/少女'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}

response = requests.get(url=url, headers=headers)
html_str = response.text
selector = parsel.Selector(html_str)
#解析到li标签，li标签可以循环
lis = selector.xpath('//div[@id="post-list"]/ul/li')
#循环li标签的所有参数
for li in lis:
    #获取标题和图片地址
    title = li.xpath('.//h2/a/text()').get()
    imgurl = li.xpath('.//h2/a/@href').get()
    #拿到图片地址后，再次请求图片地址
    response_pic = requests.get(url=imgurl, headers=headers).text
    selector_2 = parsel.Selector(response_pic)
    #获取所有图片地址
    pic_url_list = selector_2.xpath('//div[@class="entry-content"]/p/img/@src').getall()
    print(pic_url_list)
    #循环图片地址，下载图片
    for pic_url in pic_url_list:
        pic = requests.get(url=pic_url, headers=headers).content
        filename = pic_url.split('/')[-1]
        #保存图片
        with open("img/"+filename, 'wb') as f:
            f.write(pic)
            print(filename, '下载成功')
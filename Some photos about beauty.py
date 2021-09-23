import requests
import sys
import re
import parsel
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0'}
base_url = 'https://www.leshe.us/xz/twyh'
chongchongchong = requests.get(url = base_url, headers = header, verify= False)
html_data = chongchongchong.text
selector = parsel.Selector(html_data)
divs = selector.xpath('//div[@class="row posts-wrapper"]/div')
for div in divs:
    pic_title = div.xpath('.//h2/a/text()').get()
    pic_url = div.xpath('.//h2/a/@href').get()
    header_2 = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}
    chongchongchong_2 = requests.get(url= pic_url, verify= False).text
    selector_2 = parsel.Selector(chongchongchong_2)
    img_urls_list = selector_2.xpath('//div[@class="entry-content u-text-format u-clearfix"]//img/@data-srcset').getall()
    for img_url in img_urls_list:
        img_data = requests.get(url = img_url , headers= header_2, verify=False).content
        file_name = img_url.split('/')[-1]
        with open('TEST2(photo)\\' +   file_name , mode= 'wb') as f:
            f.write(img_data)
            print(pic_title, ' crawl successfull！')

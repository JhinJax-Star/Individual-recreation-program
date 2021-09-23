import requests
import re
import sys
url = 'http://www.b520.cc/0_7/'
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0'}
response = requests.get(url = url,headers=header)
response.encoding = response.apparent_encoding
html_data = response.text
result_list = re.findall('<dd><a href="(.*?)">(.*?)</a></dd>',html_data)
for chapter_url , title in result_list:
    all_url = chapter_url
    header_2 = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0'}
    response_2 = requests.get(url = all_url, headers = header_2)
    response_2.encoding = response_2.apparent_encoding
    html_data_2 = response_2.text
    result = re.findall('<p>　　(.*?)</p>',html_data_2)
    result = str(result).replace(u'\u3000',u' ')
    result = result.replace(' ','\n').replace("'","").replace('[','').replace(']','').replace(',','')
    with open('TEST1(novel)\\' + title + '.text' , mode = 'w' , encoding= 'utf-8') as f:  
        f.write(result)
        print('crawl successfull！：' , title)

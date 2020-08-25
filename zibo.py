import re
import urllib.request
import chardet

url="http://www.zibohuanghe.com/news.asp?classid=1&page=1"#输入参数为你想爬取的网页URL


headers = ("User-Agent"," Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
urllib.request.install_opener(opener)
data = urllib.request.urlopen(url).read().decode("utf-8")

mypatten="title=\".*\">(.*)</a></div></li>"
#<tr><td width="10" align="center"><img src="/images1/icon.png"/></td><td height="23" align="left"><a href="/ywyx/08/[0-9]+.shtml" target='_blank'>(.*)</a></td>
mylist=re.findall(mypatten,data)

for i in range(2,16):
    s="http://www.zibohuanghe.com/news.asp?classid=1&page="+str(i)
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen(s).read().decode("utf-8")


    mypatten = "title=\".*\">(.*)</a></div></li>"
    #class="text-overflow">(.*)</a><span style="color: rgb(93,93,93)
    mylist = mylist+re.findall(mypatten, data)
file=open('D:\codefile\huanghe\zibodata.txt','w')
file.write(str(mylist))
file.close()
print(mylist)
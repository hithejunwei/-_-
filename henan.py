import re
import urllib.request
import chardet

url="http://hnb.yrcc.gov.cn/zljj/index.jhtml"#输入参数为你想爬取的网页URL


headers = ("User-Agent"," Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
urllib.request.install_opener(opener)
data = urllib.request.urlopen(url).read().decode("utf-8")

mypatten="class=\"text-overflow\">(.*)</a><span style=\"color"
#<tr><td width="10" align="center"><img src="/images1/icon.png"/></td><td height="23" align="left"><a href="/ywyx/08/[0-9]+.shtml" target='_blank'>(.*)</a></td>
mylist=re.findall(mypatten,data)

for i in range(2,11):
    s="http://hnb.yrcc.gov.cn/zljj/index_"+str(i)+".jhtml"
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen(s).read().decode("utf-8")


    mypatten = "class=\"text-overflow\">(.*)</a><span style=\"color"
    #class="text-overflow">(.*)</a><span style="color: rgb(93,93,93)
    mylist = mylist+re.findall(mypatten, data)
file=open('D:\codefile\huanghe\henandata.txt','w')
file.write(str(mylist))
file.close()
print(mylist)
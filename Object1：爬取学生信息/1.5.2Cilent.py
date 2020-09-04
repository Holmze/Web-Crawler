import urllib.parse
import urllib.request
url = "http://127.0.0.1:5000"

try:
    html = urllib.request.urlopen(url)
    html = html.read()
    fileName = html.decode()
    print("准备下载："+fileName)
    data = urllib.request.urlopen(url+"?fileName="+urllib.parse.quote(fileName))
    data = data.read()
    fobj = open("download"+fileName,"wb")
    fobj.write(data)
    fobj.close()
    print("下载完成：",len(data),"字节")
    
except Exception as err:
    print(err)
import re
import requests
url = 'http://push2.eastmoney.com/api/qt/stock/get?ut=fa5fd1943c7b386f172d6893dbfba10b&invt=2&fltt=2&fields=f43,f57,f58,f169,f170,f46,f44,f51,f168,f47,f164,f163,f116,f60,f45,f52,f50,f48,f167,f117,f71,f161,f49,f530,f135,f136,f137,f138,f139,f141,f142,f144,f145,f147,f148,f140,f143,f146,f149,f55,f62,f162,f92,f173,f104,f105,f84,f85,f183,f184,f185,f186,f187,f188,f189,f190,f191,f192,f107,f111,f86,f177,f78,f110,f262,f263,f264,f267,f268,f250,f251,f252,f253,f254,f255,f256,f257,f258,f266,f269,f270,f271,f273,f274,f275,f127,f199,f128,f193,f196,f194,f195,f197,f80,f280,f281,f282,f284,f285,f286,f287,f292&secid=1.603103&cb=jQuery112409262947646562985_1601451983153&_=1601451983154'
json_page = requests.get(url).content.decode(encoding='utf-8')
pat = "\"data\":{.*}"
table = re.compile(pat,re.S).findall(json_page)
pat = ","
infs = re.split(pat,table[0])
pat = ':'
print("代码:"+str(re.split(pat,infs[11])[1]))
print("名称:"+str(re.split(pat,infs[12])[1]))
print("今开:"+str(re.split(pat,infs[3])[1]))
print("最高:"+str(re.split(pat,infs[1])[1]))
print("涨停:"+str(re.split(pat,infs[8])[1]))
print("换手:"+str(re.split(pat,infs[54])[1]+"%"))
print("成交量:"+str(re.split(pat,infs[4])[1]+"万手"))
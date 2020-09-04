import urllib.parse
import urllib.request
url = "http://127.0.0.1:5000"
note = "深圳xxxxx。这里四季如春xxxxx"

try:
    province = urllib.parse.quote("广东")
    city = urllib.parse.quote("深圳")
    note = "note="+urllib.parse.quote(note)
    param = "province="+province+"&city="+city
    
import re

reg = r"[A-Za-z0-9\._+]+@[A-Za-z0-9]+\.(com|org|edu|net)"
m = re.search(reg,"!!!!!!!!704062177)@qq.com chenlockholmze@gmail.com")
print(m)
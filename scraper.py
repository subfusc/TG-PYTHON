import urllib
import re 

url = "http://itavisen.no"
f = urllib.urlopen(url)
html = f.read()

reg = r'<img.*src="(.*?)".*/?>'
print re.findall(reg, html)

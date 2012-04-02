import urllib
import re 
import sys

url = sys.argv[1]
f = urllib.urlopen(url)
html = f.read()

reg = r'<img src="(.*?)".*/?>'
print re.findall(reg, html)

import urllib, re, os

page = urllib.urlopen('http://tg.ifi.uio.no/2012')

code = page.read()

bildeliste = re.findall('<img.*?src="(.*?.gif)".*?>', code)

print bildeliste

for bilde in bildeliste:
    urllib.urlretrieve(bilde, os.path.basename(bilde))

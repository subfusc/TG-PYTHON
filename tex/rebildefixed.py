import re

tekst = '<html><head><title>Digge studier ved UiO</title></head><body><h1>Studentliv ved UiO</h1><p>Det er mye digge studier ved UiO</p><img src="bilde.jpg" alt="bilde"></body></html>'

det_vi_leter_etter = r'<img.*?src="(.*?)".*?>'

resultat = re.findall(det_vi_leter_etter, tekst)
print resultat 

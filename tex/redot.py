import re

det_vi_leter_etter = "h..d" # Her er det vi leter etter

tekst = "det var en gang en hund som het Arne."
resultat = re.search(det_vi_leter_etter, tekst)

if resultat:
    print det_vi_leter_etter," finnes i teksten."
else:
    print det_vi_leter_etter," finnes ikke i teksten."


import re

# en tekst variabel som forteller
# oss hva vi leter etter.
det_vi_leter_etter = "hund"

# En tekst vi vil lete i.
tekst = "det var en gang en hund som het Arne."

# Fin alle muligheter.
resultat = re.findall(det_vi_leter_etter, tekst)

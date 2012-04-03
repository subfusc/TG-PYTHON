import re

# en tekst variabel som forteller
# oss hva vi leter etter.
det_vi_leter_etter = "hund"

# En tekst vi vil lete i.
tekst = "det var en gang en hund som het Arne."

# Let etter svar
resultat = re.search(det_vi_leter_etter, tekst)

# Hvis vi har funnet noe
if resultat: 
    # Sier vi at vi har funnet noe
    print det_vi_leter_etter + " finnes i teksten."

    # Hvis vi ikke har funnet noe
else:
    # Da sier vi at vi ikke har funnet noe
    print det_vi_leter_etter + " finnes ikke i teksten."


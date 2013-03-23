#!/usr/bin/env python
# -*- coding = utf8 -*-
# Det finnes mange versjoner av Python.
# I dette kurset etterstreber jeg å skrive kode som er kompatibel med 2.6 => 3.2

alder = input('Skriv inn din alder: ')

if alder >= 16:
    print 'Du kan komme inn på The Gathering selv om mamma sier nei!'
else:
    print 'Du må nok spørre mammaen din de neste ', 16 - alder, ' årene'

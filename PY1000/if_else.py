# coding=utf8
# Det finnes mange versjoner av Python.
# I dette kurset bruker jeg Python 2.7

alder = input('Skriv inn din alder: ')

if alder >= 16:
    print 'Du kan komme inn på The Gathering selv om mamma sier nei!'
else:
    print 'Du må nok spørre mammaen din de neste ', 16 - alder, ' årene'

from data import ar
from data import termekek
from data import dbszam 
from funcions import searchTermek 

termek = input('Keresés: ')
result = searchTermek(termek)
if result == False:
    print('Nincs ilyen termák.')
else:
    print(f'A termék ára: {ar[result]} Ft')
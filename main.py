from data import *
from funcions import *

termek = input('Keresés: ')
result = searchTermek(termek)
if result == False:
    print('Nincs ilyen termék.')
else: 
    print(f'A termék ára: {ar[result]} Ft')
from data import *
from re import I 


def searchTermek(needle):
    for i,termek in enumerate(termekek):
        if needle == termek:
            return i
    return False

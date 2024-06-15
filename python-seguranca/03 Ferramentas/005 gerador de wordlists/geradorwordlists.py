import itertools

import os
os.system('cls') or None

string = input("String a ser permutada: ")

resultado = itertools.permutations(string, len(string))

for i in resultado:
    print(''.join(i))

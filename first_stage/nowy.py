lista = ['fdadsf','dfsa','ss','s','daadaf','s' ]
slownik = {}
for el in lista:
    if not el in slownik:
        slownik[len(el)] = 1
    else:
        slownik[len(el)] += 1


for key in slownik:
    print(key)
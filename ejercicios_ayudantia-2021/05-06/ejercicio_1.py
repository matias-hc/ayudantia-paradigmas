#!/usr/bin/env python3

## para poder comparar strings de tal forma que por ejemplo se cumpla
## "a < B < c < D" (ignorar si es mayuscula) se compara con la key str.lower para
## que las letras mayusculas al momento de comparacion valgan igual que las minusculas
dic = {"abc" : 4, "casa" : 16, "ceramica" : 5, "LCC" : 3, "zebra" : 7}

### ordenar por valor de la llave

## usando el comprension de listas que itera sobre las llaves ordenadas
#ld_byKey = [(k, dic[k]) for k in sorted(dic,key=str.lower)]

## pasando a lista las tuplas llave/valor del metodo items() de diccionario, y ordenandola posteriormente
ld_byKey = sorted(list(dic.items()), key=lambda tup : str.lower(tup[0]))

### ordenar por valor de los item 'valor' del diccionario

## usando el comprension de listas que itera sobre las llaves ordenadas con respecto a los valores correspondientes
#ld_byVal = [(k, dic[k]) for k in sorted(dic,key=lambda k : dic[k])]

ld_byVal = sorted(list(dic.items()), key=lambda tup : tup[1])

print(ld_byKey)
print(ld_byVal)

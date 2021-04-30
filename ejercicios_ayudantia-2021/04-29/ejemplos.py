#!/usr/bin/env python3

print("Tuplas:")
tup = (1 , 2)
print("{} = {}".format("tup", tup))
print("iterando:")
for v in tup:
    print(v)


print("\nListas:")
lis = [0, 2, 4, 6]
print("{} = {}".format("lis", lis))
lis.append(11)
print("{}.append({})".format("lis", lis[-1]))
print("iterando(v//2, v%2):")
for v in lis:
    print(v//2, v%2)


print("\nFunciones:")
def funp(value):
    while value > 0:
        yield value
        value -= 1
    else:
        return 0
print("def funp(value):" + '\n' + "    while value > 0:" + '\n' + "        yield value" + '\n' + "        value -= 1" + '\n' + "    else:" + '\n' + "        return 0"
)
print("iterando sobre funp(5):")
for v in funp(5):
    print("funp: " + str(v+1))


print("\nLista de funciones:")
lisf = [lambda x, y: x**3 + 1, lambda x, y: x**2 + y, lambda x, y: x + y**2, lambda x, y: 1 + y**3]
print("{} = {}".format("lisf", "[lambda x, y: x**3 + 1, lambda x, y: x**2 + y, lambda x, y: x + y**2, lambda x, y: 1 + y**3]"))
print("iterando:")
for i in range(len(lisf)):
    print("{}[{}]({},{}) = {}".format("lisf", i, 2, 3, lisf[i](2,3)))


print("\nStrings:")
st = "hola"
print("{} = {}".format("st", '\"'+st+'\"'))
print("iterando:")
for c in st:
    print("letra {}".format(c))


print("\nconjuntos:")
try:
    myset = { "algo", 4 , [1, 2] }
    for e in myset:
        print("{}".format(e))
    print("{} = {}".format("myset", myset))
except TypeError as E:
    print("{} = {}".format("myset", "{ \"algo\", 4 , [1, 2] }"))
    print("TypeError:", E)
    print("A las listas, los conjuntos y los diccionarios no se les puede hacer hahsing pero las tuplas si"
          '\n' + "pero cabe destacar que es una propiedad recursiva, una tupla con listas tampoco sirve"
          )
myset2 = { "algo", 4 , (1, 2)}
print("{} = {}".format("myset2", myset2))
print("iterando:")
for e in myset2:
    print("{} {}".format(e, type(e)))


print("\ndiccionarios:")
try:
    dic = { "algo" : 111, 4 : 1111, [1, 2] : 11111}
    for e in dic:
        print("{}".format(e))
    print("{} = {}".format("dic", dic))
except TypeError as E:
    print("{} = {}".format("dic", "{ \"algo\" : 111, 4 : 1111, [1, 2] : 11111}"))
    print("TypeError:", E)
    print("Las llaves de los diccionarios deben ser hashable al igual que los miembros de un conjunto")
dic2 = { "llave1" : "valor1"
        , 2 : 32
        , 4 : "cabello"
        , "9" : 48
        }
print("{} = {}".format("dic2", dic2))
print("iterando:")
for k in dic2:
    print("dic2[{}] = {}".format(k, dic2[k]))

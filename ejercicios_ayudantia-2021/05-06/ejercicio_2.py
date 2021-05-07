#!/usr/bin/env python3
LD = ["Kz3UuwTG", 23, "duGkCWzB", 12,
      "qju7TM5M", "4XnEE9ZJ", 46, "WAk0BSv4",
      32, 14, "76HBLSP8", "IBUs3PZf",
      16, 100, "amMnAkZW", "2jSRNUzD",
      0, 23, "rYBe8CYl", 22]

def mergesort_type(L):
    if (largo := len(L)) <= 1:
        return dict([(type(x), [x]) for x in L])
    else:
        return merge_type(mergesort_type(L[:(largo//2)]), mergesort_type(L[(largo//2):]))

def merge_type(d1, d2):
    D = dict()
    for t in set(list(d1.keys())+list(d2.keys())):
        if t in d1 and t in d2:
            D[t] = merge(d1[t], d2[t])
        elif t in d1:
            D[t] = d1[t]
        elif t in d2:
            D[t] = d2[t]
    return D

def merge(l1, l2):
    L=[]
    while True :
        if (len(l1) == 0):
            L += l2
            break
        if (len(l2) == 0):
            L += l1
            break
        if (l1[0] < l2[0]):
            L.append(l1[0])
            l1 = l1[1:]
        else:
            L.append(l2[0])
            l2 = l2[1:]
    return L



def merge_add(D,l):
    for obj in l:
        if (tp:=type(obj)) in D:
            D[tp].append(obj)
        else:
            D[tp] = [obj]

print(mergesort_type(LD))

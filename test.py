# for i in [2,1,5]:
#     print(i)

# smallest = None
# print("Before:", smallest)
# for itervar in [3, 41, 12, 9, 74, 15]:
#     if smallest is None or itervar < smallest:
#         smallest = itervar
#         break
#     print("Loop:", itervar, smallest)
# print("Smallest:", smallest)

# print(0 is 0.0)

# for n in "banana":
#     print(n)

# word = "bananana"
# i = word.find("na")
# print(i)

# words = 'His e-mail is q-lar@freecodecamp.org'
# pieces = words.split()
# print(pieces)
# parts = pieces[3].split('-')
# print(parts)
# n = parts[1]
# print(n)

# dict = {"Fri": 20, "Thu": 6, "Sat": 1}
# dict["Thu"] = 13
# dict["Sat"] = 2
# dict["Sun"] = 9
# print(dict)

# counts = {'quincy' : 1 , 'mrugesh' : 42, 'beau': 100, '0': 10}
# print(counts.get('kris', 0))

# counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
# for key in counts:
#     if counts[key] > 10:
#         print(key, counts[key])

# d = dict()
# d['quincy'] = 1
# d['beau'] = 5
# d['kris'] = 9
# for (k,i) in d.items():
#     print(k, i)

# counts = {'quincy' : 1 , 'mrugesh' : 42, 'beau': 100, '0': 10}
# lst = []
# for key, val in counts.items():
#     newtup = (val, key)
#     lst.append(newtup)
# lst = sorted(lst, reverse=True)
# print(lst)
#
#
# print( sorted( [ (v,k) for k,v in counts.items() ], reverse=True ) )

# print( [ (k,v) for k,v in counts.items().sorted() ] )

# print( [ (k,v) for k,v in counts.values().sort() ] )

# import re
# s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
# # Соответствие непробельной строке + @ + непробельная строка
# lst = re.findall('\\S+@\\S+', s)
# print(lst)

import urllib.request
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())
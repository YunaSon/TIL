from collections import ChainMap

a = {1 : "python", 2 : "data science" }
b = {3 : "java script", 4 : "web"}
c = {1 : "hi", 2 : "hello"}
d = {3: "korea", 4: "america", 5: "china", 6 : "japan"}
h = [1,2,3,4,5,6,7]
k = "Hello World"

a1 = ChainMap(a, b)
a2 = ChainMap(a, c)
a3 = ChainMap(a, d)
a4 = ChainMap(a, b, c, d)
a5 = ChainMap(a, h, k)

print(a1)
print(a2)
print(a3)
print(a4)
print(a5)
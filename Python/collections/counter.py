from collections import Counter

a = [1, 2, 1, 1, 4, 2, 3, 4, 6, 4, 3, 2, 1, 6, 3, 4, 4, 3, 8]
b = ["hi", "HI", "Hello", "hello", "korea", "text", "my", "name", "Name"]

c = Counter(a)
d = Counter(b)

print(c)
print(d)

b1 = " ".join(b)
b1 = b1.lower()
b = b1.split(" ")

d = Counter(b)
print(d)

print(list(c.elements()))
print(list(d.elements()))
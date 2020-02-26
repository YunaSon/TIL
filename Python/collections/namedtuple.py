from collections import namedtuple

a = namedtuple('course', 'name, technology')
s = a('data science', 'python')
k = a._make(['artificial intelligence', 'python'])


print(a)
print(s)
print(k)
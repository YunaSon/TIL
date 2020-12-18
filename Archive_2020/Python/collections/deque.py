from collections import deque

a = ['e', 'd', 'u', 'r', 'e', 'k', 'a']
d = deque(a)

d.appendleft('python')

print(d)

d.popleft()
print(d)

d.rotate(3)
print(d)
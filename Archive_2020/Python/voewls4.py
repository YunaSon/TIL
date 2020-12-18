vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Provid a word to search for vowels: ")

found = {}
found['a'] = 0
found['e'] = 0
found['i'] = 0
found['o'] = 0
found['u'] = 0

for letter in word:
    if letter in vowels:
        found[letter] += 1 
#found['a'] = 0을 설정 안해주면 key에러가 남! vowels리스트 안의 원소와 비교하기 때문!!
for k,v in sorted(found.items()):
    print(k, 'was found', v,'time(s).')
person3 = {'Name': 'Ford prefect',
            'Gender': 'Male',
            'Occupation': 'Researcher',
            'Home Planet': 'Betelgeuse Seven'}

found ={'o':0, 'u':0, 'a':0, 'i':0, 'e':0}

#빈도수 갱신하기
found['e'] = found['e'] + 1
found['a'] += 1

print(found)

#딕셔너리 반복하기
for i in found:
    print(found[i])

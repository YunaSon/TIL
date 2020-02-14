phrase = "Don't panic!"
plist = list(phrase)
print("phrase: ", phrase)
print("plist: ", plist)

for i in range(4):
    plist.pop()

plist.remove("'")
plist.pop(0)
plist.extend([plist.pop(), plist.pop()])
#plist.extend([i for i in range(2): plist.pop()]) 안됨
plist.insert(2,plist.pop(3))

new_phrase =''.join(plist)
print("plist: ", plist)
print("new_phrase: ",new_phrase)



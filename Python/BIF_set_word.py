word = set('aeiou')
#text = input('input the words: ')
#result = word.intersection(set(text))
#results = [i for i in result]
#results.sort()
#print(results)

def search_vowels(text:str):
    word = set('aeiou')
    result = word.intersection(set(text))
    print(result)


#search_vowels('hello')


def search_vowels_v2(text:str, word:str = 'aeiou'):
    texts = set(text)
    result = texts.intersection(set(word))
    print(result)

search_vowels_v2('galaxy','g')


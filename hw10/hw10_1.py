import re
def text():
    text = input('text: ')
    words = []
    for word in re.findall(r'\b\w+', text.lower()):
        words.append(word)
    
    words_count = {}
    for word in words:
        words_count[word] = words.count(word)
    
    print(words)
    print(words_count)
    print(len(words))

text()
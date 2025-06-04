import re

sample_text = 'The sun dipped below the horizon, painting the sky in hues of orange and pink. A gentle breeze rustled the leaves, and the world grew quieter, preparing for nightfall.'

def last3():
    text = input('text: ')
    if not text.strip():
        text = sample_text
    pattern = r'\w{3}\b'
    result = re.findall(pattern, text)
    print(result)

last3()
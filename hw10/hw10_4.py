import re

sample_text = 'The sun shines brightly, and the sky is blue. Birds are singing, and the trees are rustling. The sun rises higher and higher.'

result = re.findall(r'\w+\b', sample_text)
print(f'words count: {len(result)}')

result = set(result)
print(f'unique words: {result}')
print(f'unique words count: {len(result)}')
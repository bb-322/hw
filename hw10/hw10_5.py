import re
import json
import random

sample_text = 'Smith John, born on 2001-07-15, email: john.smith@example.com, feedback: Great course, I learned a lot!'
sample_text2 = 'Doe Jane | 1998/12/03 | jane.doe98@mail.com | The course was very informative and well-structured.'
sample_text3 = 'Brown Michael - Date of Birth: 2000.07.22 - Email: michael.brown@edu.org - Feedback: I enjoyed the course, especially the hands-on projects.'
sample_text4 = 'Taylor Emily; born: 1995-11-30; contact: emily_taylor95@university.net; feedback: Excellent content and clear explanations.'
sample_texts = [sample_text, sample_text2, sample_text3, sample_text4]

pattern = r'([\w ]+).+(\d{4}\W\d{2}\W\d{2}).+ (.+[.]?@\w+.\w+)\W+[A-z]+?\W+(.+)'

text = input('text: ')
if not text.strip():
    text = random.choice(sample_texts)

for data_item in re.findall(pattern, text):
    data = {
        'full name': data_item[0],
        'birth date': data_item[1],
        'email': data_item[2],
        'feedback': data_item[3]
    }

with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)
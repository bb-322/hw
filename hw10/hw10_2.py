import os
import json
import re

path = os.path.join(os.path.dirname(__file__), 'task2.log')

with open(path, 'r') as f:
    data = f.read()

pattern = r"(\d{4}-\d{2}-\d{2})\s+((\d{2}:?){3})\s+-\s+[A-Z]+\s+-\s+(.+)"
log_groups = re.findall(pattern, data)

new_data = []

for item in log_groups:
    data_item = {
        'date': item[0],
        'time': item[1],
        'type': item[2],
        'message': item[3]
    }
    new_data.append(data_item)

with open('data.json', 'w') as f:
    json.dump(new_data, f, indent=4)
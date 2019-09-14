import json
from app import label

filename = 'test.json'

text = "# Title\n## Subtitle\n1) List one\n2) List two\n3) List three\n- List point one\n- list point two\n* Definition\n"

print(text)

label(text)

with open(filename, 'w+') as f:
	json.dump(label(text), f)
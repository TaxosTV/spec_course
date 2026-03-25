import re

text = input()

pattern = r'\b(20\d{2})-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])\s(0\d|1\d|2[0-3]):([0-5]\d):([0-5]\d)\b'

matches = re.finditer(pattern, text)

for match in matches:
    print(match.group())
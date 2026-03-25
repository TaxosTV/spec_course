import re

text = input()

pattern = r'[A-Za-z0-9+_#-]+@[A-Za-z0-9]+\.[A-Za-z]+'

emails = re.findall(pattern, text)

for email in emails:
    print(email)
import re

url = '''
https://towardsdatascience.com
https://www.youtube.com
https://mail.google.com
'''

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

matches = pattern.finditer(url)

for match in matches:
    print(match.group(4))

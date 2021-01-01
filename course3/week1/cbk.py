import requests
import re

result = requests.get("http://cbr.ru")
html = result.text
print(html)
match = re.search(r'_euro..EUR*?[\s\S]*?(\d+,\d+)', html)
rate = match.group(1)
print(rate)


import re

s = input().lower()
print(f'.{".".join(re.sub("[aeiuoy]+", "", s))}')

import re


s = input()
regexp = re.compile(r'(?<=[^aeiou])[aeiou]{2,}(?=[^aeiou])', flags=re.IGNORECASE)
m = re.findall(regexp, s)

[print(i) for i in m] if m else print("-1")

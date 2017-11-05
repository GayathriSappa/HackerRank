import re


s = input()
regexp = re.compile(r'[,.]+')
string_split = [i for i in re.split(regexp, s) if len(i) > 0]
for i in string_split:
    print(i)

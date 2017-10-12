s = input()
xs = {i.lower() for i in s if i.isalpha()}
print('pangram' if len(xs) == 26 else 'not pangram')

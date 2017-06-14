S = input()

s = sorted(S)

is_lower = list(filter(lambda x: x.islower(), s))
is_upper = list(filter(lambda x: x.isupper(), s))
is_odd_digit = list(filter(lambda x: x if x.isdigit() and int(x) % 2 == 1 else None, s))
is_even_digit = list(filter(lambda x: x if x.isdigit() and int(x) % 2 == 0 else None, s))
result = is_lower + is_upper + is_odd_digit + is_even_digit
print(*result, sep='')

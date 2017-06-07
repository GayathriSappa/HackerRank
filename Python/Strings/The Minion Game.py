def minion_game(string):
    # your code goes here
    a = s.strip().lower()
    v = sum([len(a) - i for i,c in enumerate(a) if c in 'aeiou'])
    c = sum([len(a) - i for i,c in enumerate(a) if c not in 'aeiou'])

    if (v == c):
        print('Draw')
    else:
        print('Stuart {}'.format(c)) if c > v else print('Kevin {}'.format(v))

if __name__ == '__main__':
    s = input()
    minion_game(s)

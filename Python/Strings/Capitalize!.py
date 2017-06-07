def capitalize(string):
    s = [i.capitalize() for i in string.split(' ')]
    return ' '.join(s)

if __name__ == '__main__':
    string = input()
    capitalized_string = capitalize(string)
    print(capitalized_string)

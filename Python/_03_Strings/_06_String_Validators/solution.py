if __name__ == '__main__':
    s = input()
    print('True') if len([i for i in s if i.isalnum()]) > 0 else print('False')
    print('True') if len([i for i in s if i.isalpha()]) > 0 else print('False')
    print('True') if len([i for i in s if i.isdigit()]) > 0 else print('False')
    print('True') if len([i for i in s if i.islower()]) > 0 else print('False')
    print('True') if len([i for i in s if i.isupper()]) > 0 else print('False')
 

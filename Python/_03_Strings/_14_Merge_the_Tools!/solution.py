import textwrap


def merge_the_tools(string, k):
    # your code goes here
    for substring in textwrap.wrap(string, k):
        word = []
        [word.append(i) for i in substring if i not in word]
        print(''.join(word))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

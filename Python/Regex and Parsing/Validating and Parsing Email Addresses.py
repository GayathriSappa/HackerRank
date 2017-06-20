import re
import email.utils


n = int(input())
regexp = re.compile(r'^[a-zA-Z][\w.\-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$')
for i in range(n):
    name, address = email.utils.parseaddr(input())

    m = re.search(regexp, address)
    if m:
        valid = email.utils.formataddr((name, address))
        print(valid)

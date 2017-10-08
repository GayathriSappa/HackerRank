#!/bin/python3

import sys
from datetime import date, timedelta


def solve(year):
    # Complete this function
    if year == 1918:
        difference = timedelta(days=268)
    elif year in (1700, 1800, 1900):
        difference = timedelta(days=254)
    else:
        difference = timedelta(days=255)
    d = date(year, 1, 1) + difference
    return d.strftime('%d.%m.%Y')

year = int(input().strip())
result = solve(year)
print(result)

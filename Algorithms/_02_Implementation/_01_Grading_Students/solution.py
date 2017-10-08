#!/bin/python3

import sys


def solve(grades):
    # Complete this function
    result = []
    for grade in grades:
        if grade < 38:
            result.append(grade)
        else:
            a, b = grade // 10, grade % 10
            if b > 5:
                if (a * 10 + 10) - grade < 3:
                    result.append(a * 10 + 10)
                else:
                    result.append(grade)
            elif b < 5:
                if (a * 10 + 5) - grade < 3:
                    result.append(a * 10 + 5)
                else:
                    result.append(grade)
            else:
                result.append(grade)
    return result

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
    grades_t = int(input().strip())
    grades.append(grades_t)
result = solve(grades)
print("\n".join(map(str, result)))

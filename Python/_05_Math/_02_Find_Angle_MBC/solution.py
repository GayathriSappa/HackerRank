import math

AB = int(input())
BC = int(input())

AC = math.sqrt(pow(AB, 2) + pow(BC, 2))
M = 0.5 * math.sqrt(2*pow(BC, 2) + 2 * pow(AB, 2) - pow(AC, 2))

r = math.acos((pow(M, 2) + pow(BC, 2) - pow(AC / 2, 2)) / (2 * M * BC))
print(str(round(math.degrees(r)))+'\xB0')

if __name__ == '__main__':
    students = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        scores.append(score)

    n = []
    [n.append(i) for i in scores if i not in n]
    n.sort()
    students.sort()
    [print(i[0]) for i in students if i[1] == n[1]]

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    for k, v in student_marks.items():
        if k == query_name:
            average = sum(student_marks[k])/len(student_marks[k])
            print('%0.2f' % average)  

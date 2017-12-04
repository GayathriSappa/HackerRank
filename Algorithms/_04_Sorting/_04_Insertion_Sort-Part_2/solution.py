def insertion_sort(sequence):
    for j in range(1, len(sequence)):
        i = j - 1
        while i >= 0 and sequence[i] > sequence[i + 1]:
            sequence[i], sequence[i + 1] = sequence[i + 1], sequence[i]
            i -= 1
        print(' '.join(map(str, sequence)))
    return sequence


s = int(input())
ar = [int(i) for i in input().split()]

insertion_sort(ar)

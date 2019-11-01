def selection_sort(lyst):
    i = 0
    while i < len(lyst) - 1:
        min_index = i
        j = i + 1
        while j < len(lyst):
            if lyst[j] < lyst[min_index]:
                min_index = j
            j += 1
        if min_index != i:
            swap(lyst, min_index, i)
        i += 1


def swap(a, b, c):
    temp = a[b]
    a[b] = a[c]
    a[c] = temp


ly = [23, 232, 212, 21212, 53, 22]

selection_sort(ly)
print(ly)



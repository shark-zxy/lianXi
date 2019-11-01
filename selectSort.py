def select_sort(lis):
    length = len(lis)
    i = 0
    for i in range(i, length):
        j = i + 1
        for j in range(j, length):
            if lis[j] < lis[i]:
                lis[i], lis[j] = lis[j], lis[i]


li = [3, 4, 2, 1, 5]

select_sort(li)

print(li)

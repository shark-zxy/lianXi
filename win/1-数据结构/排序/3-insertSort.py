#coding :utf-8


def insertSort(alist):
    n = len(alist)
    for j in range(1, n):
        i = j
        while i > 0:
            if alist[i] < alist[i-1]:
                alist[i], alist[i-1] = alist[i-1], alist[i]
                i -= 1
            else:
                break


if __name__ == "__main__":
    list = [13, 32, 56, 32, 34, 56, 23, 43, 87, 12, 3, 1, 2]
    print(list)
    insertSort(list)
    print(list)

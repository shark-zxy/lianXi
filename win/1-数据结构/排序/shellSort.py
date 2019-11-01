# coding: utf-8

def shellSort(aList):
    n = len(aList)
    gap = n // 2

    while gap >= 1:
        for j in range(gap, n):
            i = j
            while i > gap:
                if aList[i] < aList[i-gap]:
                    aList[i],aList[i-gap] = aList[i-gap],aList[i]
                    i -= gap
                else:
                    break
        gap //= 2


if __name__ == "__main__":
    list = [13, 32, 56, 32, 34, 56, 23, 43, 87, 12, 3, 1, 2]
    print(list)
    shellSort(list)
    print(list)

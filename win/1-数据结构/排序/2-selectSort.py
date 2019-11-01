# coding :"utf-8"


def selectSort(aList):
    n = len(aList)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if aList[min_index] > aList[j]:
                min_index = j
        aList[i], aList[min_index] = aList[min_index], aList[i]


if __name__ == "__main__":
    list = [13, 32, 56, 32, 34, 56, 23, 43, 87, 12, 3, 1, 2]
    print(list)
    selectSort(list)
    print(list)

#coding :utf-8

def mergeSort(aList):
    n = len(aList)
    if n <= 1 :
        return aList
    mid = n // 2

    left_li = mergeSort(aList[:mid])

    right_li = mergeSort(aList[mid:])

    left_pointer,right_pointer = (0,0)
    result = []

    while left_pointer < len(left_li) and right_pointer < len(right_li):
        if left_li[left_pointer] < right_li[right_pointer]:
            result.append(left_li[left_pointer])
            left_pointer += 1
        else:
            result.append(right_li[right_pointer])
            right_pointer += 1

    result += left_li[left_pointer:]
    result += right_li[right_pointer:]
    return result


if __name__ == "__main__":
    list = [13, 32, 56, 32, 34, 56, 23, 43, 87, 13, 12, 3, 1, 2]
    print(list)
    sock = mergeSort(list)
    print(sock)

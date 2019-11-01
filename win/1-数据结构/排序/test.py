#coding :utf-8

def merge_sort(aList):
    n = len(aList)
    if n <= 1:
        return aList
    mid = n // 2

    left_list = merge_sort(aList[:mid])
    right_list = merge_sort(aList[mid:])

    left_pointer,right_pointer = (0,0)
    result = []

    while left_pointer < len(left_list) and right_pointer < len(right_list):
        if left_list[left_pointer] < right_list[right_pointer]:
            result.append(left_list[left_pointer])
            left_pointer += 1
        else:
            result.append(right_list[right_pointer])
            right_pointer += 1

    result += left_list[left_pointer]
    result += right_list[right_pointer]

    return  result

def quick_sort(aList, first, last):
    if first >= last:
        return
    mid_value = aList[first]
    low = first
    high = last

    while low < high:
        while low < high and aList[high] > mid_value:
            high -= 1
        aList[low] = aList[high]
        while low < high and aList[low] <= mid_value:
            low += 1
        aList[high] = aList[low]

    aList[low] = mid_value

    quick_sort(aList, first, low-1)
    quick_sort(aList, low+1, high)

def insert_sort(aList):
    n = len(aList)
    for j in range(1,n):
        i = j
        while i < 0:
            if aList[i] < aList[i-1]:
                aList[i],aList[i-1] = aList[i-1],aList[i]
                i -= 1
            else:
                break


def shell_sort(aList):
    n = len(aList)
    gap = n // 2
    for j in range(gap,n):
        i = j
        while i < gap:
            if  aList[i] < aList[i - gap]:
                aList[i],aList[i-gap] = aList[i-gap],aList[i]
                i -= gap
            else:
                break
        gap //= 2



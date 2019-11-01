#coding :utf-8

def quickSort(aList, first, last):
    if first >= last:
        return
    mid_value = aList[first]
    low = first
    high = last
    # while high >low:
    #     if aList[high] > mid_value:
    #         high -= 1
    #     elif aList[high] < mid_value:
    #         aList[low] = aList[high]
    #         low += 1
    #     if aList[low] > mid_value:
    #         aList[high] = aList[low]
    #         high -= 1
    #     elif aList[low] < mid_value:
    #         low += 1
    while low < high:
        while low < high and aList[high] > mid_value:
            high -= 1
        aList[low] = aList[high]
        while low < high and aList[low] <= mid_value:
            low += 1
        aList[high] = aList[low]
    aList[low] = mid_value

    quickSort(aList, low+1, last)
    quickSort(aList, first, low-1)


if __name__ == "__main__":
    list = [13, 32, 56, 32, 34, 56, 23, 43, 87, 13, 12, 3, 1, 2]
    print(list)
    quickSort(list, 0, len(list)-1)
    print(list)





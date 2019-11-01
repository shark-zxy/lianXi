def quicksort(lyst):
    quicksorthelper(lyst, 0, len(lyst) - 1)


def quicksorthelper(lyst, left, right):
    if left < right:
        pivotlocation = partition(lyst, left, right)
        quicksorthelper(lyst, left, pivotlocation-1)
        quicksorthelper(lyst, pivotlocation+1, right)


def partition(lyst, left, right):
    middle = (left + right) // 2
    pivot = lyst[middle]
    lyst[middle] = lyst[right]
    lyst[right] = pivot
    boundary = left
    for index in range(left, right):
        if lyst[index] < pivot:
            lyst[index], lyst[boundary] = lyst[boundary], lyst[index]
            boundary += 1
    lyst[right], lyst[boundary] = lyst[boundary], lyst[right]
    return boundary


li = [3, 2, 12, 4, 67, 3, 22, 43, 23]
quicksort(li)
print(li)

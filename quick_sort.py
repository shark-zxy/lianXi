# def quick_sort(lyst, first, last):
#     if first >= last:
#         return -1
#     left = first
#     right = last
#     mid_value = lyst[first]
#     while left < right:
#         while lyst[left] < mid_value and left < right:
#             left += 1
#         lyst[right] = lyst[left]
#         while lyst[right] >= mid_value and left < right:
#             right -= 1
#         lyst[left] = lyst[right]
#     mid_value, lyst[right] = lyst[right], mid_value
#     quick_sort(lyst, first, left-1)
#     quick_sort(lyst, left+1, last)


# li = [1, 67, 34, 23, 82432, 21, 323, 67, 23, 232, 323, 232323, 2, 45]
#
# quick_sort(li, 0, len(li)-1)
#
# print(li)


def quick_sort(list, first, last):
    if first >= last:
        return
    left = first
    right = last
    mid_value = list[left]

    while left < right:
        while left < right and list[left] < mid_value:
            left += 1
        list[right] = list[left]
        while left < right and list[right] >= mid_value:
            right -= 1
        list[left] = list[right]
    mid_value, list[right] = list[right], mid_value
    quick_sort(list, first, left-1)
    quick_sort(list, left+1, last)


li = [1, 67, 34, 23, 82432, 21, 323, 67, 23, 232, 323, 232323, 2, 45]

quick_sort(li, 0, len(li) - 1)

print(li)

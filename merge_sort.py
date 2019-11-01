
def merge_sort(lyst):
    n = len(lyst)
    if n <= 1:
        return lyst
    mid = n // 2

    lyst_left = merge_sort(lyst[:mid])
    lyst_right = merge_sort(lyst[mid:])
    left_pointer, right_pointer = 0, 0
    result = []
    while left_pointer < len(lyst_left) and right_pointer < len(lyst_right):
        if lyst_left[left_pointer] < lyst_right[right_pointer]:
            result.append(lyst_left[left_pointer])
            left_pointer += 1
        else:
            result.append(lyst_right[right_pointer])
            right_pointer += 1

    result += lyst_left[left_pointer:]
    result += lyst_right[right_pointer:]
    return result


li = [3, 2, 1, 34, 22, 655, 323, 3, 2, 2]

argv = merge_sort(li)

print(argv)






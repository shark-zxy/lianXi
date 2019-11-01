# coding :utf-8


def DoubleSort(alist):
    n = len(alist)
    for i in range(n-1):
        count = 0
        for j in range(n-1-i):
            if alist[j] > alist[j+1]:
                """第一种交换方法"""
                """alist[j],alist[j+1] = alist[j+1],alist[j]"""
                """第二种交换方法"""
                alist[j] = alist[j]+alist[j+1]
                alist[j+1] = alist[j]-alist[j+1]
                alist[j] = alist[j]-alist[j+1]
                count += 1
        """count得作用是用来检测若不发生交换，则跳出循环，降低时间复杂度"""
        if count == 0:
            break


if __name__ == "__main__":
    alist = [1,3,56,43,54,7,23,43,5,32,2]
    print(alist)
    DoubleSort(alist)
    print(alist)

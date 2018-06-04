'''

Description:
6. 合并排序数组 II
合并两个排序的整数数组A和B变成一个新的数组。
样例
给出A=[1,2,3,4]，B=[2,4,5,6]，返回 [1,2,2,3,4,4,5,6]
挑战
你能否优化你的算法，如果其中一个数组很大而另一个数组很小？

Method:
如果考虑从前往后插入的话，后面的数组还要移位，这时可以考虑从后面往前面安排。
另外用python的话记得要先给list A append一定的位数，否则index会超出范围。

'''


def mergeSortedArray(A, B):
    # write your code here
    m = len(A)
    n = len(B)
    k = m+n-1
    A = A + ([0]*n)
    # print (A)
    while (k>=0):
        if (m==0):
            A[k] = B[n-1]
            n = n-1
            k = k-1
        elif (n==0):
            A[k] = A[m-1]
            m = m-1
            k = k-1
        elif (A[m-1]>=B[n-1]):
            A[k] = A[m-1]
            m = m-1
            k = k-1
        else:
            A[k] = B[n-1]
            n = n-1
            k = k-1
    return A


if __name__ == '__main__':
    A = [1,3,7,23]
    B = [4,5,6,7,8]
    A = mergeSortedArray(A,B)
    print (A)


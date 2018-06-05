'''

Description:
28. 搜索二维矩阵
写出一个高效的算法来搜索 m × n矩阵中的值。
这个矩阵具有以下特性：

每行中的整数从左到右是排序的。
每行的第一个数大于上一行的最后一个整数。
样例

考虑下列矩阵：

[
  [1, 3, 5, 7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
给出 target = 3，返回 true

挑战

O(log(n) + log(m)) 时间复杂度

'''

# 从每行的最后一个数来看。
class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if(len(matrix) == 0):
            return False
        for i in range(0,len(matrix)):
            if (matrix[i][-1] == target):
                return True
            if (matrix[i][-1] > target):
                break
        for j in range(0,len(matrix[i])):
            if (matrix[i][j] == target):
                return True
        return False


# 二分查找的方法，这里要特别注意下标的处理
class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if (len(matrix)==0):
            return False
        row = len(matrix)
        col = len(matrix[0])
        length = row * col
        left = 0
        right = length - 1 # 这里不是length
        while(left<=right):
            mid = left + (right-left)//2
            print (mid)
            num = matrix[mid//col][mid%col]
            if (num == target):
                return True
            elif (num > target):
                right = mid - 1
            else:
                left = mid + 1
        return False



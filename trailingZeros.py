'''

Description:
2. 尾部的零
设计一个算法，计算出n阶乘中尾部零的个数。

Method:
本来想的是遍历1~n，然后看每个数最多是5的多少指数倍，但是这样的时间复杂度至少就是O(n)了，题目要求是O(logN)的复杂度。
于是根据res = N//5 + N//25 + N//125 + ... 以此类推，看从1~N贡献的5的次数。

'''



class Solution:
    """
    @param: n: An integer
    @return: An integer, denote the number of trailing zeros in n!
    """
    def trailingZeros(self, n):
        # write your code here, try to do it without arithmetic operators.
        res = 0
        i = 1
        while (n>=(5**i)):
            res = res + n // (5**i)
            i = i + 1
        return res
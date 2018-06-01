'''

Description:
4. 丑数②
设计一个算法，找出只含素因子2，3，5 的第 n 小的数。
符合条件的数如：1, 2, 3, 4, 5, 6, 8, 9, 10, 12...
如果n = 9， 返回 10
要求时间复杂度为O(nlogn)或者O(n)

Method:
任何一个丑数都是2^i * 3^j * 5^m这种形式的，因此不断寻找丑数，将他们按从小到大的顺序进行排列，直到第n个即为结果。
注意1一开始就放在了list中，所以到n-1即可。
注意2，3，5的倍数有重复的，所以当重复时，每一个num2,num3,num5都要+1

'''


class Solution:
    """
    @param n: An integer
    @return: the nth prime number as description.
    """
    def nthUglyNumber(self, n):
        # write your code here
        ugly = []
        ugly.append(1)
        num2 = num3 = num5 = 0
        for i in range(0,n-1):
        	res = min(ugly[num2]*2, ugly[num3]*3, ugly[num5]*5)
        	ugly.append(res)
        	if (res%2 == 0):
        		num2 += 1
        	if (res%3 == 0):
        		num3 += 1
        	if (res%5 == 0):
        		num5 += 1
        return ugly[-1]


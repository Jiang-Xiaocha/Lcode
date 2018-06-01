'''

Description:
3. 统计数字
计算数字k在0到n中的出现的次数，k可能是0~9的一个值。
例如n=12，k=1，在 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]，我们发现1出现了5次 (1, 10, 11, 12)

Method:
关键就是：
当某一位的数字小于k时，那么该位出现k的次数为：更高位数字x当前位数；
当某一位的数字等于i时，那么该位出现i的次数为：更高位数字x当前位数+低位数字+1；
当某一位的数字大于i时，那么该位出现i的次数为：(更高位数字+1)x当前位数。

其中0是特殊情况，当k=0时，
因为最高位的数字不可能是0，所以上述三种情况的 更高位数字*当前位数 都要变成 （更高位数字-1）*当前位数，也就是代码中的higher--
当计算到倒数第二位时，即higher==0时，直接res++也就是加上0这一情况便可，其他同上述是一样的。

分析可以参照：https://www.jianshu.com/p/ad6ad2118c02

'''


# 263ms
class Solution {
public:
    /*
     * @param : An integer
     * @param : An integer
     * @return: An integer denote the count of digit k in 1..n
     */
    int digitCounts(int k, int n) {
        // write your code here
        int current=0;
        int higher=0;
        int lower=0;
        int i=1;
        int res=0;
        if (n==0 && k==0)
        	return 1;
        while((n/i) != 0){
        	higher = n / (i*10);
        	current = (n/i) % 10;
        	lower = n-(n/i * i);
        	if (k==0){
        		if (higher == 0){
        			res++;
        			break;
        		}
        		else
        			higher--;
        	}
        	if (current < k)
        		res = res + higher * i;
        	if (current == k)
        		res = res + higher * i + lower + 1;
        	if (current > k)
        		res = res + (higher + 1) * i;
        	i = i*10;
        }
        return res;
    }
};


# 466ms
class Solution {
public:
    /*
     * param k : As description.
     * param n : As description.
     * return: How many k's between 0 and n.
     */
    int digitCounts(int k, int n) {
        // write your code here
        int count = 0 , x;
        if (k == 0 && n == 0) count = 1;
        for (int i = 1;x = n / i;i *= 10) {
            int high = x / 10;
            if (k == 0) {
                if (high) high--;
                else {
                    count++;
                    break;
                }
            }
            count += high * i;
            int current = x % 10;
            if (current > k) count += i;
            else if (current == k) count += n - x * i + 1;
        }
        return count;
    }
};
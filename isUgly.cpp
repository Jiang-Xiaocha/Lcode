'''

Description:
517. 丑数
写一个程序来检测一个整数是不是丑数。
丑数的定义是，只包含质因子 2, 3, 5 的正整数。比如 6, 8 就是丑数，但是 14 不是丑数以为他包含了质因子 7。
可以认为 1 是一个特殊的丑数。

Method:
注意是正整数。


'''

# 最典型的方法
class Solution {
public:
    /**
     * @param num: An integer
     * @return: true if num is an ugly number or false
     */
    bool isUgly(int num) {
        // write your code here
        if (num <= 0) return false;
        if (num == 1) return true;
          
        while (num % 2 == 0) num /= 2;
        while (num % 3 == 0) num /= 3;
        while (num % 5 == 0) num /= 5;
          
        return num == 1;
    }
};



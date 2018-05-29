'''

Description:
1. A + B 问题
给出两个整数a和b,求他们的和,但不能使用+等数学运算符。

Method:
主要分开来考虑进位与不进位的两个和，然后使用递归或者循环。
本来想用python写的，但用了python才发现python的左移机制和传统意义上的是不同的，这样对于负数会出现问题，就用了C++，
但可以考虑python实现一下传统意义上的左移右移？

'''


class Solution {  
public:  
    /* 
     * @param a: The first integer 
     * @param b: The second integer 
     * @return: The sum of a and b 
     */  
    int aplusb(int a, int b) {  
        // write your code here, try to do it without arithmetic operators.  
        if ((a&b) == 0)
            return a^b;
        else
            return aplusb(a^b,(a&b)<<1);
    }  
}; 
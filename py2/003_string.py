#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/2 16:36
# @Author  : Scheaven
# @File    : 003_string.py
# @description: 
'''
python 2
题目描述
对于一个字符串，我们想通过添加字符的方式使得新的字符串整体变成回文串，但是只能在原串的结尾添加字符，请返回在结尾添加的最短字符串。

给定原字符串A及它的长度n，请返回添加的字符串。保证原串不是回文串。

测试样例：
"ab",2
返回："a"
'''

class Palindrome:
    def addToPalindrome(self, A, n):
        i = 0
        while i < n :
            if A+A[i::-1]==( A+A[i::-1] )[::-1]:
                return A[i::-1]
            i += 1

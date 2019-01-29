#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
python 2
题目描述
一只袋鼠要从河这边跳到河对岸，河很宽，但是河中间打了很多桩子，每隔一米就有一个，每个桩子上都有一个弹簧，袋鼠跳到弹簧上就可以跳的更远。每个弹簧力量不同，用一个数字代表它的力量，如果弹簧力量为5，就代表袋鼠下一跳最多能够跳5米，如果为0，就会陷进去无法继续跳跃。河流一共N米宽，袋鼠初始位置就在第一个弹簧上面，要跳到最后一个弹簧之后就算过河了，给定每个弹簧的力量，求袋鼠最少需要多少跳能够到达对岸。如果无法到达输出-1

输入描述:
输入分两行，第一行是数组长度N (1 ≤ N ≤ 10000)，第二行是每一项的值，用空格分隔。
输出描述:
输出最少的跳数，无法到达输出-1

示例1
输入
5
2 0 1 1 1

输出
4

算法思想：
curr用于记录当前所跳跃所能达到的最大距离 max(curr, i+list[i])。 i+list[i]为i位置跳跃后落到的位置。
lastdis 为每次跳跃后所能降落的位置
jumpcount 为跳跃的次数

"""

n = int(raw_input())
list = [int(x) for x in raw_input().split()]
curr = 0
lastdis = 0
jumpcount = 0
list.append(1)
a = len(list)
for i in range(a):
    if curr < i:  # 如果所能达到的索引位置小于当前的索引表示无法达到i
        print '-1'
        exit()
    if i > lastdis: # 当当前索引位置大于上次降落的位置时跳跃一次并更新降落位置
        lastdis = curr
        jumpcount += 1
    curr = max(curr, i+list[i]) # 相当于取上一个跳跃索引i到本次索引之间跳跃后降落的最大值
if lastdis >= n:
    print jumpcount
else:
    print '-1'

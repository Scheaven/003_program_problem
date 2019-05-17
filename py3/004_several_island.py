#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/19 15:50
# @Author  : Scheaven
# @File    : 004_several_island.py
# @description:
# https://www.nowcoder.com/practice/1ecd3d9e09664cde94919b65ea06b47c?tpId=90&tqId=30919&tPage=1&rp=1&ru=/ta/2018test&qru=/ta/2018test/question-ranking
# 算法思想： 如果新输入的行和列没有与之前输入的相连接，则岛的个数加1，上下左右每连接一个位置岛的个数减一

if __name__ == '__main__':
    m = int(input())
    n = int(input())
    k = int(input())
    island_list = []
    result = ""
    curr_count = 0
    for i in range(k):
        row, col = input().split(" ")
        if [int(row), int(col)] in island_list or int(row)>=m or int(col) >= n:
            result += " " + str(curr_count)
        else:
            curr_count += 1
            if [int(row)-1, int(col)] in island_list:
                curr_count -= 1
            if [int(row)+1, int(col)] in island_list:
                curr_count -= 1
            if [int(row), int(col)-1] in island_list:
                curr_count -= 1
            if [int(row), int(col)+1] in island_list:
                curr_count -= 1
            island_list.append([int(row), int(col)])
            if curr_count <= 0:
                curr_count = 1
            result += " " + str(curr_count)
    print(result.strip())




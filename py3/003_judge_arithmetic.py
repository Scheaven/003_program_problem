#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/6 14:28
# @Author  : Scheaven
# @File    : 003_judge_arithmetic.py
# @description: https://www.nowcoder.com/practice/e11bc3a213d24fc1989b21a7c8b50c3f?tpId=90&tqId=30781&tPage=1&rp=1&ru=/ta/2018test&qru=/ta/2018test/question-ranking

# 算法思想：先排序，再计算差值是否相等


def judge_arithmetic(len_n, str_sequence):
    se_list = []
    for item in str_sequence:
        se_list.append(int(item))
    se_list.sort()
    d = se_list[1] - se_list[0]
    for i in range(len_n):
        if i*d != se_list[i] - se_list[0]:
            print("Impossible")
            return
    print("Possible")



if __name__ == '__main__':
    n = int(input())
    sequence_list = input().split(" ")
    judge_arithmetic(n, sequence_list)



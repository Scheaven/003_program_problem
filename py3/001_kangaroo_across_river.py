#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/24 17:32
# @Author  : Scheaven
# @File    : kangaroo_across_river.py
# @description:
'''
https://www.nowcoder.com/practice/74acf832651e45bd9e059c59bc6e1cbf?tpId=85&tqId=29892&tPage=1&rp=1&ru=/ta/2017test&qru=/ta/2017test/question-ranking

算法思想：
    感觉题的理解稍微有些偏差，解题的思想是站在第一个桩子上开始跳。感觉属于贪心算法。
    如果所站立的桩子的索引号为i，并且弹力为j,j不为0，则下一跳跳的范围为[i+1,i+j]
    获取的跳跃的列表List中索引为[i+1,i+j]，所以选择落下的那个桩为索引值加上桩子上的数字跳的最大的那个桩（索引号为j+List[j]）。
    重复以上跳跃，一直到落地的桩子索引大于n。
'''


def greedy_across_river(ori_index, des_index, n, j_list, k):
    TF = True
    if des_index > n:
        return k

    max_jump = ori_index
    for jump_index in range(ori_index, des_index):
        if int(j_list[jump_index]) != 0:
            TF = False
        if max_jump + int(j_list[max_jump]) < int(jump_index) + int(j_list[jump_index]):
            max_jump = int(jump_index)

    if TF :
        return -1

    if int(j_list[max_jump]) == 0:
        ori_index = max_jump + 2
    else: ori_index = max_jump + 1
    k += 1

    # ori_index = max_jump + 1
    des_index = max_jump + 1 + int(j_list[max_jump])

    print(ori_index , des_index)
    return greedy_across_river(ori_index, des_index, n, j_list, k)


if __name__ == '__main__':
    N = int(input())
    jump_list = input().split(" ")

    jump_count = 0
    origin_index = destination_index = 0
    print(origin_index, destination_index+1)
    jump_count = greedy_across_river(origin_index, destination_index+1, N, jump_list, jump_count)
    print(jump_count)


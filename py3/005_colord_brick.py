#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/6 15:31
# @Author  : Scheaven
# @File    : 005_colord_brick.py
# @description: https://www.nowcoder.com/practice/8c29f4d1bea84d6ba2847e079b7420f7?tpId=90&tqId=30780&tPage=1&rp=1&ru=/ta/2018test&qru=/ta/2018test/question-ranking


if __name__ == '__main__':
    number_bricks = input()
    brick_dic = {}
    for brick in number_bricks:
        if brick in brick_dic:
            brick_dic[brick] += 1
        else:
            brick_dic[brick] = 1



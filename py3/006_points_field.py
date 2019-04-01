#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/14 14:45
# @Author  : Scheaven
# @File    : 006_points_field.py
# @description: https://www.nowcoder.com/practice/fe30a13b5fb84b339cb6cb3f70dca699?tpId=85&tqId=29833&tPage=1&rp=1&ru=/ta/2017test&qru=/ta/2017test/question-ranking
'''
算法思想：
评价：该题是我碰到过的最难的一道题
更具题意：需要是要切出的16块地中的最小价值的地块的值A的最最大；
最粗暴的思想是穷举法，即只要能横竖切四刀的方式都穷举出来。然而时间复杂度为O(n^4).是不可能的情况。
思考拆分：
得到的值一定在最小值Min，到16块的均值avg之间即区间[min,avg]
横切采用穷举法，即先横着切三刀
竖着切的时候保证每切一刀切好的部分的值都大于最小值min小于均值avg
如果没有满足的情况则缩小区间，即增加min,或减小avg
等区间缩小为小值大于大值时，则输出结果


'''

N, M = map(int, input().split())
mat = [[int(c) for c in input().strip()] for i in range(N)]

left = min([min(m) for m in mat])
right = sum([sum(m) for m in mat]) // 16 + 1
# sum grid from (x0,y0) to (x1,y1)
sums_ = [[0] * (M + 1) for i in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, M + 1):
        sums_[i][j] = sums_[i - 1][j] + sums_[i][j - 1] - sums_[i - 1][j - 1] + mat[i - 1][j - 1]


def sum_grid(x0, y0, x1, y1, mat):
    return sums_[x1][y1] + sums_[x0][y0] - sums_[x0][y1] - sums_[x1][y0]


def judge(mat, N, M, val):
    for r1 in range(1, N - 2):
        if sum_grid(0, 0, r1, M, mat) < 4 * val: continue
        for r2 in range(r1 + 1, N - 1):
            if sum_grid(r1, 0, r2, M, mat) < 4 * val: continue
            for r3 in range(r2 + 1, N):
                if sum_grid(r2, 0, r3, M, mat) < 4 * val: continue
                if sum_grid(r3, 0, N, M, mat) < 4 * val: continue
                start, count = 0, 0
                for i in range(1, M + 1):
                    if sum_grid(0, start, r1, i, mat) >= val \
                            and sum_grid(r1, start, r2, i, mat) >= val \
                            and sum_grid(r2, start, r3, i, mat) >= val \
                            and sum_grid(r3, start, N, i, mat) >= val:
                        start, count = i, count + 1
                        if count == 4:
                            return True
    return False


while left < right:
    mid = (left + right) // 2
    state = judge(mat, N, M, mid)
    if state:
        left = mid + 1
    else:
        right = mid
print(right - 1)


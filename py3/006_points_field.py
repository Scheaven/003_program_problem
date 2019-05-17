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


# 获取累加矩阵：新的矩阵中的每个元素为以该元素为右下角的子矩阵的所有元素的和即Y[i,j] = sum(mat[0:i,0:j]);
def get_submat_sum(M, N, mat):
    submat_sum = [[0]*(M + 1) for i in range(N + 1)]  # 初始化所有初始信息为0
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            # 计算公式D=C+B-A+a
            submat_sum[i][j] = submat_sum[i][j-1] + submat_sum[i-1][j] - submat_sum[i-1][j-1] + mat[i-1][j-1]
    return submat_sum


# 计算所分配的区域内的数据信息和:mat之所以没有用是因为之前计算过了submat的和
def sum_grid(x0, y0, x1, y1, mat_sum):
    return mat_sum[x1][y1] - mat_sum[x1][y0] - mat_sum[x0][y1] + mat_sum[x0][y0]


# 判断切割方式是否满足要求
def sect_judge(submat_sum, N, M, val):
    for row_seg1 in range(1, N - 2):
        if sum_grid(0, 0, row_seg1, M, submat_sum) < 4*val: continue
        for row_seg2 in range( row_seg1+1, N - 1):
            if sum_grid(row_seg1, 0, row_seg2, M, submat_sum) < 4 * val:continue
            for row_seg3 in range(row_seg2+1, N):
                if sum_grid(row_seg2,0,row_seg3,M ,submat_sum) <4 * val:continue
                if sum_grid(row_seg3,0,N, M, submat_sum) < 4 * val:continue
                ######### 以上竖切割的四部分的和都符合要求######
                # 在竖切分的基础上进行横向切分，确保每一部分都符合要求
                col_seg,seg_count = 0,0
                for i in range(1,M + 1):
                    if sum_grid(0,col_seg,row_seg1,i,submat_sum) >= val \
                            and sum_grid(row_seg1,col_seg,row_seg2,i,submat_sum) >= val \
                            and sum_grid(row_seg2,col_seg,row_seg3,i,submat_sum) >= val \
                            and sum_grid(row_seg3,col_seg,N,i,submat_sum) >= val:
                        col_seg = i
                        seg_count += 1
                        if seg_count == 4:
                            return True
    return False

if __name__ == '__main__':
    N, M = map(int, input().split())
    mat = [[int(a) for a in input().strip()] for i in range(N)]  # 将获得数据存储在矩阵之中
    section_left = min([min(m) for m in mat])  # 即牛牛可能得到的最小值
    section_right = sum([sum(m) for m in mat]) // 16 + 1  # 即牛牛可能得到的最大值
    submat_sum = get_submat_sum(M, N, mat)

    while section_left < section_right:
        section_mid = (section_left + section_right) // 2
        sect_state = sect_judge(submat_sum, N, M, section_mid)
        if sect_state:
            section_left = section_mid + 1
        else:
            section_right = section_mid

    print(section_right-1)

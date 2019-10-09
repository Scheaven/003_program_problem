#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/9 11:15
# @Author  : Scheaven
# @File    :  010_rotate_matrix.py
# @description: 旋转矩阵：将一个二维矩阵进行旋转
# 算法思想： 如果是正方矩阵，行列相等，相对简单，矩阵大小为N*M
#           原字母a(i,j)旋转后的位置是a(j,M-1-i)
#           旋转时从左到右，从上到下围绕圆心依次填充。所以一共四个循环
import numpy as np

def rotate_matrix(ori_arr):
    print("ori_arr::", ori_arr)
    row, col = ori_arr.shape
    new_arr = np.zeros((col, row))
    point_count = 0
    round_count = 0
    while point_count < row*col:
        row_x, col_y = round_count, round_count
        print("=============")
        while col_y < row - round_count:
            new_arr[row_x, col_y] = ori_arr[row - 1 - col_y, row_x]
            point_count += 1
            col_y += 1
        col_y -= 1
        print("01",new_arr,point_count)

        if point_count > row*col:
            break

        row_x += 1
        while row_x < col - round_count:
            new_arr[row_x,col_y] = ori_arr[row - 1 - col_y, row_x]
            point_count += 1
            row_x += 1
        row_x -= 1

        print("02", new_arr, point_count)
        if point_count > row*col:
            break

        col_y -= 1
        while col_y >= round_count:
            new_arr[row_x, col_y] = ori_arr[row - 1 - col_y, row_x]
            point_count += 1
            col_y -= 1
        col_y += 1
        print("03", new_arr, point_count)

        if point_count >= row*col:
            break
        row_x -= 1
        while row_x > round_count:
            new_arr[row_x, col_y] = ori_arr[row - 1 - col_y, row_x]
            point_count += 1
            row_x -= 1
        print("04", new_arr, point_count)
        round_count += 1
if __name__ == '__main__':
    ori_arr = np.zeros((3,10))
    for i in range(ori_arr.shape[0]*ori_arr.shape[1]):
        ori_arr[i//ori_arr.shape[1], i%ori_arr.shape[1]] = i
    rotate_matrix(ori_arr)
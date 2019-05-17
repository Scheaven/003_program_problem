#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/22 11:52
# @Author  : Scheaven
# @File    : 007_max_towdimension_set.py
# @description: 
'''
算法思想：
算法一：生成一个队列装输出的值，然后遍历每一个输入值，
如果列表中没有横纵坐标都大于输入值时就将入到输出列表；
如果输出列表中的某个值横纵坐标都小于输入值，则删除输出列表的该值；
比较时直接获取输出列表的每个元素算法复杂度为O(N*M**2)


'''
out_point_list = []
min_x = 0
min_y = 0
max_x = 0
max_y = 0

# 算法一：遍历输出列表out_point_list
def add_point_list(x1,y1,min_x,max_x,min_y,max_y):
    i = 0
    k = 0
    list_length = len(out_point_list)
    for j in range(list_length):
        j = j - k
        x0,y0 = out_point_list[j]
        if x0 > x1:
            if y0 > y1:
                return min_x,max_x,min_y,max_y
        else:
            i+=1
            if y0 < y1:
                out_point_list.remove((x0,y0))
                k += 1
                i -= 1
    out_point_list.insert(i,(x1,y1))
    min_x = min(min_x,x1)
    min_y = min(min_y,y1)
    max_x = max(max_x,x1)
    max_y = max(max_y,y1)

    return min_x,max_x,min_y,max_y
# 算法一：折半查找输出列表out_point_list:=====没写好，存在问题
def bisearch_list(x1,y1):
    x_low,x_height = 0,len(out_point_list)
    x_mid = (x_low+x_height)//2
    k = 0
    j = 0
    while True:
        if x_low+1>=x_height:
            break
        x0, y0 = out_point_list[x_mid]
        if x0 > x1:
            x_height = x_mid
            x_mid = (x_low + x_height) // 2
        else:
            x_low = x_mid + 1
            x_mid = (x_low + x_height) // 2
    j = x_mid
    for i in range(x_mid):
        i = i - k
        x0,y0 = out_point_list[i]
        if y0<y1:
            out_point_list.remove((x0, y0))
            k += 1
            j -= 1
    for i in range(x_mid+1,len(out_point_list)):
        x0,y0 = out_point_list[i]
        if y0>y1:
            return

    out_point_list.insert(j,(x1,y1))


if __name__ == '__main__':
    N = int(input())
    x, y = map(int, input().split())
    min_x,max_x,min_y,max_y = x,x,y,y
    out_point_list.append((x,y))
    for i in range(1,N):
        x_axis, y_axis = map(int,input().split())
        if min_x >= x_axis and min_y >= y_axis:
            continue
        elif max_y <= y_axis and max_x <= x_axis:
            out_point_list = []
            out_point_list.insert(0, (x_axis, y_axis))
        else:
            min_x, max_x, min_y, max_y = add_point_list(x_axis, y_axis, min_x, max_x, min_y, max_y)
        # bisearch_list(x_axis, y_axis)

    for A,B in out_point_list:
        print(A,B)


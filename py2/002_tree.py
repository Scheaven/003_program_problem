#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/2 16:19
# @Author  : Scheaven
# @File    : 002_.py
# @description: 
'''
python 2
题目描述
现在有一棵合法的二叉树，树的节点都是用数字表示，现在给定这棵树上所有的父子关系，求这棵树的高度
输入描述:
输入的第一行表示节点的个数n（1 ≤ n ≤ 1000，节点的编号为0到n-1）组成，
下面是n-1行，每行有两个整数，第一个数表示父节点的编号，第二个数表示子节点的编号
输出描述:
输出树的高度，为一个整数
示例1
输入
复制
5
0 1
0 2
1 3
1 4
输出
复制

'''
if __name__=='__main__':
    n=int(raw_input())
    if n==0:
        print 0
    elif n==1:
        print 1
    else:
        tree={'0':[1,0]}
        for i in range(n-1):
            father,child=raw_input().split(' ')
            if father in tree and tree[father][1]<2:
                tree[father][1]+=1
                tree[child]=[tree[father][0]+1,0]
        print max(node[0] for node in tree.values())
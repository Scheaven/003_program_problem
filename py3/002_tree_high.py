#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/12 11:44
# @Author  : Scheaven
# @File    : 002_tree_hight.py
# @description: 
'''
https://www.nowcoder.com/practice/4faa2d4849fa4627aa6d32a2e50b5b25?tpId=85&tqId=29897&tPage=1&rp=1&ru=/ta/2017test&qru=/ta/2017test/question-ranking

算法思想：get_tree_hight2 核心算法
    感觉题的理解稍微有些偏差，题目说是二叉树，其实测试用例里边发现是多叉树。多叉树只取前边出现的两个子树
    有上到下计算树高
    构建字典为根节点和左右子树，
    左右子树分别为层高和子树的个数
    子树的个数来控制是否为二叉树



个人写的多叉树算法思想：
    由下到上计算树高
    从测试用例里边观察到存在子节点出现的规律，是按照顺序出现的。
    对获取的数据简单处理之后，将存储数据的列表逆序。
    然后从最后一个子节点开始向上计算树的高度。每次都寻找最后一个子节点的父节点，然后使其存储树高那以为的数字比所有子节点的最大树高增加1
'''


def get_input():
    tree_list = []
    for line_i in range(n-1):
        f_node,ch_node = input().split(" ")
        tree_list.append([f_node,ch_node,0])
    return tree_list


def read_tree_number():
    f = open("002_tree_h.txt")
    numbers = f.readlines()[0].strip( ).split(" ")
    newNumber = []
    i = 0
    while i < len(numbers):
        newNumber.append([numbers[i],numbers[i+1],0])
        i += 2
    return newNumber


def my_arithmetic():
    n = int(input())
    tree_list = get_input()
    # tree_list = read_tree_number()
    tree_list.reverse()
    # print(tree_list)
    print(get_tree_high(tree_list)+1)


# Calculate the height of the tree from bottom to top
def get_tree_high(tree):
    max_layer = 0
    if len(tree) == 1:
        return 1

    for line_top in range(len(tree)):
        l_f_node,l_ch_node,max_size = tree[line_top]
        if l_f_node != '0':
            tree[len(tree) - int(l_f_node)][2] = max(tree[len(tree) - int(l_f_node)][2], max_size+1)
        else:
            max_layer = max(max_layer,max_size+1)
    return max_layer

################核心算法########################
# It feels really good to borrow the algorithm：Calculate the height of the tree  from top to bottom.
def get_tree_hight2():
    num = int(input())
    tree = {'0': [1, 0]}
    for i in range(num - 1):
        parent, children = input().split()
        if parent in tree and tree[parent][1] < 2:  # 确保是二叉树
            tree[children] = [tree[parent][0] + 1, 0]
            tree[parent][1] += 1
    depth = [x[0] for x in tree.values()]
    print(max(depth))

if __name__ == '__main__':
    my_arithmetic()
    get_tree_hight2()
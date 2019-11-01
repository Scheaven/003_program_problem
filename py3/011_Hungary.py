# 一、问题描述

# 问题描述：N个人分配N项任务，一个人只能分配一项任务，一项任务只能分配给一个人，将一项任务分配给一个人是需要支付报酬，如何分配任务，保证支付的报酬总数最小。

# 问题数学描述：

# 　　

# 二、实例分析---全排列法

# 在讲将匈牙利算法解决任务分配问题之前，先分析几个具体实例。

# 以3个工作人员和3项任务为实例，下图为薪酬图表和根据薪酬图表所得的cost矩阵。

# 　　

# 利用最简单的方法(全排列法)进行求解，计算出所有分配情况的总薪酬开销，然后求最小值。

# total_cost1 = 250 + 600 + 250 = 1100;  x00 = 1,x11 = 1,x22 = 1;

# total_cost2 = 250 + 350 + 400 = 1000;  x00 = 1,x12 = 1,x21 = 1;

# total_cost3 = 400 + 400 + 250 = 1050;  x01 = 1,x10 = 1,x22 = 1;

# total_cost4 = 400 + 350 + 200 = 950;   x01 = 1,x12 = 1,x20 = 1;  //最优分配

# total_cost5 = 350 + 400 + 400 = 1150; x02 = 1,x10 = 1,x21 = 1;

# total_cost6 = 350 + 600 + 250 = 1150; x02 = 1,x11 = 1,x22 = 1;

# 对于任务数和人员数较少时，可利用全排列法计算结果。

# 若将N任务分配给N个人员，其包含的所有分配情况数目为N!，N增大时，全排列法将难以完成任务。

# 三、匈牙利算法

# 下面简要介绍匈牙利算法。

# 其基本的理论基础是针对cost矩阵，将cost矩阵的一行或一列数据加上或减去一个数，其最优任务分配求解问题不变。

# 　　

# 算法的基本步骤如下：

# 　　

# 四、实例分析---匈牙利算法

# 下面结合具体实例，分析匈牙利算法如何解决任务分配问题。

# 以N = 4为实例，下图为cost列表和cost矩阵。

# 　　

# Step1.从第1行减去75，第2行减去35，第3行减去90，第4行减去45。

# 　　

# Step2.从第1列减去0，第2列减去0，第3列减去0，第4列减去5。

# 　　

# Step3.利用最少的水平线或垂直线覆盖所有的0。

# 　　

# Step4.由于水平线和垂直线的总数是3，少于4，进入Step5。

# Step5.没有被覆盖的最小值是5，没有被覆盖的每行减去最小值5，被覆盖的每列加上最小值5，然后跳转到步骤3.

# 　　

# Step3.利用最少的水平线或垂直线覆盖所有的0。

# 　　

# Step4.由于水平线和垂直线的总数是3，少于4，进入Step5。

# Step5.没有被覆盖的最小值是20，没有被覆盖的每行减去最小值20，被覆盖的每列加上最小值20，然后跳转到步骤3.

# 　　

# Step3.利用最少的水平线或垂直线覆盖所有的0。

# 　　

# Step4.由于水平线和垂直线的总数是4，算法结束，分配结果如下图所示。

# 　　

# 其中，黄色框表示分配结果，左边矩阵的最优分配等价于左边矩阵的最优分配。

# 以上内容为转载部分，下面代码内容为原创

# 五、python代码

# 原文链接：https://blog.csdn.net/jingshushu1995/article/details/80411325
import itertools
import numpy as np
from numpy import random
from scipy.optimize import linear_sum_assignment
 
 
# 任务分配类
class TaskAssignment:
 
    # 类初始化，需要输入参数有任务矩阵以及分配方式，其中分配方式有两种，全排列方法all_permutation或匈牙利方法Hungary。
    def __init__(self, task_matrix, mode):
        self.task_matrix = task_matrix
        self.mode = mode
        if mode == 'all_permutation':
            self.min_cost, self.best_solution = self.all_permutation(task_matrix)
        if mode == 'Hungary':
            self.min_cost, self.best_solution = self.Hungary(task_matrix)
 
    # 全排列方法
    def all_permutation(self, task_matrix):
        number_of_choice = len(task_matrix)
        solutions = []
        values = []
        for each_solution in itertools.permutations(range(number_of_choice)):
            each_solution = list(each_solution)
            solution = []
            value = 0
            for i in range(len(task_matrix)):
                value += task_matrix[i][each_solution[i]]
                solution.append(task_matrix[i][each_solution[i]])
            values.append(value)
            solutions.append(solution)
        min_cost = np.min(values)
        best_solution = solutions[values.index(min_cost)]
        return min_cost, best_solution
 
    # 匈牙利方法
    def Hungary(self, task_matrix):
        b = task_matrix.copy()
        # 行和列减0
        for i in range(len(b)):
            row_min = np.min(b[i])
            for j in range(len(b[i])):
                b[i][j] -= row_min
        for i in range(len(b[0])):
            col_min = np.min(b[:, i])
            for j in range(len(b)):
                b[j][i] -= col_min
        line_count = 0
        # 线数目小于矩阵长度时，进行循环
        while (line_count < len(b)):
            line_count = 0
            row_zero_count = []
            col_zero_count = []
            for i in range(len(b)):
                row_zero_count.append(np.sum(b[i] == 0))
            for i in range(len(b[0])):
                col_zero_count.append((np.sum(b[:, i] == 0)))
            # 划线的顺序（分行或列）
            line_order = []
            row_or_col = []
            for i in range(len(b[0]), 0, -1):
                while (i in row_zero_count):
                    line_order.append(row_zero_count.index(i))
                    row_or_col.append(0)
                    row_zero_count[row_zero_count.index(i)] = 0
                while (i in col_zero_count):
                    line_order.append(col_zero_count.index(i))
                    row_or_col.append(1)
                    col_zero_count[col_zero_count.index(i)] = 0
            # 画线覆盖0，并得到行减最小值，列加最小值后的矩阵
            delete_count_of_row = []
            delete_count_of_rol = []
            row_and_col = [i for i in range(len(b))]
            for i in range(len(line_order)):
                if row_or_col[i] == 0:
                    delete_count_of_row.append(line_order[i])
                else:
                    delete_count_of_rol.append(line_order[i])
                c = np.delete(b, delete_count_of_row, axis=0)
                c = np.delete(c, delete_count_of_rol, axis=1)
                line_count = len(delete_count_of_row) + len(delete_count_of_rol)
                # 线数目等于矩阵长度时，跳出
                if line_count == len(b):
                    break
                # 判断是否画线覆盖所有0，若覆盖，进行加减操作
                if 0 not in c:
                    row_sub = list(set(row_and_col) - set(delete_count_of_row))
                    min_value = np.min(c)
                    for i in row_sub:
                        b[i] = b[i] - min_value
                    for i in delete_count_of_rol:
                        b[:, i] = b[:, i] + min_value
                    break
        row_ind, col_ind = linear_sum_assignment(b)
        min_cost = task_matrix[row_ind, col_ind].sum()
        best_solution = list(task_matrix[row_ind, col_ind])
        return min_cost, best_solution
 
 
# 生成开销矩阵
rd = random.RandomState(10000)
task_matrix = rd.randint(0, 100, size=(5, 5))
# 用全排列方法实现任务分配
ass_by_per = TaskAssignment(task_matrix, 'all_permutation')
# 用匈牙利方法实现任务分配
ass_by_Hun = TaskAssignment(task_matrix, 'Hungary')
print('cost matrix = ', '\n', task_matrix)
print('全排列方法任务分配：')
print('min cost = ', ass_by_per.min_cost)
print('best solution = ', ass_by_per.best_solution)
print('匈牙利方法任务分配：')
print('min cost = ', ass_by_Hun.min_cost)
print('best solution = ', ass_by_Hun.best_solution)



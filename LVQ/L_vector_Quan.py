#!/usr/bin/env python
import random
import math
import numpy as np
import matplotlib.pyplot as plt

def creat_data(data_num):
    num_id = range(data_num)
    density = [round(random.uniform(0.2, 0.8), 3) for __ in range(data_num)]
    sugar_content = [round(random.uniform(0, 0.5), 3) for __ in range(data_num)]
    data_set = []
    for i in range(len(num_id)):
        if i>100 and i < 600:
            data_set.append([density[i], sugar_content[i],'c2'])
        else:
            data_set.append([density[i], sugar_content[i], 'c1'])
    return data_set

def get_initial_prototy_vector(data_set,class_num):
    class_data_set = [random.choice(data_set) for __ in range(class_num)]
    return class_data_set

def cal_dist(vector1,vector2):
    vector1 = np.array(vector1)
    vector2 = np.array(vector2)
    dist = math.sqrt(sum((vector1-vector2)**2))
    return dist

def update_prototy_vector(vector1,vector2,flag):
    vector1 = np.array(vector1)
    vector2 = np.array(vector2)
    study_ratio = 0.1
    new_vector = vector1+flag*study_ratio*(vector2-vector1)
    return new_vector

def get_last_prototy_vector(data_set,initial_class_set):
    for i in range(len(data_set)):
        dist = []
        for j in range(len(initial_class_set)):
            dist.append(cal_dist(initial_class_set[j][0:2],data_set[i][0:2]))
        min_dist_index = dist.index(min(dist))
        if initial_class_set[min_dist_index][2] == data_set[i][2]:
            flag = 1
        else:
            flag = -1
        new_vector = update_prototy_vector(initial_class_set[min_dist_index][0:2],data_set[i][0:2],flag)
        initial_class_set[min_dist_index][0:2] = new_vector
        return initial_class_set

def get_class_set(data_set,last_prototy_vector):
    class_set = {}
    for j in range(len(last_prototy_vector)):
        class_set[j] = []
    for i in range(len(data_set)):
        dist = []
        for j in range(len(last_prototy_vector)):
            dist.append(cal_dist(data_set[i][0:2],last_prototy_vector[j][0:2]))
        min_index = dist.index(min(dist))
        class_set[min_index].append(data_set[i][0:2])
    return class_set

def plot_scatter(class_set,last_prototy_vector):
    color = ['red','blue','green','black','yellow']
    x_mean = []
    y_mean = []
    for item in last_prototy_vector:
        x_mean.append(item[0])
        y_mean.append(item[1])
    for key  in class_set:
        print(last_prototy_vector[key][2])
        x = []
        y = []
        for item in class_set[key]:
            x.append(item[0])
            y.append(item[1])
        """
        if last_prototy_vector[key][2] == 'c1':
            color = 'red'
        else:
            color = 'blue'
        """
        plt.scatter(x,y,color = color[key] )
    plt.scatter(x_mean,y_mean,marker='+',s = 300,color = 'red')
    plt.show()

def main():
    last_prototy_vector = []
    i = 0
    data_set = creat_data(1000)
    initial_class_set = get_initial_prototy_vector(data_set,5)
    while i < 100:
        last_prototy_vector = get_last_prototy_vector(data_set, initial_class_set)
        initial_class_set = last_prototy_vector
        i = i+1
    class_set = get_class_set(data_set,last_prototy_vector)
    plot_scatter(class_set,initial_class_set)

if __name__ == '__main__':
    main()












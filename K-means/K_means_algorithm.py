#!/usr/bin/env python
#-*-conding = utf8-*-
"""
K-means算法实现
"""
import random
import matplotlib.pyplot as plt

def get_classfication(star_class,data_set):
    classification = {}
    for key in data_set:
        mindist = 100
        for class_key in star_class:
            dist = 0
            for i in range(len(star_class[class_key])):
                dist += (data_set[key][i]-star_class[class_key][i])**2
            dist = dist ** 0.5
            if dist<mindist:
                mindist = dist
                classification[key] = class_key
    class_fi = {}
    for i in range(len(star_class)):
        class_fi[list(star_class.keys())[i]] = []
        for key in classification:
            if classification[key] == list(star_class.keys())[i]:
                class_fi[list(star_class.keys())[i]].append(key)
    return class_fi

def cla_means(class_fi,data_set):
    attribute_num = len(random.choice(data_set))
    attribute_mean = {}
    for key in class_fi:
        attribute_mean[key] = [0]*attribute_num
        for item in class_fi[key]:
            for i in range(attribute_num):
                attribute_mean[key][i] += data_set[item][i]/len(class_fi[key])
                attribute_mean[key][i] = round(attribute_mean[key][i],3)

    return attribute_mean

def get_random_class(data_set,class_num):
    random_class = {}
    id_keys = [random.choice(list(data_set.keys())) for __ in range(class_num)]
    for key in id_keys:
        random_class[key] = data_set[key]
    return random_class

def plot_scatter(class_fi):
    color = ['red','blue','green','black']
    key_list = list(class_fi.keys())
    for i  in range(len(class_fi)):
        x = []
        y = []
        for item in class_fi[key_list[i]]:
            x.append(data_set[item][0])
            y.append(data_set[item][1])
        plt.scatter(x,y,color = color[i] )
    plt.show()


if __name__ == '__main__':
    num_id = range(100)
    density = [round(random.uniform(0.2, 0.8), 3) for __ in range(100)]
    sugar_content = [round(random.uniform(0, 0.5), 3) for __ in range(100)]
    scal = [random.randint(50, 100) for __ in range(30)]
    data_set = {}
    for i in range(len(num_id)):
        data_set[i] = [density[i], sugar_content[i]]
    com_class_fi = []
    class_num = 3
    star_class = get_random_class(data_set, class_num)
    while True:
        class_fi = get_classfication(star_class,data_set)
        if class_fi == com_class_fi:
            plot_scatter(class_fi)
            break
        else:
            star_class = cla_means(class_fi,data_set)
            com_class_fi = class_fi
        print(class_fi,star_class)










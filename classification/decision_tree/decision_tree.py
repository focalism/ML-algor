#!/usr/bin/env python
import pandas as pd
import math
import matplotlib.pyplot as plt
from plot_decision_tree import createPlot
data_set = pd.read_excel('watermalon2.xlsx',0)

def cal_root_entropy(data_set):
    data_result = dict(data_set.groupby('好瓜').size())
    root_entropy = 0
    for key in data_result:
        root_entropy += -data_result[key]/len(data_set)*math.log(data_result[key]/len(data_set),2)
    return root_entropy

def get_data_classifi(data_set):
    attributes = data_set.columns
    attributes_value = {}
    attributes_data = {}
    for attribute in attributes:
        attributes_value[attribute] = set(data_set[attribute])
    for key in attributes_value:
        attributes_data[key] = {}
        for item in attributes_value[key]:
            attributes_data[key][item] = []
            attributes_data[key][item] = data_set[data_set[key] == item]
    return attributes_data

def cal_entropy(data_set):
    entropy = {}
    attributes_data = get_data_classifi(data_set)
    root_entropy = cal_root_entropy(data_set)
    for key in attributes_data:
        if key != '编号' and key != '好瓜':
            entropy[key] = 0
            for item in attributes_data[key]:
                item_root_entropy = cal_root_entropy(attributes_data[key][item])
                entropy[key] += (len(attributes_data[key][item])/len(data_set))*item_root_entropy
            entropy[key] = round(root_entropy-entropy[key],3)
    return  max(entropy.items(), key=lambda x:x[1])[0]

def getNumLeafs(myTree):
    numLeafs = 0
    firstStr = list(myTree.keys())[0]
    secondDict = myTree[firstStr]
    for key in secondDict:
        if type(secondDict[key]).__name__=='dict':#是否是字典
            numLeafs += getNumLeafs(secondDict[key]) #递归调用getNumLeafs
        else:
            numLeafs +=1 #如果是叶节点，则叶节点+1
    return numLeafs
def get_tree_depth(mytree):
    maxdepth = 0
    firstStr = list(mytree.keys())[0]
    secondDict = mytree[firstStr]
    for key in secondDict:
        if type(secondDict[key]).__name__ == 'dict':
            thisDepth = 1+ get_tree_depth(secondDict[key])
        else:
            thisDepth = 1
        if thisDepth > maxdepth:
            maxdepth = thisDepth
    return maxdepth

def get_tree(data_set):
    node_class = {}
    node1 = (cal_entropy(data_set))
    node_class[node1] = {}
    node_tree = {node1:{}}
    node1_attribute = set(data_set[node1])
    for item in node1_attribute:
        node_class[node1][item] = data_set[data_set[node1] == item].copy()
        if (len(set(node_class[node1][item]['好瓜'])) == 1):
            node_tree[node1][item] = set(node_class[node1][item]['好瓜'])
        else:
            node_tree[node1][item] = get_tree(node_class[node1][item])
    return (node_tree)
mytree = (get_tree(data_set))
print(mytree)
createPlot(mytree)

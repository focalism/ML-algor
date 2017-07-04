#coding:utf-8
import random

class KNN():

    def __init__(self):
        pass

    def create_sample_test_data(self,dataset):
        with open(dataset,'r') as f:
            data = f.readlines()
        sample_data = random.sample(data,len(data)/3)
        test_data = random.sample(data,len(data)/2)
        return sample_data,test_data

    def split_data(self,data):
        pass


    def normalise_data(self,data_set,split_sign):
        normal_data = {}
        for data in data_set:
            data_info = data.split(split_sign)
            for i in range(len(data_info)):
                normal_data[str(i)] = []
                normal_data[str(i)].append(data_info[i])
        for i in range(len(normal_data.keys())-1):
            normal_data[key] = [x/max(normal_data[key]) for x in normal_data[key]]
        return normal_data

    def 





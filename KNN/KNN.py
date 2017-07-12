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
        normal_data = []
        for data in data_set:
            data_info = data.split(split_sign)
            normal_data.append([x for x in data_info])

        for i in range(len(normal_data)):
            for j in range(len(normal_data[i])-1):
                normal_data[i][j] = normal_data[i][j]/max(normal_data[:][j])
        return normal_data
        

    def cal_dist(self,sample_data,unkonw_data):
        result = []
        dist = [[0]]*len(unkonw_data)
        dist = [x*len(sample_data) for x in dist]
        for i  in range(len(unkonw_data)):
            for j in range(len(unkonw_data)):
                for k in range(len(unkonw_data[i])):
                    dist[i][j] += (unkonw_data[i][k]-sample_data[j][k])**2
                    result[i][j].append([dist[i],sample_data[j][-1]])
        return result

    def cluster(self,results,k):
        temp_result = {}
        for i  in len(results):
            results[i].sort()
            if k >len(results[i]):
                return

            temp = results[i][0:k]
            for  j in range(len(temp)):
                if temp[j][1] in temp_result:
                    temp_result[temp[j][1]] += 1
                else:
                    temp_result[temp[j][1]] = 0
            
            Attributes[i] = max(temp_result.items(),key = lambda x:x[1])[1]

        return Attributes

            

        


        

                
                







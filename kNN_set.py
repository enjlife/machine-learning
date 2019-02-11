import numpy as np
import operator
import os

def createDataSet():
    group = np.array([[1.0,1.1],[1.,1.],[0.,0.],[0.,0.1]])
    labels = ['A','A','B','B']
    return group,labels
def classify0(inx,dataset,labels,k):
    datasize = dataset.shape[0]
    diff = np.tile(inx,(datasize,1)) - dataset
    sum = np.sum(np.square(diff),axis=1)
    distances = np.sqrt(sum)
    sort_distance = distances.argsort()
    count = {}
    for i in range(k):
        votelabels = labels[sort_distance[i]]
        count[votelabels] = count.get(votelabels,0) + 1
    sortcount = sorted(count.items(),key=operator.itemgetter(1),reverse=True)
    return sortcount[0][0]
group,labels = createDataSet()
classify0([0,0],group,labels,3)
print(os.path.dirname(__file__))
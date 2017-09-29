from knn import *
def classfier0(dataSet,lables,X,k):
    dataSetSize=dataSet.shape[0]
    '''获取训练集的数量'''
    diffMat=tile(X,[dataSetSize,1])-dataSet
    '''测试数据和训练集合的差值'''
    sqDiffMat=diffMat**2
    distance=(sqDiffMat.sum(axis=1))**2
    '''测试数据距离所有训练集的距离'''
    sortedDisIndex=distance.argsort()
    '''从小到大排列，返回索引值'''
    distCount={}
    for i  in  range(k):
        label=labels[sortedDisIndex[0]]
        distCount[label]=distCount.get(label,0)+1
        '''取前面k个距离最小的数据类型放到字典中'''
    sortedDistCount=sorted(distCount.items(),key=operator.itemgetter(1))
    '''得到二元列表后，元组第二列排序，返回二元列表'''
    return print(sortedDistCount[0][0])
    '''返回二元列表中第0元组第0个元素'''
dataSet,labels=createDataSet()
'''之前4个数据集'''
classfier0(dataSet,labels,[0.5,0.6],3)
from numpy import *
'''加载iris数据，returnMat和irisLabel'''
f = open('C:\project\data\iris.txt')
lines = f.readlines()
returnMat = zeros((len(lines), 4))
'''得到数值矩阵'''
index = 0
irisLabel=[]
'''类型列表'''
for line in lines:
    line = line.strip()
    '''消去换行符'''
    formLine = line.split(',')
    returnMat[index] = formLine[0:4]
    index+=1
    irisLabel.append(formLine[-1])

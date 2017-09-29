from numpy import *
f = open('C:\project\data\iris.txt')
lines = f.readlines()
returnMat = zeros((len(lines), 4))
index = 0

print(irisLabel)irisLabel=[]
for line in lines:
    line = line.strip()
    '''消去换行符'''
    formLine = line.split(',')
    returnMat[index] = formLine[0:4]
    index+=1
    irisLabel.append(formLine[-1])
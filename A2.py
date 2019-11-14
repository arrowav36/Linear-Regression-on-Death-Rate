import pandas as pd
import numpy as np
import statistics
#read dataset of csv format and label it
X=pd.read_csv('death_rate.csv',names=('A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12','A13','A14','A15','B'))
#extract each column and convert it into list
A1 = X['A1']
A1 = list(A1)
A2 = X['A2']
A2 = list(A2)
A3 = X['A3']
A3 = list(A3)
A4 = X['A4']
A4 = list(A4)
B = X['B']
B = list(B)
#find mean of each independend and dependent variables
X1=statistics.mean(A1)
X2=statistics.mean(A2)
X3=statistics.mean(A3)
X4=statistics.mean(A4)
Y1=statistics.mean(B)
#function to find theta_1
def fun1(x,y):
    lst1=[]
    lst2=[]
    ls1=[]
    ls2=[]
    for i in range(len(x)):
        a=x[i]-X1
        lst1.append(a)
    for i in range(len(x)):
        b=y[i]-Y1
        lst2.append(b)

    q=np.array(lst1)
    r=np.array(lst2)
    h=list(q*r)

    s=list(np.square(lst1))
    O1=sum(h)/sum(s)
    O01=Y1-(O1*X1)
    ls1.append(O1)
    ls2.append(O01)
    ls1=ls1+ls2
    return ls1
aa=fun1(A1,B)
bb=fun1(A2,B)
cc=fun1(A3,B)
dd=fun1(A4,B)

O0=(aa[1]+bb[1]+cc[1]+dd[1])/4
print("Enter the first 4 features to predict:\n")
x1,x2,x3,x4=map(float,input().split())
value=O0+aa[0]*x1+bb[0]*x2+cc[0]*x3+dd[0]*x4
print(value)
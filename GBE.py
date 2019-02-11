import numpy as np
import itertools
import functools
from fractions import gcd
#import pandas as pd

def misorientation(x,y,N):
    if x==0:
        return 180.0
    cal_rad=2*np.arctan((y/x)*np.sqrt(N))
    cal_degree=np.degrees(cal_rad)
    return cal_degree

def list_formation(number):
    arr=[]
    while (number > 0):
        arr.append(number%10)
        number = int(number/10)
    return arr
    
def raganathan(sigma,plan):
    N=sum(map(lambda x:x*x,plan))
    m=list(np.arange(0,20,1))
    y=list(np.arange(0,20,1))
    angle=[]
    combination=list(itertools.product(m,y))
    if sigma%2!=0 and N!=0 and sigma!=1:
        for c in range(len(combination)):
            if combination[c][0]==0 and combination[c][1]==0:
                continue
            if combination[c][1]==0:
                continue
            test=np.square(combination[c][0])+np.square(combination[c][1])*N
            if test%2!=0 and test!=sigma:
                continue
            if test==sigma:
                angle.append(misorientation(combination[c][0],combination[c][1],N))
            while test>sigma:
                test=test/2
                if test==sigma:
                    angle.append(misorientation(combination[c][0],combination[c][1],N))
                    break
                if test%2!=0:
                    break
        try:
            return np.round(angle,1)
        except:
            return False
    else:
        return False

def all_solution(sigma):
    u=list(np.arange(0,15,1))
    v=list(np.arange(0,15,1))
    w=list(np.arange(0,15,1))
    arr=[]
    axis=list(itertools.product(u,v,w))
    for num in axis:
        m=0
        if raganathan(sigma,num) and functools.reduce(gcd,num)==1:
#            arr.append(num)
            if not arr:
                arr.append(num)
            elif functools.reduce(gcd,num)==1:
                for i in range(len(arr)):
                    if set(arr[i])==set(num) and sum(arr[i])==sum(num):
                        m=m+1
                if m==0:
                    arr.append(num)
                    
    return arr

def triple_junction(sigma1,sigma2,sigma3,plan):
    angle1,angle2,angle3=list(set(raganathan(sigma1,plan))),list(set(raganathan(sigma2,plan))),list(set(raganathan(sigma3,plan)))
    set_of_angles=[]
    for i in angle1:
        for j in angle2:
            summation,difference=i+j,np.round(abs(i-j),1)
            for k in angle3:
                if summation==k or difference==k or abs(difference-k)<1:
                    comb=[i,j,k]
                    set_of_angles.append(comb)
    return set_of_angles

#column=['axis','angle']
#newDF = pd.DataFrame(columns=column)
#row_index=all_solution(7)
#solution={}
#
#for i in row_index:
#    angle=raganathan(7,i)
#    solution[str(i)]=angle
#    
#d = {'Axis': list(solution.keys()),'Angle': list(solution.values())}
#df = pd.DataFrame(data=d) 
#df.to_csv('F:\sigma 7 permutation.csv',index=False)                        
                        
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 16:21:28 2020

@author: saisr
"""


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
#from sklearn import metrics
def model1(input_variable):
    inp =input_variable
    
    car=['nano','hondacity','volkswagen','hyundai','skoda','maruti']
    
    
    A=[]
    list=['1_Nano_mean.csv','2_New_Honda_city.csv','4_Volkswagen_Vento.csv',
          '6_hyundai_Verna.csv','8_Skoda_Rapid.csv','11_Maruti_swift.csv']
    
    for k in range(0,len(list)):
        data=pd.read_csv(list[k])
        l=data.shape
        
        x=data.iloc[:,0:l[1]-1].values
        y=data.iloc[:,l[1]-1].values
        
        x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
        
        model=LinearRegression()
        model.fit(x_train,y_train)
        
        sum=x[0][:]
        for i in range(1,l[0]):
            sum=sum+x[i][:]
        
        for i in range(0,len(sum)):
            sum[i]=sum[i]/l[0]
        
        sum = [sum]
        q=model.predict(sum)
        q=q.tolist()
        #print cars[k],q
        A.append(q[0])
    print (A)
    least=min(A)
    A=[(i/least) for i in A]
    A=[i*5 for i in A]
    A=[round(i,1) for i in A]
    
    print (A)
    flag=0
    
    for p in range(0,len(car)):
        if(inp== car[p]):
            return (A[p])
            flag=1
            
    if(flag==0):
        return("Not Found")
            
        
def model_vmi(input_variable):
    A=[5,6.2,9.3,8.5,7.7,9.4]
    car=['nano','hondacity','volkswagen','hyundai','skoda','maruti']
    flag=0
    for i in range(0,len(A)):
        if(car[i]==input_variable):
            flag=1
            return(A[i])
            break
    if(flag==0):
        return("Not Found")
"""
Created on Mon Jan 27 21:47:46 2020

@author: saisr

list=['1_Nano_mean.xlsx','2_New_Honda_city.xlsx','3_Datsun_GO.xlsx','4_Volkswagen_Vento.xlsx','5_Chevrolet_Beat.xlsx',
      '6_hyundai_Verna.xlsx','7_Honda_Brio.xlsx','8_Skoda_Rapid.xlsx','9_Volkswagen_Polo.xlsx','11_Maruti_swift.xlsx']

list1=['1_Nano_mean.csv','2_New_Honda_city.csv','3_Datsun_GO.csv','4_Volkswagen_Vento.csv','5_Chevrolet_Beat.csv',
      '6_hyundai_Verna.csv','7_Honda_Brio.csv','8_Skoda_Rapid.csv','9_Volkswagen_Polo.csv','11_Maruti_swift.csv']

print list
list=['1_Nano_mean.xlsx','2_New_Honda_city.xlsx','4_Volkswagen_Vento.xlsx',
      '6_hyundai_Verna.xlsx','8_Skoda_Rapid.xlsx','11_Maruti_swift.xlsx']

list1=['Data/1_Nano_mean.csv','Data/2_New_Honda_city.csv','Data/4_Volkswagen_Vento.csv',
      'Data/6_hyundai_Verna.csv','Data/8_Skoda_Rapid.csv','Data/11_Maruti_swift.csv']

"""

import pandas as pd
import random

list=['1_Nano_mean.xlsx','2_New_Honda_city.xlsx','4_Volkswagen_Vento.xlsx',
      '6_hyundai_Verna.xlsx','8_Skoda_Rapid.xlsx','11_Maruti_swift.xlsx']

list1=['Data/1_Nano_mean.csv','Data/2_New_Honda_city.csv','Data/4_Volkswagen_Vento.csv',
      'Data/6_hyundai_Verna.csv','Data/8_Skoda_Rapid.csv','Data/11_Maruti_swift.csv']
      
for k in range(0,len(list)):
    data=pd.read_excel(list[k])
    data=data.drop(['Dist.','Cost'],axis=1)
    w=data['Mean']
    data_array=data.values
    
    column_names=[]
    for i in range(0,len(data_array)):
        column_names.append(data_array[i,0])
        
    #print w
    #print column_names
    data_final=pd.DataFrame(columns = column_names)
        
    for i in range(0,len(data_array)):
        N=1000
        n_comp=3
        m=w[i]
        m_r=m*0.95
        m_l=m*1.05
        mean=[m_r,m,m_l]
        sigma=[0.01,0.01,0.01]
        mult=[1,1,1]
        assert n_comp == len(mean), "The length of the list of mean values does not match number of Gaussian components"
        assert n_comp == len(sigma), "The length of the list of sigma values does not match number of Gaussian components"
        assert n_comp == len(mult), "The length of the list of multiplier values does not match number of Gaussian components"
        
        rand_samples = []
        for j in range(N):
            pivot = random.uniform(0,n_comp)
            j = int(pivot)
            rand_samples.append(mult[j]*random.gauss(mean[j],sigma[j]))
            
        data_final[data_array[i,0]]=rand_samples
    
    sum=data_final.iloc[:][column_names[0]]
    for p in range(1,len(column_names)):
        sum=sum+data_final.iloc[:][column_names[p]]
        
    mean_index=0
    for q in range(0,len(sum)):
        mean_index=mean_index+sum[q]
    mean_index=mean_index/N
    
    #print mean_index
    mean_index_r=mean_index-(mean_index*0.05)
    mean_index_l=mean_index+(mean_index*0.05)
    mean_index_array=[mean_index_l,mean_index,mean_index_r]
    
    'sigma of index cal.'
    index_sigma=[0.005,0.005,0.005]
       
    mult=[1,1,1]
    assert n_comp == len(mean), "The length of the list of mean values does not match number of Gaussian components"
    assert n_comp == len(sigma), "The length of the list of sigma values does not match number of Gaussian components"
    assert n_comp == len(mult), "The length of the list of multiplier values does not match number of Gaussian components"
        
    index = []
    for j in range(N):
        pivot = random.uniform(0,n_comp)
        j = int(pivot)
        index.append(mult[j]*random.gauss(mean_index_array[j],index_sigma[j]))
            
    data_final['Index']=index
    #print data_final.head()
    data_final.to_csv(list1[k],index=False)

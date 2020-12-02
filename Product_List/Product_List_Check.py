import pandas as pd
import numpy as np

dataset = pd.read_excel("E:\ML\Datasets\product_list.xlsx")
print("Shape: ")
print(dataset.shape)
print('\n')
print('\t\t\t\t\t    Dataset\n')
print('\t\t\t\t\t--------------------\n')
print(dataset.head(10))

clmn_name = list(dataset)
#print(clmn_name)
rows=len(dataset)
print('\n')
print("-------------------The following Columns have Null values-----------------------\n")

for i in clmn_name:
    j=0;  #iterating over each coloumn    
    while(j<=rows-1):
        flag=0
        #print(dataset[i][j])
        j=j+1
    if(dataset[i].isnull().any()==True):
        print("{} Hey! This column has null value".format(dataset[i]))
        print('\n')


print('\n')
print("\t\t----------Finding Mean of MRP and Sale Price----------------")

mean_value1=dataset['MRP'].mean()
mean_value2=dataset['Sale Price'].mean()
print('\n')
print("--------------------The Mean Values are :\n MRP: {} ||||| Sale Price:{}--------------------".format(mean_value1,mean_value2))
print('\n')
dataset['MRP'].fillna(value=dataset['MRP'].mean(), inplace=True)
dataset['Sale Price'].fillna(value=dataset['Sale Price'].mean(), inplace=True)
print(dataset.head())


print('\n')
print("Comapring MRP and Sale Price.........")


if (np.where(dataset['MRP']>=dataset['Sale Price'])):
    print('\n')
    print("_________Warning!!!!!!! Some of the MRP values are greater than Sale Price______________\n")
    print("Adjusting MRP and Sale Price..............")
    print('\n')
    
#comparing the Elements in MRP and Sale Price 
    for ind in dataset.index:
        if (dataset['MRP'][ind]>dataset['Sale Price'][ind]):
            copy=dataset['MRP'][ind]
            dataset['MRP'][ind]=dataset['Sale Price'][ind]
            dataset['Sale Price'][ind]=copy

print('\n')
print("Done")
print('\n')
print(dataset.head())


print('\n')

print("Cleaning the whole dataset........")
print('\n')

dataset.at[1,'Product Name']= "PRODUCT2"
dataset.at[4,'Product Name']= "PRODUCT5"
dataset.at[0,'Weight']=1000
i=[0,1,2,3,4]
dataset.at[i,'Weight Unit (g/kg)']= 'g'


mean_value3=dataset['Stock'].mean()
mean_value4=dataset['Weight'].mean()


dataset['Stock'].fillna(value=dataset['Stock'].mean(), inplace=True)
dataset['Weight'].fillna(value=dataset['Weight'].mean(), inplace=True)
print('\n')
print('--------------------------------:Updated Dataframe:------------------------------\n')


clean_dataset=dataset
print(clean_dataset.head())

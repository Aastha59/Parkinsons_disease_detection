#!/usr/bin/env python
# coding: utf-8

# Importing Dependencies 

# In[1]:


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import svm
from sklearn.metrics import accuracy_score


# In[2]:


df=pd.read_csv("parkinsons.csv")


# In[3]:


df


# In[4]:


df.head()


# In[5]:


df.describe()


# In[6]:


df.info()


# In[7]:


#to see all the rows
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
df


# In[8]:


df.shape


# In[9]:


df.isnull().sum()
#there is no null value ... so it is a good dataset


# In[10]:


#'value_counts()' method in Pandas is used to get a Series containing the counts of unique values in a column
df['status'].value_counts()
# 1: those who are affected by partition
# 0: those who are not affected by partition


# In[11]:


#df is the DataFrame you have created, which contains your data.
#status is the column name based on which you want to group the DataFrame.
#.groupby('status') groups the DataFrame 'df' based on unique values in the 'status' column.
#.mean() calculates the mean for each group separately
df.groupby('status').mean()


# In[12]:


X=df.drop(columns=['name', 'status'],axis=1)
Y=df['status']


# In[13]:


print(X)


# In[14]:


print(Y)


# In[15]:


X_train, X_test, Y_train,Y_test= train_test_split(X,Y, test_size=0.2,random_state=2)


# In[16]:


print(X.shape,X_train.shape,X_test.shape)


# In[17]:


ss=StandardScaler()


# In[18]:


# data standardization
# Process of transforming data into standardized format so that user may process any value
#fit training data into it
ss.fit(X_train)


# In[19]:


X_train=ss.transform(X_train)
X_test=ss.transform(X_test)


# In[20]:


X_train=ss.transform(X_train)
X_test=ss.transform(X_test)


# In[21]:


print(X_train)


# In[22]:


print(X_test)


# In[23]:


#SVM(Support vector machine is used. It is used in email, web pages, handwriting recognization, page identification, gene classification)
model=svm.SVC(kernel='linear')


# In[24]:


model.fit(X_train, Y_train)


# In[25]:


#model evaluation
#by prediction check the accuracy of train and test data
X_train_pred=model.predict(X_train)
train_data_acc=accuracy_score(Y_train, X_train_pred)


# In[26]:


print("acc of training data : ", train_data_acc)


# In[27]:


X_test_pred=model.predict(X_test)
test_data_acc=accuracy_score(Y_test,X_test_pred)


# In[28]:


print("accuracy of testing data: ",test_data_acc)


# In[30]:


input_data=(217.11600,233.48100,93.97800,0.00404,0.00002,0.00127,0.00128,0.00381,0.01299,0.12400,0.00679,0.00631,0.01075,0.02038,0.00681,24.58100,0.462516,0.582710,-5.517173,0.389295,2.925862,0.220657)
input_data_np=np.asarray(input_data)
input_data_re=input_data_np.reshape(1,-1)
s_data=ss.transform(input_data_re)
pred=model.predict(s_data)
print(pred)
if(pred[0]==0):
    print("Negative, No Parkinsons found")
else:
    print("Positive, Parkinsons found")


# In[ ]:





# In[ ]:





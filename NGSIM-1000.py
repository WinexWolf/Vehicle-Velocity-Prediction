#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df=pd.read_excel("1000cars_dsproject.xlsx")
df.head()


# In[3]:


df.describe()


# In[4]:


df = df.fillna("NA")
df.isnull()


# In[5]:


df.shape


# In[6]:


df.isnull().sum()


# In[7]:


#find min global time in ms
ms_min_gt = df['Global_Time'].min()
ms_min_gt


# In[8]:


#milliseconds to seconds
df['Global_Time']=df['Global_Time']/1000


# In[9]:


#find min global time in s
s_min_gt = df['Global_Time'].min()
s_min_gt


# In[10]:


#new column for velocity groups
df['v_group'] = df.apply(lambda _: '', axis=1)
df.loc[((df['v_Vel'] >=0) &(df['v_Vel'] < 10)), 'v_group'] = 0
df.loc[((df['v_Vel'] >=10) &(df['v_Vel'] < 20)), 'v_group'] = 1
df.loc[((df['v_Vel'] >=20) &(df['v_Vel'] < 30)), 'v_group'] = 2
df.loc[((df['v_Vel'] >=30) &(df['v_Vel'] < 40)), 'v_group'] = 3
df.loc[((df['v_Vel'] >=40) &(df['v_Vel'] < 50)), 'v_group'] = 4
df.loc[((df['v_Vel'] >=50) &(df['v_Vel'] < 60)), 'v_group'] = 5
df.loc[((df['v_Vel'] >=60) &(df['v_Vel'] < 70)), 'v_group'] = 6


# In[11]:


#number of cars in each lane
df_lane=df.groupby(['Lane_ID'])['Vehicle_ID'].count().reset_index(name='number of cars')
df_lane


# In[12]:


#Vehicle attributes
veh_attributes=pd.DataFrame(zip(df.Preceding,df.Space_Headway,df.Vehicle_ID,df.v_Vel))
veh_attributes = veh_attributes.rename(columns={0: 'Current_Vehicle_No.', 3: 'Following_Vehicle_Velocity',2:'Following_Vehicle_No.',1:'Gap'})
veh_attributes


# In[13]:


#convert feet to metres *0.3048
df['v_Acc']=df['v_Acc']*0.3048
df


# In[14]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[15]:


import matplotlib.pyplot as plt
# x axis values 
x = df['Global_Time']
# corresponding y axis values 
y = df['v_Acc']
# plotting the points  
plt.plot(x, y) 
  
# naming the x axis 
plt.xlabel('time(s)') 
# naming the y axis 
plt.ylabel('acceleration(m/s^2)') 
  
# giving a title to my graph 
plt.title('My first graph!') 
  
# function to show the plot 
plt.show() 


# In[ ]:





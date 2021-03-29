#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np


# In[5]:


df=pd.read_excel("dsproject_400_cars.xlsx")
df.head()


# In[6]:


df.describe()


# In[7]:


df = df.fillna("NA")


# In[8]:


df.isnull()


# In[9]:


df.shape


# In[10]:


df.isnull().sum()


# In[11]:


import matplotlib.pyplot as plt


# In[12]:


df.dtypes


# In[13]:


import seaborn as sns
sns.relplot(x='Local_X',y='Local_Y',data=df)


# In[14]:


sns.relplot(x='Global_X',y='Global_Y',data=df)


# In[15]:


dff=df.groupby(['Lane_ID'])['Vehicle_ID'].count().reset_index(name='number of cars')
dff


# In[16]:


df0=df.loc[df['Lane_ID'] == 0]
df0


# In[17]:


sns.relplot(x='Local_X',y='Local_Y',data=df0)


# In[18]:


df1=df.loc[df['Lane_ID'] == 1]
df1


# In[19]:


sns.relplot(x='Local_X',y='Local_Y',data=df1)


# In[20]:


import matplotlib.pyplot as plt


# In[21]:


plt.scatter(df0['Local_X'],df0['Local_Y'], color='r')
plt.scatter(df1['Local_X'],df1['Local_Y'], color='g')
plt.xlabel('Latitude')
plt.ylabel('Longitude')
plt.show()


# In[22]:


df['v_group'] = df.apply(lambda _: '', axis=1)


# In[23]:


df.loc[((df['v_Vel'] >=0) &(df['v_Vel'] < 10)), 'v_group'] = 0
df.loc[((df['v_Vel'] >=10) &(df['v_Vel'] < 20)), 'v_group'] = 1
df.loc[((df['v_Vel'] >=20) &(df['v_Vel'] < 30)), 'v_group'] = 2
df.loc[((df['v_Vel'] >=30) &(df['v_Vel'] < 40)), 'v_group'] = 3
df.loc[((df['v_Vel'] >=40) &(df['v_Vel'] < 50)), 'v_group'] = 4
df.loc[((df['v_Vel'] >=50) &(df['v_Vel'] < 60)), 'v_group'] = 5
df.loc[((df['v_Vel'] >=60) &(df['v_Vel'] < 70)), 'v_group'] = 6


# In[24]:


df.tail()


# In[25]:


arr1 = np.array([df['Frame_ID'],  
                       df['Global_Time']])


# In[26]:


print(arr1)


# In[27]:


sns.relplot(x='Global_Time',y='Frame_ID',data=df0)


# In[49]:


sns.relplot(x='Global_Time',y='Local_Y',data=df)


# In[48]:


sns.relplot(x='Global_Time',y='Local_Y',data=df0)


# In[47]:


sns.relplot(x='Global_Time',y='Local_Y',data=df1)


# In[50]:


df1a=df.groupby(['Local_Y','Global_Time'])['v_group'].unique().reset_index(name='Velocity group')
df1a


# In[51]:


df1b=df1a.pivot(index='Local_Y',columns='Global_Time')
df1b=df1b.fillna(0)
df1b


# In[52]:


df1c=df1b.T
df1c


# In[34]:


import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sn
import plotly as py


# In[35]:


def multi_plot(df, title, addAll = True):
   fig = go.Figure()

   for column in df.columns.to_list():
       fig.add_trace(
           go.Bar(
                x =[1,2,3,4,5,6,7,8,9,10],
               y = df[column]['Velocity group'],
               name = column
           )
       )

   button_all = dict(label = 'All',
                     method = 'update',
                     args = [{'visible': df.columns.isin(df.columns),
                              'title': 'All',
                              'showlegend':True}])

   def create_layout_button(column):
       return dict(label = column,
                   method = 'update',
                   args = [{'visible': df.columns.isin([column]),
                            'title': column,
                            'showlegend': True}])

   fig.update_layout(
       updatemenus=[go.layout.Updatemenu(
           active =0 ,
           buttons = ([button_all] * addAll) + list(df.columns.map(lambda column: create_layout_button(column)))
           )
       ],
        yaxis_type="log"       
   )
   # Update remaining layout properties
   fig.update_layout(
       title_text=title,
       height=800
       
   )
  
   fig.show()
multi_plot(df1c, title="by Local_Y")


# In[38]:


min_gt = df['Global_Time'].min()
min_gt


# In[39]:


df['Global_Time']=df['Global_Time']-min_gt


# In[43]:


df['Global_Time']=df['Global_Time']/1000


# In[46]:





# In[ ]:





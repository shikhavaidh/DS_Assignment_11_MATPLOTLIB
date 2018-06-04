
# coding: utf-8

# In[2]:



# In[92]:

#Assignment 11.1
#This assignment is for visualization using matplotlib:
#data to use:
#url=https://raw.githubusercontent.com/Geoyi/Cleaning-Titanic-Data/master/titanic_original.csv'
#titanic = pd.read_csv(url)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
url="https://raw.githubusercontent.com/Geoyi/Cleaning-Titanic-Data/master/titanic_original.csv"
titanic = pd.read_csv(url)
df = pd.DataFrame(titanic)
dfTotalRowCount = df.count() 
dfSexCnt = df['sex'].value_counts()
#print(dfSexCnt)
cntMale = dfSexCnt['male']
cntFemale = dfSexCnt['female']
print("Male - " + str(cntMale))
print("Female - " + str(cntFemale))

#Charts to plot:
#1.Create a pie chart presenting the male/female proportion
# Data to plot
labels = 'Male', 'Female'
sizes = [cntMale, cntFemale]
colors = ['yellowgreen', 'gold']
plt.pie(sizes, colors=colors, shadow=True, startangle=90, autopct='%1.1f%%')
plt.legend(patches, labels, loc="best")
plt.axis('equal')
plt.tight_layout()
plt.show()


# In[3]:

# In[ ]:

#2. Create a scatterplot with the Fare paid and the Age, differ the plot color by gender


# In[143]:

#filtered_df.count()
df['color'] = np.where(df['sex']=='female', 'black', 'green')
plt.scatter(df['fare'],df['age'],color=df['color'],label=df['sex'].value_counts())
plt.xlim(0, 100)
#plt.ylim(0, 100)
plt.legend(loc=1)
plt.grid(True)

plt.show()


# In[ ]:




# In[ ]:




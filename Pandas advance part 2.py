#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[6]:


course_name = ['Data Science', 'Machine Learning', 'Big Data', 'Data Engineer']
duration = [2,3,6,4]
df = pd.DataFrame(data = {'course_name' : course_name, 'duration' : duration})


# In[7]:


df


# Q1. Write a code to print the data present in the second row of the dataframe, df.

# In[23]:


df.loc[1:1]


# Q2. What is the difference between the functions loc and iloc in pandas.DataFrame?

# In[24]:


dic = {"Brand":["Honda","Tata","Maruti"],
       "Year":[2020,2021,2022],
       "Km":[1000,110,10]
    
}


# In[26]:


x=pd.DataFrame(dic)


# In[27]:


x


# python loc() function
# The loc() function is label based data selecting method which means that we have to pass the name of the row or column which we want to select. This method includes the last element of the range passed in it, unlike iloc(). loc() can accept the boolean data unlike iloc(). Many operations can be performed using the loc()

# In[31]:


x.loc[x.Brand=="Tata"] #example of loc


# In[32]:


x.loc[1:1]


# The iloc() function is an indexed-based selecting method which means that we have to pass an integer index in the method to select a specific row/column. This method does not include the last element of the range passed in it unlike loc(). iloc() does not accept the boolean data unlike loc(). Operations performed using iloc() are:

# In[35]:


x.iloc[[1]] #example of iloc


# Q3. Reindex the given dataframe using a variable, reindex = [3,0,1,2] and store it in the variable, new_df
# then find the output for both new_df.loc[2] and new_df.iloc[2].
# 
# Did you observe any difference in both the outputs? If so then explain it.
# Consider the below code to answer further questions:
# import pandas as pd
# import numpy as np
# columns = ['column_1', 'column_2', 'column_3', 'column_4', 'column_5', 'column_6']
# indices = [1,2,3,4,5,6]
# #Creating a dataframe:
# df1 = pd.DataFrame(np.random.rand(6,6), columns = columns, index = indices)
# 

# In[36]:


import pandas as pd
import numpy as np
columns = ['column_1', 'column_2', 'column_3', 'column_4', 'column_5', 'column_6']
indices = [1,2,3,4,5,6]
#Creating a dataframe:
df1 = pd.DataFrame(np.random.rand(6,6), columns = columns, index = indices)


# In[37]:


df1


# In[49]:


new_indices=[3,0,1,2]


# In[52]:


new_df=df1.reindex(new_indices)


# In[53]:


new_df


# In[56]:


new_df.loc[[2]]


# In[57]:


new_df.iloc[[2]]


# by observing both the case we can say that loc keyword is used for both index & row. on the other
# hand iloc is used for index only

# Q4. Write a code to find the following statistical measurements for the above dataframe df1:
# (i) mean of each and every column present in the dataframe.
# (ii) standard deviation of column, ‘column_2’

# In[59]:


df1


#  (i) mean of each and every column present in the dataframe

# In[61]:


df1.mean()


# (ii) standard deviation of column, ‘column_2’

# In[73]:


df1['column_2']=df1.std()


# In[77]:


df1['column_2']


# In[75]:


df1.describe()


# Q6. What do you understand about the windows function in pandas and list the types of windows
# functions?

# In[78]:


import pandas as pd


# In[79]:


file = pd.read_csv("D:\data analysit python\Titanic\Titanic.csv")


# In[80]:


f = file.groupby("Survived")


# In[81]:


f.sum()  #if we want to check sum


# In[82]:


f.min()


# In[83]:


f.max()


# In[84]:


f = file.groupby("Sex")


# In[85]:


f.sum()


# Q7. Write a code to print only the current month and year at the time of answering this question.

# In[88]:


import pandas as pd
import datetime


# In[91]:


from datetime import date
  
# creating the date object of today's date
todays_date = date.today()
  
# printing todays date
print("Current date: ", todays_date)
  
# fetching the current year, month and day of today
print("Current year:", todays_date.year)
print("Current month:", todays_date.month)


# Q9. Write a Python program that reads a CSV file containing categorical data and converts a specified
# column to a categorical data type. The program should prompt the user to enter the file path, column
# name, and category order, and then display the sorted data.

# Q11. You are given a CSV file containing student data that includes the student ID and their test score. Write
# a Python program that reads the CSV file, calculates the mean, median, and mode of the test scores, and
# displays the results in a table.
# The program should do the followingM
# I Prompt the user to enter the file path of the CSV file containing the student dataR
# I Read the CSV file into a Pandas DataFrameR
# I Calculate the mean, median, and mode of the test scores using Pandas toolsR
# I Display the mean, median, and mode in a table.
# Assume the CSV file contains the following columnsM
# I Student ID: The ID of the studentR
# I Test Score: The score of the student's test.
# Example usage of the program:
# Enter the file path of the CSV file containing the student data: student_data.csv
# +-----------+--------+
# | Statistic | Value |
# +-----------+--------+
# | Mean | 79.6 |
# | Median | 82 |
# | Mode | 85, 90 |
# +-----------+--------+
# Assume that the CSV file student_data.csv contains the following data:
# Student ID,Test Score
# 1,85
# 2,90
# 3,80
# 4,75
# 5,85
# 6,82
# 7,78
# 8,85
# 9,90
# 10,85
# The program should calculate the mean, median, and mode of the test scores and display the results

# In[118]:


import pandas as pd


# In[119]:


Lucky = pd.read_csv("D:\student_data\student_data.csv")


# In[120]:


Lucky.head()


# In[121]:


Lucky.describe()


# In[122]:


Lucky.columns


# In[123]:


Lucky['Test Score'].mean()


# In[124]:


Lucky['Test Score'].std()


# In[128]:


Lucky['Test Score'].mode()


# In[ ]:





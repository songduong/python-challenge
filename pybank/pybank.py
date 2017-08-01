
# coding: utf-8

# In[79]:

import pandas as pd
import numpy as np


# In[80]:

'pybank="pybank.csv"
pbf = pd.read_csv(pybank)
pbf.head()
#pbf=pybank file =] 


# In[81]:

total_months=len(pbf.Date.unique())


# In[82]:

revenue_sum=pbf["Revenue"].sum()


# In[99]:

avg_rev_chg=int(pbf["Revenue"].diff().mean())


# In[105]:

pbf["Rev Dif"]=pbf["Revenue"].diff()


# In[102]:

max_date=pbf.ix[pbf["Rev Dif"].idxmax()]
min_date=pbf.ix[pbf["Rev Dif"].idxmin()]


# In[117]:

print("Financial Analysis")
print("--------------(drum roll)---------------------")
print("Total Months: " + str(total_months))
print("Total Revenue: "+ "$" + str(revenue_sum))
print("Average Revenue Change: $" + str(round(avg_rev_chg)))
print("Greatest Increase in Revenue: " + str(max_date["Date"]) + " " + "$" +str(int(max_date["Rev Dif"])))
print("Greatest Decrease in Revenue: " + str(min_date["Date"]) + " " + "$" +str(int(min_date["Rev Dif"])))


# In[ ]:




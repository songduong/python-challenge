
# coding: utf-8

# In[17]:

import numpy as np
import pandas as pd


# In[18]:

pypoll="pypoll.csv"
ppf = pd.read_csv(pypoll)


# In[19]:

total_votes=len(ppf["Voter ID"])


# In[20]:

can_list=ppf["Candidate"].unique().tolist()


# In[21]:

canct=ppf["Candidate"].value_counts()


# In[38]:

Khan=canct["Khan"]
Correy=canct["Correy"]
Li=canct["Li"]
OTooley=canct["O'Tooley"]


# In[43]:

all_votes_count={
    "Khan": canct["Khan"],
    "Correy": canct["Correy"],
    "Li": canct["Li"],
    "Otooley": canct["O'Tooley"]
}


# In[40]:

khanpct='{:.1%}'.format(khan/total_votes)
correypct='{:.1%}'.format(correy/total_votes)
lipct='{:.1%}'.format(li/total_votes)
otooleypct='{:.1%}'.format(otooley/total_votes)


# In[45]:

winner=max(all_votes_count, key=all_votes_count.get)


# In[46]:

print("Election Results")
print("--------------------------")
print("Total Votes: " + str(total_votes))
print("--------------------------")
print("Khan: " + str(khanpct) + " " + str(khan))
print("Correy: " + str(correypct) + " " + str(correy))
print("Li: " + str(lipct) + " " +str(li))
print("O'Tooley: " + str(otooleypct) + " " +str(otooley))
print("--------------------------")
print("Winner: " + str(winner))


# In[ ]:




#!/usr/bin/env python
# coding: utf-8

# In[1]:


"Import file"
import pandas as pd
file= "C:/Users/sledg/PythonData/pandas-challenge/Resources/data.csv"
data= pd.read_csv(file)
data.head()


# In[2]:


"Find number of players"
players_count= len(data['SN'].unique())
players_count


# In[3]:


"Create data frame"
total_players_df= pd.DataFrame({"Total Players":[players_count]})
total_players_df


# In[4]:


"Purchasing Analysis (Total)"
num_unique_items=len(data["Item ID"].unique())
num_unique_items


# In[5]:


avg_price=(data["Price"].mean())
avg_price


# In[6]:


num_purchases=(data["SN"].count())
num_purchases


# In[7]:


total_rev=(data["Price"].sum())
total_rev


# In[8]:


print("Purchasing Analysis (Total)")
purchasing_analysis_list= pd.DataFrame({"Number of Unique Items": [num_unique_items], "Average Price": [avg_price],"Number of Purchases": [num_purchases],"Total Revenue":[total_rev]})
purchasing_analysis_list


# In[9]:


"Gender Demographics"
group_data=data.groupby(["Gender"])
group_data


# In[10]:


gender_count=data["Gender"].unique()
gender_count


# In[11]:


total_gender_each=group_data["Gender"].value_counts()
total_gender_each


# In[12]:


percent_players=(data["Gender"].value_counts()/data["Gender"].count())*100
percent_players
percent_players.head()


# In[13]:


info_gender=data["Gender"].value_counts()
info_gender


# In[14]:


print("Gender Demographics")
gender_list=pd.DataFrame({"Total Count": info_gender, "Percentage of Players": percent_players})
gender_list
gender_list.head()


# In[15]:


"Purchasing Analysis (Gender)"
group_data=data.groupby(["Gender"])
group_data

total_gender_each=group_data["Gender"].value_counts()
total_gender_each


# In[16]:


avg_purchase_price=group_data["Price"].mean()
avg_purchase_price


# In[17]:


total_purchase_value=group_data["Price"].sum()
total_purchase_value


# In[18]:


avg_purchase_person=(group_data["Price"].mean())*num_purchases/576
avg_purchase_person


# In[19]:


print("Purchasing Analysis (Gender)")
purchasing_analysis_list=pd.DataFrame({"Purchase Count": total_gender_each, "Average Purchase Price": avg_purchase_price, "Total Purchase Value": total_purchase_value, "Avg Total Purchase Per Person": avg_purchase_person})
purchasing_analysis_list.head()


# In[20]:


"Import file"
import pandas as pd
file= "C:/Users/sledg/PythonData/pandas-challenge/Resources/data.csv"
data= pd.read_csv(file)
data.head()


# In[21]:


"Age Demographics"
agebins = [0, 9.90, 14.90, 19.90, 24.90, 29.90, 34.90, 39.90, 99999]
agenames=["<10", "10-14", "15-19", "20-24", "25-29","30-34","35-39","40+"]
data["Age Demographics"]=pd.cut(data["Age"], agebins, labels=agenames)
data


# In[22]:


data=data.groupby(["Age Demographics"])
data.head()


# In[23]:


age_count= (data["Age Demographics"].count())
age_count


# In[24]:


age_percent= (data["Age"].value_counts)
age_percent_final= (age_percent/num_purchases)*100


# In[ ]:


print("Age Demographics")


# In[ ]:


age_dem_list= pd.DataFrame({"Total Count": age_count, "Percent Players": age_percent})
age_dem_list.head()


# In[35]:


"Purchasing Analysis (Age)"
avg_purchase_count_age=data["Age"].count()
avg_purchase_price_age=data["Price"].mean()
total_purchase_age=data["Price"].sum()
avg_total_person_age=(data["Price"].mean())*(780/576)


# In[ ]:


print("Purchasing Analysis (Age)")
purchasing_analysis_age_list=pd.DataFrame({"Purchase Count": avg_purchase_count_age, "Average Purchase Price": avg_purchase_price_age, "Total Purchase Value": total_purchase_age, "Avg Total Purchase per Person": avg_total_person_age})
purchasing_analysis_age_list.head()


# In[ ]:


"Import file"
import pandas as pd
file= "C:/Users/sledg/PythonData/pandas-challenge/Resources/data.csv"
data= pd.read_csv(file)
data.head()


# In[ ]:


top_spenders= data[["Purchase ID", "SN", "Price"]]
top_spenders.head()


# In[ ]:


top_spenders= top_spenders.groupby(["SN"])
top_spenders.head()


# In[ ]:


purchase_count_SN= top_spenders["SN"].value_counts()
purchase_count_SN.head()


# In[ ]:


avg_purchase_price_SN= top_spenders["Price"].mean()
avg_purchase_price_SN


# In[ ]:


total_purchase_SN= top_spenders["Price"].sum()
total_purchase_SN.head()


# In[ ]:


print("Top Spenders")
top_spenders_list= pd.DataFrame({"Purchase Count": purchase_count_SN, "Average Purchase Price": avg_purchase_price_SN, "Total Purchase Value": total_purchase_SN})
top_spenders_list=top_spenders_list.sort_values("Total Purchase Value", ascending= True)
top_spenders_list.head()


# In[25]:


"Import file"
import pandas as pd
file= "C:/Users/sledg/PythonData/pandas-challenge/Resources/data.csv"
data= pd.read_csv(file)
data.head()
"Most Popular Items"
most_pop_items= data[["Item ID", "Item Name", "Price"]]
most_pop_items.head()


# 
# 
# 

# In[26]:


most_pop_items=most_pop_items.groupby("Item ID")
most_pop_items.head()


# In[27]:


purchase_count_itemID= most_pop_items["Item Name"].value_counts()
purchase_count_itemID.head()


# In[28]:


avg_price_itemID= data["Price"].mean()
avg_price_itemID


# In[29]:


total_purchase_itemID= data["Price"].sum()
total_purchase_itemID


# In[33]:


print("Most Popular Items"
      most_pop_items_list=pd.DataFrame({"Purchase Count": purchase_count_itemID, "Item Price": avg_price_itemID, "Total Purchase Value": total_purchase_itemID})
      most_pop_items_list.head()


# In[34]:


print("Most Profitable Items")
most_pop_items_list= most_pop_items.sort_values("Total Purchase Value", ascending=False)
most_pop_items_list.head()


# In[ ]:





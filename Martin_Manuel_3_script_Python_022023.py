#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import requests

# ask user for X-RapidAPI-Key, app_key, and app_id
x_rapidapi_key = input("Enter your X-RapidAPI-Key: ")
app_key = input("Enter your app_key: ")
app_id = input("Enter your app_id: ")

# set up API request parameters
url = "https://edamam-food-and-grocery-database.p.rapidapi.com/api/food-database/v2/parser"
querystring = {"app_key": app_key, "app_id": app_id, "ingr": "champagne"}
headers = {
    "X-RapidAPI-Key": x_rapidapi_key,
    "X-RapidAPI-Host": "edamam-food-and-grocery-database.p.rapidapi.com"
}

# send API request and get response
response = requests.request("GET", url, headers=headers, params=querystring)

# convert response json to a pandas dataframe
results = response.json()["hints"]
df = pd.json_normalize(results)
df_sortie = df[['food.foodId','food.label','food.category','food.foodContentsLabel','food.image']]
df_sortie = df_sortie.head(10)

# save results to csv file
df_sortie.to_csv('extraction_10_premiers_produits_champagne.csv')



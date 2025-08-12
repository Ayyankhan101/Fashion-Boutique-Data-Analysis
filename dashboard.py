import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Fashion Boutique Analysis Dashboard')

# Load the data
df = pd.read_csv('fashion_boutique_dataset.csv.gz', compression='gzip')

# Data Cleaning
df['customer_rating'].fillna(df['customer_rating'].mean(), inplace=True)
df['size'].fillna(df['size'].mode()[0], inplace=True)
df['return_reason'].fillna('Not Returned', inplace=True)

# Sidebar Filters
st.sidebar.header('Filters')
category = st.sidebar.multiselect(
    'Select Category',
    options=df['category'].unique(),
    default=df['category'].unique()
)

brand = st.sidebar.multiselect(
    'Select Brand',
    options=df['brand'].unique(),
    default=df['brand'].unique()
)

season = st.sidebar.multiselect(
    'Select Season',
    options=df['season'].unique(),
    default=df['season'].unique()
)

# Filter the dataframe
df_filtered = df[df['category'].isin(category) & df['brand'].isin(brand) & df['season'].isin(season)]

st.header('Filtered Data')
st.write(df_filtered)

# Visualizations
st.header('Data Visualizations')

# Price Distribution
st.subheader('Price Distribution')
fig, ax = plt.subplots()
sns.histplot(df_filtered['current_price'], bins=30, kde=True, ax=ax, color='green' , alpha=0.6)
st.pyplot(fig)

# Product Count by Category
st.subheader('Product Count by Category')
fig, ax = plt.subplots()
sns.countplot(y='category', data=df_filtered, order = df_filtered['category'].value_counts().index, ax=ax , palette='viridis', color='red')
st.pyplot(fig)

# Price Distribution by Category
st.subheader('Price Distribution by Category')
fig, ax = plt.subplots()
sns.boxplot(x='category', y='current_price', data=df_filtered, ax=ax , palette='Set2', color='orange')
plt.xticks(rotation=45)
st.pyplot(fig)

# Return Analysis
st.header('Return Analysis')

# Return Rate
st.subheader('Return Rate')
return_counts = df_filtered['is_returned'].value_counts()
fig, ax = plt.subplots()
ax.pie(return_counts, labels=return_counts.index, autopct='%1.1f%%', startangle=90 , colors=['lightblue', 'lightcoral'])
st.pyplot(fig)

# Return Reasons
st.subheader('Return Reasons')
fig, ax = plt.subplots()
sns.countplot(y='return_reason', data=df_filtered[df_filtered['is_returned']==True], order = df_filtered[df_filtered['is_returned']==True]['return_reason'].value_counts().index, ax=ax,palette='pastel', color='orange')
st.pyplot(fig)

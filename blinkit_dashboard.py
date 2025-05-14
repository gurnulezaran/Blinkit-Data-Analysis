
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page settings
st.set_page_config(page_title="Blinkit Sales Dashboard", layout="wide")

# Title
st.title("🛒 Blinkit Sales Analysis Dashboard")

# Load data
df = pd.read_csv("blinkit_data.csv")

# Data cleaning
df['Item Fat Content'] = df['Item Fat Content'].replace({
    'LF': 'Low Fat',
    'low fat': 'Low Fat',
    'reg': 'Regular'
})

# Metrics
total_sales = df['Sales'].sum()
avg_sales = df['Sales'].mean()
no_of_items_sold = df['Sales'].count()
avg_ratings = df['Rating'].mean()

# Display KPIs
st.subheader("📌 Key Performance Indicators")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Sales", f"${total_sales:,.0f}")
col2.metric("Average Sales", f"${avg_sales:,.0f}")
col3.metric("Items Sold", f"{no_of_items_sold:,}")
col4.metric("Average Rating", f"{avg_ratings:.1f}")

st.markdown("---")

# Pie Chart - Sales by Fat Content
st.subheader("🥧 Sales Distribution by Item Fat Content")
sales_by_fat = df.groupby('Item Fat Content')['Sales'].sum()

fig1, ax1 = plt.subplots()
ax1.pie(sales_by_fat, labels=sales_by_fat.index, autopct='%.1f%%', startangle=90)
ax1.axis('equal')
st.pyplot(fig1)

# Bar Chart - Sales by Item Type
st.subheader("📦 Total Sales by Item Type")
sales_by_type = df.groupby('Item Type')['Sales'].sum().sort_values(ascending=False)

fig2, ax2 = plt.subplots(figsize=(10, 6))
bars = ax2.bar(sales_by_type.index, sales_by_type.values)
ax2.set_xticklabels(sales_by_type.index, rotation=90)
ax2.set_ylabel("Total Sales")
ax2.set_title("Sales by Item Type")
st.pyplot(fig2)

# Grouped Bar Chart - Outlet Tier vs Fat Content
st.subheader("🏬 Outlet Tier by Item Fat Content")
grouped = df.groupby(['Outlet Location Type', 'Item Fat Content'])['Sales'].sum().unstack()
grouped = grouped[['Regular', 'Low Fat']]

fig3, ax3 = plt.subplots(figsize=(8, 5))
grouped.plot(kind='bar', ax=ax3)
ax3.set_xlabel("Outlet Location Type")
ax3.set_ylabel("Total Sales")
ax3.set_title("Outlet Tier by Item Fat Content")
st.pyplot(fig3)

# Line Chart - Sales by Establishment Year
st.subheader("📈 Sales by Outlet Establishment Year")
sales_by_year = df.groupby('Outlet Establishment Year')['Sales'].sum().sort_index()

fig4, ax4 = plt.subplots(figsize=(9, 5))
ax4.plot(sales_by_year.index, sales_by_year.values, marker='o', linestyle='-')
ax4.set_xlabel("Establishment Year")
ax4.set_ylabel("Total Sales")
ax4.set_title("Outlet Establishment vs Sales")
st.pyplot(fig4)

# Pie Chart - Sales by Outlet Size
st.subheader("🏠 Sales by Outlet Size")
sales_by_size = df.groupby('Outlet Size')['Sales'].sum()

fig5, ax5 = plt.subplots(figsize=(4, 4))
ax5.pie(sales_by_size, labels=sales_by_size.index, autopct='%1.1f%%', startangle=90)
ax5.set_title("Sales by Outlet Size")
st.pyplot(fig5)

# Bar Chart - Sales by Location
st.subheader("📍 Sales by Outlet Location Type")
sales_by_location = df.groupby('Outlet Location Type')['Sales'].sum().sort_values(ascending=False)

fig6, ax6 = plt.subplots(figsize=(8, 3))
sns.barplot(x='Sales', y='Outlet Location Type', data=sales_by_location.reset_index(), ax=ax6)
ax6.set_title("Sales by Outlet Location")
st.pyplot(fig6)

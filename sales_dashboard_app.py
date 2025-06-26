import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set page config
st.set_page_config(
    page_title="Sales Data Analysis & Forecasting",
    page_icon=None,
    layout="wide"
)

st.write("✅ This is Kirti's updated dashboard live now")

# Load data
df = pd.read_csv(r'E:\sales data project\retail_sales_dataset.csv')

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Extract Year for filtering
df['Year'] = df['Date'].dt.year

# Sidebar filter for year
st.sidebar.title("Filter Options")
selected_year = st.sidebar.selectbox("Select Year:", sorted(df['Year'].unique()))

# Filter data for selected year
filtered_data = df[df['Year'] == selected_year]

# App title
st.title("📊 Sales Data Analysis & Forecasting Dashboard")

# Show basic metrics
total_sales = filtered_data['Total Amount'].sum()
total_transactions = filtered_data.shape[0]
average_sales = filtered_data['Total Amount'].mean()

col1, col2, col3 = st.columns(3)
col1.metric("💰 Total Sales", f"₹{total_sales:,.0f}")
col2.metric("📝 Total Transactions", total_transactions)
col3.metric("📊 Average Sale Amount", f"₹{average_sales:,.2f}")

st.markdown("---")

# Total Sales Over Time chart
st.subheader("📈 Total Sales Over Time")

sales_over_time = filtered_data.groupby('Date')['Total Amount'].sum()

if not sales_over_time.empty:
    st.line_chart(sales_over_time)
else:
    st.write("⚠️ No sales data available for this year.")

st.markdown("---")

# Product Category Sales distribution
st.subheader("🛍️ Sales by Product Category")
if not filtered_data.empty:
    category_sales = filtered_data.groupby('Product Category')['Total Amount'].sum().sort_values(ascending=False)
    st.bar_chart(category_sales)
else:
    st.write("⚠️ No product category data available for this year.")

st.markdown("---")

# Gender Sales Pie Chart
st.subheader("👥 Sales Distribution by Gender")
if not filtered_data.empty:
    gender_sales = filtered_data.groupby('Gender')['Total Amount'].sum()

    fig, ax = plt.subplots()
    ax.pie(gender_sales, labels=gender_sales.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    st.pyplot(fig)
else:
    st.write("⚠️ No gender-based data available for this year.")

st.markdown("---")

# 📊 Sales by Age Group
st.subheader("📊 Sales by Age Group")
if not filtered_data.empty:
    age_group_sales = filtered_data.groupby('Age')['Total Amount'].sum().sort_index()
    st.bar_chart(age_group_sales)
else:
    st.write("⚠️ No age group data available for this year.")

st.markdown("---")

# 🥇 Top 5 Customers by Total Sales
st.subheader("🥇 Top 5 Customers by Total Sales")
if not filtered_data.empty:
    top_customers = filtered_data.groupby('Customer ID')['Total Amount'].sum().sort_values(ascending=False).head(5)

    fig2, ax2 = plt.subplots()
    top_customers.plot(kind='bar', ax=ax2, color='skyblue')
    ax2.set_ylabel("Total Sales (₹)")
    ax2.set_xlabel("Customer ID")
    st.pyplot(fig2)
else:
    st.write("⚠️ No customer sales data available for this year.")

st.markdown("---")

# Footer
st.caption("Built with ❤️ using Streamlit | Kirti Goyal's Sales Data Project")

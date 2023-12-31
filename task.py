
## below python should be able to do below things.
# - Compute the total revenue generated by the online store for each month in the dataset.
# - Compute the total revenue generated by each product in the dataset.
# - Compute the total revenue generated by each customer in the dataset.
# - Identify the top 10 customers by revenue generated.

## revenue = product_price * quantity

import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('orders.csv')

# Convert the 'order_date' column to a datetime format
df['order_date'] = pd.to_datetime(df['order_date'])

# total revenue generated by the online store for each month
df['revenue'] = df['product_price'] * df['quantity']
monthly_revenue = df.groupby(df['order_date'].dt.to_period('M'))['revenue'].sum()

# total revenue generated by each product
product_revenue = df.groupby('product_name')['revenue'].sum()

# total revenue generated by each customer
customer_revenue = df.groupby('customer_id')['revenue'].sum()

# Identify the top customers by revenue generated, pass the number of customer to nlargest
top_customers = customer_revenue.nlargest(5)

print("Monthly Revenue:")
print(monthly_revenue)

print("\nProduct Revenue:")
print(product_revenue)

print("\nCustomer Revenue:")
print(customer_revenue)

print("\nTop 5 Customers by Revenue:")
print(top_customers)
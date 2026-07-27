import pandas as pd
from sqlalchemy import create_engine, text

#create engine
engine = create_engine("mysql+mysqldb://root:password@localhost:3306/classicmodels")

sql_query_order = """ SELECT orderNumber, productCode,priceEach, orderLineNumber, quantityOrdered FROM orderdetails; """
 
SQL_Query_product = """ SELECT * FROM products """;

with engine.connect() as my_conn:
  	# Use pandas read_sql() to read data from the database into a dataframe.
	  
    #Using Product table
 	#  my_data = pd.read_sql(text(SQL_Query_product),my_conn)
     
    # We can specify the index column using index_col parameter as shown below.
    # products_df = pd.read_sql(text(SQL_Query_product),my_conn, index_col ='productCode')
# print(products_df)

# Using Order Details Table
    orders_prod_df = pd.read_sql(text(sql_query_order),my_conn)
print("Sample of the 'orders' DataFrame:")
print(orders_prod_df.head())
 

#print all records from table
# print(my_data.head(10))

#  Print only specific columns using the Pandas square [ ] attribute.
# print(my_data[['productCode','productName']].head(10))

# Perform Exploratory Data Analysis (EDA).
# print("\nBasic Statistics:")
# print(products_df.describe())

# # Check data types.
# print('\n', products_df.dtypes)

#  Find the number of rows and columns.
# print(products_df.shape) # Get the number of rows and columns
# print(products_df.shape[0]) # Get the number of rows only
# print(products_df.shape[1]) # Get the number of columns only

# Check for missing values.
# print("\nMissing Values:")
# print(products_df.isnull().sum())

# Grouping and Aggregations
# grouped_df = products_df.groupby('productLine').agg({'quantityInStock': 'sum', 'buyPrice': 'mean'}).reset_index()
# print("\nGrouped Data:")
# print(grouped_df)

# From Order details table data
orders_prod_df['totalCost'] = orders_prod_df['priceEach'] * orders_prod_df['quantityOrdered']

# Group by 'orderNumber' and sum 'totalCost' for each group
grouped_df = orders_prod_df.groupby('orderNumber')['totalCost'].sum().reset_index()
print(grouped_df)

import pandas as pd

# # create empty dataframe
# df = pd.DataFrame()

# # Created a new column with some data
# df['SQL'] = [78,89,90] 

# df['Python'] = [67,78,99]

# # Insert a new row
# df.loc[len(df)] = [78,89]
# print(df)

# ===============================

# data = { 'apples sales': [3,2,0,1,9,6,3,2,7], 'oranges sales': [0,3,7,2,2,5,8,7,1]   }

# # years = list(range(2000, 2000 + len(data['apples sales'])))

# # OR

# years = pd.RangeIndex(2000,2009)

# # OR Increment years by 2 
# # years = pd.RangeIndex(2000,2009, step=2)

# sales_df = pd.DataFrame(data, index=years)

# # print(sales_df)
# # print(sales_df.shape)
# # print(sales_df.dtypes)
# print(type(sales_df["apples sales"]))

# We can access an index or label using “index” attributes, as shown below:

# print(sales_df.index) # get index information.
# print(sales_df.index[0]) # get first row label .
# print(sales_df.index[-1]) # get last row label.
# print(sales_df.index.values) # get indexes as an array.
# print(sales_df.index.tolist()) # get index as a list.

# ===============================

# employee_df = pd.read_csv('./data/employee.csv', index_col=0)

# # print(employee_df)
# print(employee_df.info())

# print('=========== JSON File ============')

# cars_df = pd.read_json('./data/cars.json')

# # print(cars_df.describe())  # Numerical columns only
# print(cars_df.describe(include='all')) # To include non-numeric columns


print('=========== Column Attribute  ============')

# Create DataFrame from a dictionary
student_dict = {    'Name': ['Joe', 'Nat', 'Harry'],  'Age': [20, 21, 19],  'Marks': [85.10, 77.80, 91.54]}
student_df = pd.DataFrame(student_dict)

# Get the column names as a Pandas Index object
# columns_index = student_df.columns
# print("Columns (Index):", columns_index)

# # Get the label of the first column
# first_column = student_df.columns[0]
# print("First Column Name:", first_column)

# # Get the column names as a list
# columns_list = student_df.columns.tolist()
# print("Columns (List):", columns_list)


# ========== Access the column data ========

# print(student_df[["Name", "Age"]])
# print(student_df["Age"].value_counts(ascending=False))

# print(student_df["Marks"].values.tolist())
      
#================== Rename Column Name  or Index ===========
technologies = (
    {'Courses':["Spark","PySpark","Hadoop","Python","pandas","Oracle","Java"],
     'Fee' :[20000,25000,26000,22000,24000,21000,22000],
     'Duration':['30day', '40days' ,'35days', '40days', '60days', '50days', '55days']
    })
df = pd.DataFrame(technologies)
print(df.columns)

# Rename a Single Column 
df2=df.rename(columns = {'Courses':'Courses_Name'}) # rename the column from Courses to Courses_Name.
print(df2.columns)


df.insert(1, 'Available', False)
print(df)
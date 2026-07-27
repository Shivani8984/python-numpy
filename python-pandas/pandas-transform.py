import pandas as pd

# # Loading the datasets  
# store_info_df = pd.read_csv('./data/store_info.csv')
# trans1_df = pd.read_csv('./data/transaction1.csv')
# trans2_df = pd.read_csv('./data/transactions2.csv')

# # combine the transactions
# combine_trans_df = pd.concat([trans1_df, trans2_df], ignore_index=True)
# print(combine_trans_df)

# # Merging two datasets by common column / Index

#     # merge the store info with the transactions
# merged_trans_df = pd.merge(combine_trans_df, store_info_df, on="StoreID")
# print('\n ', merged_trans_df)

demoData_One = {
  'subject_id': ['1', '2', '3', '4', '5'],
  'student_name': ['Mark', 'Khalid', 'Deborah', 'Trevon', 'Raven']
}
df1 = pd.DataFrame(demoData_One, columns=['subject_id', 'student_name'])
print(df1)
demoData_Two = {
  'subject_id': ['4', '5', '6', '7', '8'],
  'student_name': ['Eric', 'Imani', 'Cece', 'Darius', 'Andre']
}
df2 = pd.DataFrame(demoData_Two, columns=['subject_id', 'student_name'])
print(df2)

students_df = pd.merge(df1, df2, on='subject_id')
print('\n ', students_df)

df3=df1.join(df2, lsuffix="_left", rsuffix="_right")
print("After joining two DataFrames:\n", df3)
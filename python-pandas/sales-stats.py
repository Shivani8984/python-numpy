import pandas as pd

# Load the datatsets
trans1_df = pd.read_csv('./data/transaction1.csv')
trans2_df = pd.read_csv('./data/transactions2.csv')

# print(trans1_df)
# print('\n', trans2_df)

combine_trans_df  = pd.concat([trans1_df, trans2_df], ignore_index=True)
# print(combine_trans_df)
# print(combine_trans_df.info())          # Gives info about columns
# print(combine_trans_df.describe())      # Gives description like mean,count,std,min about datatset

category_group = combine_trans_df.groupby("Category")
# print(category_group)   # gives only object information

# print(category_group.get_group("Home"))
# print(category_group.get_group("Electronics"))

# Group and aggregate data
# category_group_byaggregation= combine_trans_df.groupby("Category")["SalesAmount"].agg(sum)
# category_group_byaggregation= combine_trans_df.groupby("Category")["SalesAmount"].agg(["sum", "mean", "median"])
# category_group_byaggregation.columns = ["Total Sales", "Average", "Middle"] #Renaming the column
# print(category_group_byaggregation)

# Pivot table func
# stats = combine_trans_df.pivot_table("SalesAmount", "StoreID", aggfunc=["count", "sum"])
# print(stats)

combine_trans_df = combine_trans_df.sort_values(by=["StoreID", "Date"])

# print('\n',"================CUMSUM============")
combine_trans_df['Cumulative_Sales'] = combine_trans_df.groupby("StoreID")["SalesAmount"].cumsum()
# combine_trans_df['Cumulative_Sales'] = combine_trans_df.groupby("StoreID")["SalesAmount"].agg("cumsum")
# print(combine_trans_df)


print('\n',"================TRANSFORM============")
combine_trans_df["Total"] = combine_trans_df.groupby("StoreID")["SalesAmount"].transform("sum")
print(combine_trans_df)

print('\n',"================DIFF============")
combine_trans_df["Trend"] = combine_trans_df.groupby("StoreID")["SalesAmount"].diff()
print(combine_trans_df)


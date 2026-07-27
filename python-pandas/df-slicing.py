import pandas as pd

df = pd.read_csv('./data/employee.csv')

# print(df.loc[:5])
# print(df.loc[1:4])
# print(df.iloc[1:4])

#            [rows:rows, columns:columns]
# print(df.iloc[1:5,       1:3])

# print(df.loc[1:5,"Name": "Weight"])


# ====== Working with missing values ========

# print(df.isnull())

# ------- Filling the missing data
# df["Age"] = df["Age"].fillna(18, inplace=True)
# df["Salary"] = df["Salary"].fillna(25000, inplace=True)

# # Fill weight with average value
# df.fillna({"Weight": df["Weight"].mean()}, inplace=True)
# print(df)

# --------- Drops rows with missing values  ----------

# df = df.dropna()
# print(df)

# -- replace dat with new value
# df = df.replace("James", "Rihana")

# df.loc[:, "newCol"] = True
# df["newCol"] = df["newCol"].replace(False, True)
# print(df)


# ----------- Date Range Function ----------

# print(pd.to_datetime("2026-07-21"))
# print(pd.date_range("2026-01-01", "2026-01-13"))

# ---------Creating a date range with periods--------
#  will generate a pandas DateTimeIndex containing 10 dates evenly spaced
print(pd.date_range(start='01-01-2026', end='07-31-2026', periods=10))

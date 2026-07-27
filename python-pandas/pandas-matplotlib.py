import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# Line plot graph using matplotlib.pyplot with State-based approach:
# Example One: With Line
xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

df = pd.read_csv('./data/transaction1.csv')
# print(df)

# plt.plot(df["TransactionID"], df["SalesAmount"])
# df["SalesAmount"].hist()
# df["SalesAmount"].plot(kind="pie")
# plt.show()

# plt.plot(xpoints, ypoints) #Creates the plot
# plt.show() #Open the graph

# Example Two: Without Line
# plt.plot(xpoints, ypoints, '0')
# plt.show()

dates  = df["Date"]
sales = df["SalesAmount"]

# plt.plot(
#     dates,
#     sales,
#     marker='o',
#     color="red",
#     linewidth=2,
#     label="Sales Data",
#     # xlabel="Date",
#     # ylabel="Amount",
#     linestyle="--"
# )
# plt.show()

# Create the objects
fig, ax = plt.subplots()
fig.suptitle("2026 Sales")
ax.plot(dates, sales)
plt.show()
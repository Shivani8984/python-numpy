import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# Line plot graph using matplotlib.pyplot with State-based approach:
# Example One: With Line
xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

df = pd.read_csv('./data/transaction1.csv')
df1 = pd.read_csv('./data/transactions2.csv')
 
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
# plt.hist(sales)
# plt.plot(dates,sales, 'o')

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
# fig, ax = plt.subplots()
# fig.suptitle("2026 Sales")
# ax.plot(dates, sales)
# plt.show()

plt.title("Sales Data", fontweight="bold", fontfamily="monospace", fontsize=28)

plt.xlabel("Date", color="green", fontsize=14, fontweight='bold')

plt.ylabel('Amount', color="green", fontsize=14, fontweight='bold')

plt.grid()

# create a new subplot
plt2 = plt.subplot(1,2,2)
# plot the new data
plt2.plot(df1["Date"], df1["SalesAmount"])
# plt.tight_layout(pad=2.5)

# create the figure and axes objects
# fig, ax = plt.subplots()

# fig.suptitle('2026 Sales')

# ax.set_title('Axes', loc='left', fontstyle='oblique', fontsize='medium')
# ax.plot(dates, sales)

plt.show()
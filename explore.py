import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
pd.set_option("display.float_format", "{:.2f}".format)

df = pd.read_csv("austin_home_sales.csv")

print(df.shape)
print(df.describe())

plt.scatter(df["Sq_Footage"], df["Sale_Price"])
plt.xlabel("Sq_Footage")
plt.ylabel("Sale_Price")
plt.tight_layout()
plt.savefig("scatter.png")
plt.close()

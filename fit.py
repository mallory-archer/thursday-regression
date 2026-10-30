import pandas as pd
from statsmodels.formula.api import ols

df = pd.read_csv("austin_home_sales.csv")

model = ols(
    "Sale_Price ~ Sq_Footage + Bedrooms + Home_Age_Years + Dist_Downtown_Mi",
    data=df,
).fit()

print(model.summary())

for name, coefficient in model.params.items():
    print(f"{name} coefficient: {coefficient:.0f}")

for name, pvalue in model.pvalues.items():
    print(f"{name} p-value: {pvalue:.4f}")

print(f"R-squared: {model.rsquared:.4f}")
print(f"Adjusted R-squared: {model.rsquared_adj:.4f}")

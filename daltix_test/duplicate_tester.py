import pandas as pd

df = pd.read_csv("products.csv")

print("The ammount of duplicate results is: " + str(df['url'].duplicated().sum()))

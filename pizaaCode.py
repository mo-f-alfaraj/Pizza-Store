import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import Data
pizzaStore = pd.read_csv(r"D:\Work\Projects\Pizza\pizza.csv")

# Data Viewing & Preprocessing
pizzaStore.info()
print(pizzaStore.isna().sum())

# Replace Columns Titles 
pizzaStore= pizzaStore.rename(columns={'company': 'branch'})
pizzaStore.columns = pizzaStore.columns.str.replace('_', ' ').str.title()

# Replace Columns Values 
pizzaStore = pizzaStore.apply(lambda col: col.str.replace('_', ' ').str.title() if col.dtype == 'object' else col)
pizzaStore['Branch'] = pizzaStore['Branch'].replace(['A', 'B', 'C', 'D', 'E'], ['Mumbai', 'Delhi', 'Bengaluru', 'Hyderabad', 'Calcutta'], regex=True).astype(str)
pizzaStore['Price Rupiah'] = pizzaStore['Price Rupiah'].replace('[Rp,]', '', regex=True).astype(float)
pizzaStore['Diameter'] = pizzaStore['Diameter'].replace('[ Inch]', '', regex=True).astype(float)

print(pizzaStore)

# Save New Data
pizzaStore.to_csv(r"D:\Work\Projects\Pizza\pizza_mod.csv")
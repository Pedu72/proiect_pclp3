import pandas as pd
import numpy as np

# -=-=-=-=-=-=-=- Task 1 -=-=-=-=-=-=-=- #

file = 'train.csv'
data = pd.read_csv(file)

print("-=-=-=-=-=-=-=- Task 1 -=-=-=-=-=-=-=-\n")

cols = len(data.columns)
print(f"Numarul de coloane este {cols}.\n")

types = data.dtypes
print(f"Tipurile de date pentru fiecare coloana: \n{types}\n")

miss = data.isnull().sum()
print(f"Numarul de date lipsa pentru fiecare coloana: \n{miss}\n")

rows = data.shape[0]
print(f"Numarul de randuri este {rows}.\n")

dups = data.duplicated().sum()
print(f"Numarul de randuri duplicate este {dups}.\n")



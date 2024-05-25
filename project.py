import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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



# -=-=-=-=-=-=-=- Task 1 -=-=-=-=-=-=-=- #

print("\n\n-=-=-=-=-=-=-=- Task 2 -=-=-=-=-=-=-=-\n")

counter = data['Survived'].value_counts()
survived = counter[1] / rows * 100
dead = counter[0] / rows * 100
print(survived)
print(dead)
print(f"Pe nava {survived:.2f}% dintre pasageri au supravietuit, iar {dead:.2f}% si-au pierdut viata")

x = np.array(["Supravietuitori", "Morti"])
y = np.array([survived, dead])
colors = np.array(["Green", "Red"])

plt.bar(x, y, color = colors)
plt.title('Supravietuitori')
plt.show()



counter = data['Pclass'].value_counts()
class_1 = counter[1] / rows * 100
class_2 = counter[2] / rows * 100
class_3 = counter[3] / rows * 100
print(f"Pe nava {class_1:.2f}% dintre pasageri au stat la clasa I, {class_2:.2f}% la clasa a II-a, iar {class_3:.2f}% la clasa a III-a.")

x = np.array(["Clasa I", "Clasa a II-a", "Clasa a III-a"])
y = np.array([class_1, class_2, class_3])
colors = np.array(["Green", "Blue", "Purple"])

plt.bar(x, y, color = colors)
plt.title('Clasa')
plt.show()



counter = data['Sex'].value_counts()
males = counter['male'] / rows * 100
females = counter['female'] / rows * 100
print(f"Pe nava {males:.2f}% dintre pasageri au fost barbati, iar {females:.2f}% femei.")

x = np.array(["Barbati", "Femei"])
y = np.array([males, females])
colors = np.array(["Blue", "Purple"])

plt.bar(x, y, color = colors)
plt.title('Sex')
plt.show()
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -=-=-=-=-=-=-=-=-=-=- Task 1 -=-=-=-=-=-=-=-=-=-=- #

file = 'train.csv'
data = pd.read_csv(file)

print("-=-=-=-=-=-=-=-=-=-=- Task 1 -=-=-=-=-=-=-=-=-=-=-\n")

cols = len(data.columns)
print(f"Numarul de coloane este {cols}.\n")

types = data.dtypes
print(f"Tipurile de date pentru fiecare coloana: \n{types}\n")

miss = data.isnull().sum()
print(f"Numarul de date lipsa pentru fiecare coloana: \n{miss}\n")

rows = len(data)
print(f"Numarul de randuri este {rows}.\n")

dups = data.duplicated().sum()
print(f"Numarul de randuri duplicate este {dups}.\n")



# -=-=-=-=-=-=-=-=-=-=- Task 2 -=-=-=-=-=-=-=-=-=-=- #

print("\n\n-=-=-=-=-=-=-=-=-=-=- Task 2 -=-=-=-=-=-=-=-=-=-=-\n")

counter = data['Survived'].value_counts()
surv = counter[1]
dead = counter[0]
print(f"Pe nava {surv / rows * 100:.2f}% dintre pasageri au supravietuit, iar {dead / rows * 100:.2f}% si-au pierdut viata")

values = np.array([surv / rows * 100, dead / rows * 100])
labels = np.array(["Supravietuitori", "Morti"])
colors = np.array(["Green", "Red"])

plt.pie(values, labels = labels, colors = colors)
plt.title('Supravietutori')
plt.show()



counter = data['Pclass'].value_counts()
class_1 = counter[1]
class_2 = counter[2]
class_3 = counter[3]
print(f"Pe nava {class_1 / rows * 100:.2f}% dintre pasageri au stat la clasa I, {class_2 / rows * 100:.2f}% la clasa a II-a, iar {class_3 / rows * 100:.2f}% la clasa a III-a.")

values = np.array([class_1 / rows * 100, class_2 / rows * 100, class_3 / rows * 100])
labels = np.array(["Clasa I", "Clasa a II-a", "Clasa a III-a"])
colors = np.array(["Green", "Blue", "Purple"])

plt.pie(values, labels = labels, colors = colors)
plt.title('Clasa')
plt.show()



counter = data['Sex'].value_counts()
males = counter['male']
females = counter['female']
print(f"Pe nava {males / rows * 100:.2f}% dintre pasageri au fost barbati, iar {females / rows * 100:.2f}% femei.\n")

values = np.array([males / rows * 100, females / rows * 100])
labels = np.array(["Barbati", "Femei"])
colors = np.array(["Cyan", "Pink"])

plt.pie(values, labels = labels, colors = colors)
plt.title('Sex')
plt.show()



# -=-=-=-=-=-=-=-=-=-=- Task 3 -=-=-=-=-=-=-=-=-=-=- #

print("\n\n-=-=-=-=-=-=-=-=-=-=- Task 3 -=-=-=-=-=-=-=-=-=-=-\n")

plt.hist(data['Age'])
plt.title('Varsta')
plt.show()

plt.hist(data['SibSp'])
plt.title('Numarul de Frati/Surori si Soti/Sotii ai unei persoane la bord')
plt.show()

plt.hist(data['Parch'])
plt.title('Numarul de Parinti si Copii ai unei persoane la bord')
plt.show()

plt.hist(data['Fare'])
plt.title('Pretul platit pe Bilet')
plt.show()



# -=-=-=-=-=-=-=-=-=-=- Task 4 -=-=-=-=-=-=-=-=-=-=- #

print("\n\n-=-=-=-=-=-=-=-=-=-=- Task 4 -=-=-=-=-=-=-=-=-=-=-\n")

miss_cols = miss[miss != 0].index

for col in miss_cols:
    miss_num = data[col].isnull().sum()
    print(f"Din coloana {col} lipsesc {miss_num} din cele {rows} valori.")

    miss_num_surv = data.loc[data['Survived'] == 1, col].isnull().sum()
    print(f"Pentru {miss_num_surv / surv * 100:.2f}% dintre supravietuitori nu se cunosc informatiile pentru campul {col}.")

    miss_num_dead = data.loc[data['Survived'] == 0, col].isnull().sum()
    print(f"Pentru {miss_num_dead / dead * 100:.2f}% dintre morti nu se cunosc informatiile pentru campul {col}.\n")



# -=-=-=-=-=-=-=-=-=-=- Task 5 -=-=-=-=-=-=-=-=-=-=- #

print("\n\n-=-=-=-=-=-=-=-=-=-=- Task 5 -=-=-=-=-=-=-=-=-=-=-\n")

age_cat = []
age_count = [0] * 5

for age in data['Age']:
    if pd.isnull(age):
        age_cat.append(np.nan)
        age_count[0] = age_count[0] + 1

    elif age <= 20:
        age_cat.append(1)
        age_count[1] = age_count[1] + 1

    elif age <= 40:
        age_cat.append(2)
        age_count[2] = age_count[2] + 1

    elif age <= 60:
        age_cat.append(3)
        age_count[3] = age_count[3] + 1
        
    else:
        age_cat.append(4)
        age_count[4] = age_count[4] + 1

data.insert(len(data.columns), 'AgeCategory', age_cat)

print("Nuarul de persoane pentru fiecare categorie de varsta:")
print(f"[ 0,  20]:    {age_count[1]:d}")
print(f"[21,  40]:    {age_count[2]:d}")
print(f"[41,  60]:    {age_count[3]:d}")
print(f"[61, max]:    {age_count[4]:d}")
print(f"Necunoscut    {age_count[0]:d}\n")

values = age_count
labels = np.array(["Necunoscut", "[0, 20]", "[21, 40]", "[41, 60]", "[61, max]"])
colors = np.array(["Gray", "Red", "Green", "Blue", "Purple"])

plt.bar(labels, values, color = colors)
plt.title('Categoria de Varsta')
plt.show()



# -=-=-=-=-=-=-=-=-=-=- Task 6 -=-=-=-=-=-=-=-=-=-=- #

print("\n\n-=-=-=-=-=-=-=-=-=-=- Task 6 -=-=-=-=-=-=-=-=-=-=-\n")

surv_male_age = [0] * 5

surv_male = data[data['Survived'] == 1]
surv_male = surv_male[surv_male['Sex'] == 'male']

for i in range(5):
    surv_male_age[i] = len(surv_male[surv_male['AgeCategory'] == i])

print("Nuarul de barbati supravietuitori pentru fiecare categorie de varsta:")
print(f"[ 0,  20]:    {surv_male_age[1]:d}")
print(f"[21,  40]:    {surv_male_age[2]:d}")
print(f"[41,  60]:    {surv_male_age[3]:d}")
print(f"[61, max]:    {surv_male_age[4]:d}")
print(f"Necunoscut    {surv_male_age[0]:d}\n")

values = surv_male_age
labels = np.array(["Necunoscut", "[0, 20]", "[21, 40]", "[41, 60]", "[61, max]"])
colors = np.array(["Gray", "Red", "Green", "Blue", "Purple"])

plt.bar(labels, values, color = colors)
plt.title('Categoria de Varsta pentru Barbatii Supravietuitori')
plt.show()



# -=-=-=-=-=-=-=-=-=-=- Task 6 -=-=-=-=-=-=-=-=-=-=- #

print("\n\n-=-=-=-=-=-=-=-=-=-=- Task 6 -=-=-=-=-=-=-=-=-=-=-\n")
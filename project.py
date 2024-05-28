import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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
plt.savefig('out/2_1 - Supravietuitori')
plt.clf()



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
plt.savefig('out/2_2 - Clasa')
plt.clf()



counter = data['Sex'].value_counts()
males = counter['male']
females = counter['female']
print(f"Pe nava {males / rows * 100:.2f}% dintre pasageri au fost barbati, iar {females / rows * 100:.2f}% femei.\n")

values = np.array([males / rows * 100, females / rows * 100])
labels = np.array(["Barbati", "Femei"])
colors = np.array(["Cyan", "Pink"])

plt.pie(values, labels = labels, colors = colors)
plt.title('Sex')
plt.savefig('out/2_3 - Sex')
plt.clf()





# -=-=-=-=-=-=-=-=-=-=- Task 3 -=-=-=-=-=-=-=-=-=-=- #

print("\n\n-=-=-=-=-=-=-=-=-=-=- Task 3 -=-=-=-=-=-=-=-=-=-=-\n")

plt.hist(data['Age'])
plt.title('Varsta')
plt.savefig('out/3_1 - Varsta')
plt.clf()

plt.hist(data['SibSp'])
plt.title('Numarul de Frati/Surori si Soti/Sotii ai unei persoane la bord')
plt.savefig('out/3_2 - SibSp')
plt.clf()

plt.hist(data['Parch'])
plt.title('Numarul de Parinti si Copii ai unei persoane la bord')
plt.savefig('out/3_3 - Parch')
plt.clf()

plt.hist(data['Fare'])
plt.title('Pretul platit pe Bilet')
plt.savefig('out/3_4 - Pretul platit pe Bilet')
plt.clf()




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
plt.savefig('out/5 - Categoria de Varsta')
plt.clf()





# -=-=-=-=-=-=-=-=-=-=- Task 6 -=-=-=-=-=-=-=-=-=-=- #

print("\n\n-=-=-=-=-=-=-=-=-=-=- Task 6 -=-=-=-=-=-=-=-=-=-=-\n")

surv_male_age = [0] * 5

surv_male = data[(data['Survived'] == 1) & (data['Sex'] == 'male')]

for i in range(5):
    surv_male_age[i] = len(surv_male[surv_male['AgeCategory'] == i])


print("Nuarul de barbati supravietuitori pentru fiecare categorie de varsta:")
print(f"[ 0,  20]:    {surv_male_age[1]:d}")
print(f"[21,  40]:    {surv_male_age[2]:d}")
print(f"[41,  60]:    {surv_male_age[3]:d}")
print(f"[61, max]:    {surv_male_age[4]:d}")
print(f"Necunoscut    {surv_male_age[0]:d}\n")

data['Children'] = data['Age'] < 18
surv_male_cat = data[data['Sex'] == 'male'].groupby(['AgeCategory', 'Survived']).size().unstack(fill_value = 0)
surv_male_cat.plot(kind = 'bar', figsize=(14, 7), color = ['red', 'green'])

plt.title('Categoria de Varsta pentru Barbatii Supravietuitori')
plt.savefig('out/6 - Cetegora de Varsta pentru Barbatii Supravietuitori')
plt.clf()





# -=-=-=-=-=-=-=-=-=-=- Task 7 -=-=-=-=-=-=-=-=-=-=- #

print("\n\n-=-=-=-=-=-=-=-=-=-=- Task 7 -=-=-=-=-=-=-=-=-=-=-\n")

children = len(data[data['Age'] < 18])
print(f"Pe nava {children / rows * 100:.2f}% dintre pasageri au fost copii.\n")

data['Children'] = data['Age'] < 18
children_surv = data.groupby(['Children', 'Survived']).size().unstack(fill_value = 0)
children_surv.plot(kind = 'bar', figsize=(14, 7), color = ['red', 'green'])

plt.title('Rata de Supravietuire - Copii VS Adulti')
plt.savefig('out/7 - Rata de Supravietuire - Copii VS Adulti')
plt.clf()





# -=-=-=-=-=-=-=-=-=-=- Task 8 -=-=-=-=-=-=-=-=-=-=- #

print("\n\n-=-=-=-=-=-=-=-=-=-=- Task 8 -=-=-=-=-=-=-=-=-=-=-\n")

for survived in [0, 1]:
    age_mean = round(data[data['Survived'] == survived]['Age'].mean())
    age_cat_mean = np.floor(age_mean / 20)
    if age_cat_mean > 4:
        age_cat_mean = 4

    data.loc[data['Survived'] == survived, 'Age'] = data.loc[data['Survived'] == survived, 'Age'].fillna(age_mean)
    data.loc[data['Survived'] == survived, 'AgeCategory'] = data.loc[data['Survived'] == survived, 'AgeCategory'].fillna(age_cat_mean)


for pclass in [1, 2, 3]:
    cabin_mode = data[data['Pclass'] == pclass]['Cabin'].mode()[0]
    embarked_mode = data[data['Pclass'] == pclass]['Embarked'].mode()[0]

    data.loc[data['Pclass'] == pclass, 'Cabin'] = data.loc[data['Pclass'] == pclass, 'Cabin'].fillna(cabin_mode)
    data.loc[data['Pclass'] == pclass, 'Embarked'] = data.loc[data['Pclass'] == pclass, 'Embarked'].fillna(embarked_mode)


print(data.info())
print("")





# -=-=-=-=-=-=-=-=-=-=- Task 9 -=-=-=-=-=-=-=-=-=-=- #

print("\n\n-=-=-=-=-=-=-=-=-=-=- Task 9 -=-=-=-=-=-=-=-=-=-=-\n")

data['Title'] = data['Name'].str.extract(' ([A-Za-z]+)\.')
title_sex = data.groupby(['Title', 'Sex']).size().unstack(fill_value = 0)

print(title_sex)
print("")

title_sex.plot(kind = 'bar', figsize=(14, 7), color = ['pink', 'cyan'])
plt.title('Numarul de Persoane pentru fiecare Titlu')
plt.xticks(rotation = 25)
plt.legend()
plt.savefig('out/9 - Numarul de Persoane pentru fiecare Titlu')
plt.clf()





# -=-=-=-=-=-=-=-=-=-=- Task 10 -=-=-=-=-=-=-=-=-=-=- #

print("\n\n-=-=-=-=-=-=-=-=-=-=- Task 10 -=-=-=-=-=-=-=-=-=-=-\n")

data['IsAlone'] = (data['SibSp'] == 0) & (data['Parch'] == 0)

plt.hist(data[data['IsAlone']]['Survived'], alpha=0.7, label='Singuri', color='Gray', align = 'left')
plt.hist(data[~data['IsAlone']]['Survived'], alpha=0.7, label='Cu Rude', color='Orange', align = 'mid')
plt.legend()

plt.title('Supravietuirea in funtie de Existenta Rudelor')
plt.savefig('out/10_1 - Supravietuirea in funtie de Existenta Rudelor')
plt.clf()




catplot = sns.catplot(
    data = data.head(100),
    x = 'Pclass',
    y = 'Fare',
    hue = 'Survived',
    kind = 'swarm',
    s = 5
)

plt.title('Relatia dintre Tarif, Clasa si Supravietuire')
plt.savefig('out/10_2 - Relatia dintre Tarif, Clasa si Supravietuire')



data = data.drop(columns = ['Children', 'IsAlone', 'Title'])

data.to_csv('out/test_out.csv')

import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
import random
import plotly.express as ex
import matplotlib.ticker as mticker
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
plt.style.use('ggplot')

onefig_size = (10,4)
multifigs_size = (12,4)

#-------------------------
original_df = pd.read_csv('/content/drive/MyDrive/IT502_/ASM2/prod2.csv')
original_df.head(10)
#-------------------------
original_df.info()
#-------------------------
original_df.describe()
#-------------------------
original_df.describe(include='object')
#-------------------------
original_df.isnull().sum()
#-------------------------
null_mask = original_df['PrimaryColor'].isnull()
null_values = original_df[null_mask]
print(null_values)
#-------------------------
original_df['PrimaryColor'].replace(np.nan, "Blue", inplace=True)
original_df.isnull().sum()
#-------------------------
null_mask = original_df['PrimaryColor'].isnull()
null_values = original_df[null_mask]
print(null_values)
#-------------------------
original_df_copy = original_df.copy()
#-------------------------
original_df["Gender"].value_counts()
#-------------------------
ex.pie(original_df,names='Gender',title='Propotion Of Gender',hole=0.33)
#-------------------------
data = {'Gender': ['Women', 'Men', 'Unisex', 'Boys', 'Girls', 'Unisex Kids'],
        'Count': [5126, 4591, 1188, 1100, 440, 46]}
original_df = pd.DataFrame(data)
g = original_df.plot(x='Gender', y='Count', kind='bar', color='pink')

for index, value in enumerate(original_df['Count']):
    plt.text(index, value, str(value), ha='center', va='bottom')
#-------------------------
new_df = pd.read_csv('/content/drive/MyDrive/IT502_/ASM2/prod2.csv')
#-------------------------
print(new_df.info())
#-------------------------
profit_by_gender = new_df.groupby('Gender')['Profit'].sum()

plt.figure(figsize=(10, 5))
plt.bar(profit_by_gender.index, profit_by_gender.values)

for index, value in enumerate(profit_by_gender.values):
    plt.annotate(f'{value:,.0f}', xy=(index, value), ha='center', va='bottom')

formatter = mticker.StrMethodFormatter('{x:,.0f} USD')
plt.gca().yaxis.set_major_formatter(formatter)

plt.xlabel('Gender')
plt.ylabel('Total Profit (USD)')
plt.title('Total Profit by Gender')
plt.show()
#-------------------------
original_df = pd.read_csv('/content/drive/MyDrive/IT502_/ASM2/prod2.csv', parse_dates=['Month'], dayfirst=True)
#-------------------------
plt.figure(figsize=(10, 5))
sns.lineplot(data=original_df, x='Month', y='Profit', hue='Gender', ci=None)
plt.title('Total Profit by Month and Gender')
plt.xlabel('Month')
plt.ylabel('Total Profit')
plt.xticks(rotation=45)
plt.legend(title='Gender', loc='upper left', bbox_to_anchor=(1, 1))
plt.show()
#-------------------------
plt.figure(figsize=(10, 5))
sns.boxplot(data=original_df, x='Gender', y='Profit')
plt.title('Boxplot of Profit by Gender')
plt.xlabel('Gender')
plt.ylabel('Profit')
plt.show()
#-------------------------
plt.figure(figsize=(10, 5))
sns.countplot(data=original_df, x='Gender', hue='PrimaryColor')
plt.title('Bar Chart of Gender and PrimaryColor')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.legend(title='PrimaryColor', loc='upper right')
plt.show()


import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
data=pd.read_csv(r"D:\college\course projects\eda cp\data_ecommerce_customer_churn.csv")
data.count()

df=pd.DataFrame(data)
df.head()

#median for numerical data
df['Tenure'].fillna(df['Tenure'].median(), inplace=True)
df['WarehouseToHome'].fillna(df['WarehouseToHome'].median(),inplace=True)
df['DaySinceLastOrder'].fillna(df['DaySinceLastOrder'].median(), inplace=True)
df.head()


#dropping null values
df.dropna()

df['Churn'].value_counts().plot(kind='pie',autopct='%1.1f%%')
plt.title("Customer Retention Overview")
plt.show()
#Overview purposes

plt.figure(figsize=(10,6))
sns.countplot(x='PreferedOrderCat',hue='Churn',data=df)
plt.show()
sns.countplot(x='MaritalStatus',hue='Churn',data=df)
plt.show()

df=pd.DataFrame(data)
churncat=df[df['Churn']==1]['PreferedOrderCat'].value_counts()
plt.figure(figsize=(10,6))
plt.bar(churncat.index,churncat.values,color='green')
plt.xlabel("Churned Customers Count")
plt.ylabel("Order Category")
plt.title("Churned Customers by Order Category")
plt.show()
#To focus on a particular category

plt.figure()
score = df['SatisfactionScore'].value_counts().sort_index()
plt.pie(score.values,labels=score.index,autopct='%1.1f%%')
plt.title("Satisfaction Score Distribution")
plt.show()
#To understand user experience
pd.crosstab(df['Complain'], df['Churn'], normalize='index').plot(kind='bar',stacked=True)
plt.title("Complaint Impact on Churn")
plt.show()
#tro understand correlation between user experience and customer support system
#distribution of data amongst numerical variables
#identification of outliers
num_vars = ['Tenure', 'WarehouseToHome', 'NumberOfAddress', 'NumberOfDeviceRegistered',
            'DaySinceLastOrder', 'CashbackAmount']

fig, axs = plt.subplots(nrows=6, ncols=1, figsize=(15, 20))
axs = axs.flatten()

for i, var in enumerate(num_vars):
    sns.violinplot(x=var, data=df, ax=axs[i])

fig.tight_layout()
fig.delaxes(axs[5])

plt.show()
#previous data separated by churn
fig, axs = plt.subplots(nrows=6, ncols=1, figsize=(15, 20))
axs = axs.flatten()

for i, var in enumerate(num_vars):
    sns.boxplot(y=var,x='Churn', hue='Churn',data=df, ax=axs[i])

fig.tight_layout()
fig.delaxes(axs[5])

plt.show()

sns.kdeplot(df[df['Churn']==1]['DaySinceLastOrder'], label='Churn')
sns.kdeplot(df[df['Churn']==0]['DaySinceLastOrder'], label='No Churn')
plt.legend()
plt.title("Recency vs Churn")
plt.show()

#recent customers churn more likely
#churns have been more recent   

sns.scatterplot(x='DaySinceLastOrder', y='CashbackAmount', data=df)
plt.show()

#previous data separated by churn
sns.scatterplot(x='DaySinceLastOrder', y='CashbackAmount', hue='Churn',data=df)
plt.show()
sns.heatmap(
    pd.crosstab(df['PreferedOrderCat'], df['Churn'], normalize='index'),
    annot=True,
    cmap='coolwarm'
)
plt.title("Churn Heatmap by Category")
plt.show()
#categorical heatmap

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv(r"C:\Users\priye\Downloads\loan_prediction_dataset.csv")

print(df.head(1))

print(df.info())

print(df.describe())

print(df.loc[0, "Age"])

print(df[
      (df["Age"]>60)
      &
      (df["Credit_Score"]>6)
      ]
      )

print(df.sort_values(
    "Credit_Score",
    ascending=False
    )
)

df.isnull().sum()

import matplotlib.pyplot as plt

approved = df[df['Loan_Approved'] == 1]
rejected = df[df['Loan_Approved'] == 0]

plt.hist(approved['Credit_Score'], alpha=0.5, label='Approved')
plt.hist(rejected['Credit_Score'], alpha=0.5, label='Rejected')

plt.title('Credit Score Distribution by Loan Approval')
plt.xlabel('Credit Score')
plt.ylabel('Number of Applicants')
plt.legend()

plt.show()

approved = df[df['Loan_Approved'] == 1]
rejected = df[df['Loan_Approved'] == 0]

plt.hist(approved['Income'], alpha=0.5, label='Approved')
plt.hist(rejected['Income'], alpha=0.5, label='Rejected')

plt.title('Income Distribution by Loan Approval')
plt.xlabel('Income')
plt.ylabel('Number of Applicants')
plt.legend()

plt.show()

plt.scatter(df['Income'], df['Credit_Score'])

plt.title('Income vs Credit Score')
plt.xlabel('Income')
plt.ylabel('Credit Score')

plt.show()

df.groupby('Employment_Status')['Loan_Approved'].mean().plot(kind='bar')

plt.title('Loan Approval Rate by Employment Status')
plt.xlabel('Employment Status')
plt.ylabel('Approval Rate')

plt.show()

df['Credit_Score'].hist(bins=20)

plt.title('Distribution of Credit Scores')
plt.xlabel('Credit Score')
plt.ylabel('Number of Applicants')

plt.show()

df.to_csv('loan_cleaned.csv', index=False)

import os
print(os.getcwd())
print(os.listdir())
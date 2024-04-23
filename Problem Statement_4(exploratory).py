import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv("C:/Users/GREESHMA/Downloads/SMA Practicals/linkedin_poll.csv")

print("\nShape of dataset:",df.shape)
print("\nFirst few rows of the dataset:",df.head())
print("\nDatatypes included in the dataset:",df.dtypes)
print("\nNumber of missing values in the dataset:",df.isna().sum())
print("\nDescription of the dataset: ")
print(df.describe())

#line plot
x=df['Quiz_number']
y=df['Total_Likes']
plt.plot(x,y)
plt.show()

#scatter plot
plt.scatter(x,y)
plt.show()

#histogram
sns.histplot(x=df['Max_Right'], binwidth=1)
plt.show()

#boxplot
cat_col=df['Max_Right']
num_col=df['Total_Likes']
sns.boxplot(x=cat_col,y=num_col,data=df)
plt.show()

#correlation matrix with heatmap
corr_matrix=df.corr()
sns.heatmap(corr_matrix,annot=True)
plt.show()

#bargraph
plt.bar(x,y)
plt.show()

#pie chart
data=df.head(10)['Total_Responses']
numm=df.head(10)['Max_Right']
plt.pie(data,labels=numm)
plt.title('x v/s y')
plt.show()

#violin plot
x=df.head(10)['Total_Responses']
y=df.head(10)['Max_Right']
sns.violinplot(x=x,y=y)
plt.show()

#hexbin
x=df.head(10)['Total_Responses']
y=df.head(10)['Right_Answers']
plt.hexbin(x,y,gridsize=10)
plt.show()

#area fill
plt.fill_between(x,y)
plt.show()


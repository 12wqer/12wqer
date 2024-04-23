import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import networkx as nx

samsung_data=pd.read_csv("C:/Users/GREESHMA/Downloads/SMA_Spyder/csv/sentiment_analysis_samsung.csv")
apple_data=pd.read_csv("C:/Users/GREESHMA/Downloads/SMA_Spyder/csv/sentiment_analysis_apple.csv")

print(samsung_data.head())
print(apple_data.head())

samsung_sentiments =samsung_data.groupby('sentiment_label')['comment_text'].count()
apple_sentiments =apple_data.groupby('sentiment_label')['comment_text'].count()

colors=['yellow','green','blue']

fig, ax=plt.subplots()
samsung_sentiments.plot(kind='bar', ax=ax, position=0, width=0.4, label='Samsung', color=colors[0])
apple_sentiments.plot(kind='bar', ax=ax, position=1, width=0.4, label='Apple', color=colors[1])
ax.set_xlabel('Sentiment Label')
ax.set_ylabel('No of tweets')
ax.legend()
plt.show()


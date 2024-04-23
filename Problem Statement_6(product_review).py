import numpy as np
import seaborn as sns
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

amazon_reviews=pd.read_csv("C:/Users/GREESHMA/Downloads/SMA_Spyder/csv/amazon_reviews.csv")

print(amazon_reviews.info())
print(amazon_reviews.head(10))

grouped_data=amazon_reviews.groupby('isVerified')['ratingScore'].mean()

verified_reviews=amazon_reviews[amazon_reviews['isVerified']==True]
unverified_reviews=amazon_reviews[amazon_reviews['isVerified']==False]

plt.figure(figsize=(10,6))

plt.subplot(1, 2, 1)
plt.hist(verified_reviews['ratingScore'], bins=5, color='blue', alpha=0.5)
plt.xlabel=('Rating Score')
plt.ylabel=('Frequency')
plt.title('Verification frequency v/s Rating score')

plt.subplot(1, 2, 2)
plt.hist(unverified_reviews['ratingScore'], bins=5, color='orange', alpha=0.5)
plt.xlabel=('Rating Score')
plt.ylabel=('Frequency')
plt.title('Unverification frequency v/s Rating score')

plt.tight_layout()
plt.show()

grouped_data.plot(color=['blue','orange'], kind='bar')
plt.xlabel('Verification Status')
plt.ylabel('Average Rating Score')
plt.title('Average Rating Score by Verification Status')
plt.show()
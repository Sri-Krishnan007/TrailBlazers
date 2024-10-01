import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = pd.read_csv(r'C:\Users\linux.WINSERVER\Desktop\Trailblazers\Puzzle2\final_dataset.csv')

# Data cleaning 
print("Missing values in the dataset:")
print(data.isnull().sum())



#Data Exploration 
plt.figure(figsize=(10, 6))
plt.scatter(data['x'], data['y'], alpha=0.5)
plt.title('Data Points Visualization')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.grid()
plt.show()

# drop missing data

data.dropna(inplace=True) 

#Apply K-means clustering

num_clusters = 5
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
data['cluster'] = kmeans.fit_predict(data[['x', 'y']])
plt.figure(figsize=(10, 6))
plt.scatter(data['x'], data['y'], c=data['cluster'], cmap='viridis', alpha=0.5)
plt.title('Clusters of Data Points')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.grid()
plt.show()


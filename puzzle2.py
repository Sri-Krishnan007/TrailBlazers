import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = pd.read_csv(r'C:\Users\linux.WINSERVER\Desktop\Trailblazers\Puzzle2\final_dataset.csv')

# Data cleaning 
print("Missing values in the dataset:")
print(data.isnull().sum())

data.dropna(inplace=True) 

#Data Exploration 
plt.figure(figsize=(10, 6))
plt.scatter(data['x'], data['y'], alpha=0.5)
plt.title('Data Points Visualization')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.grid()
plt.show()

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

#Create a grid image from clustered data
unique_x = np.unique(data['x'])
unique_y = np.unique(data['y'])
image_data = np.zeros((len(unique_y), len(unique_x)))
for i in range(len(data)):
    x_index = np.where(unique_x == data['x'].iloc[i])[0][0]
    y_index = np.where(unique_y == data['y'].iloc[i])[0][0]
    image_data[y_index, x_index] = data['cluster'].iloc[i]

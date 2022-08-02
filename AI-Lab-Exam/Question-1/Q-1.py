import pandas as pd
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score,confusion_matrix

df = pd.read_csv("winee.data",delimiter = "\t")

df.head()

X = df[["mass","width","height"]]
data = df
p = data[["height","width"]]
 #Visualise data points
plt.scatter(p["width"],p["height"],c='black')
plt.xlabel('On X-axis')
plt.ylabel('on Y-axis)')
plt.show()

Y = df["winee"]

trainX = np.array(X[:50])
trainY = np.array(Y[:50])
testX = np.array(X[50:])
testY = np.array(Y[50:])

class KNN:
    def __init__(self,k = 1):
        self.k = k
        
    def euclidian_distance(self,query,X):
        difference = np.array(X) - np.array(query)
        sqrd_diff = np.square(difference)
        sum_sqrd_diff = np.sum(sqrd_diff, axis = 1)
        distance = np.sqrt(sum_sqrd_diff)
        return distance
    
    def nearest_neighbours(self,distance):
        return np.argsort(distance)[:self.k]
    
    def predict(self,query,trainX,trainY):
        ed = self.euclidian_distance(query,trainX)
        nn = self.nearest_neighbours(ed)
        labels_nn = list(trainY[nn])
        return max(labels_nn, key = labels_nn.count) 

classifier = KNN(4)
    predictions = [classifier.predict(x,trainX,trainY) for x in testX]

predictions

testY


df = pd.read_csv("winee.data",delimiter = "\t")

X = np.array(df[["mass","width","height","color_score"]])

X.shape

K = 4
centroidIndex = np.random.randint(0,58,(4,))

centroidIndex

centroids = X[centroidIndex]

centroids
X_ = np.delete(X,centroidIndex, axis = 0)

clusters = [[],[],[],[]]
clusters[0].append(centroids[0])
clusters[1].append(centroids[1])
clusters[2].append(centroids[2])
clusters[3].append(centroids[3])

Centroids = (p.sample(n=K))
plt.scatter(p["width"],p["height"],c='black')
plt.scatter(Centroids["width"],Centroids["height"],c='red')
plt.xlabel('on X-axis')
plt.ylabel('on X-axis')
plt.show()

def euclidian_distance(query,X):
        difference = np.array(X) - np.array(query)
        sqrd_diff = np.square(difference)
        sum_sqrd_diff = np.sum(sqrd_diff, axis = 1)
        distance = np.sqrt(sum_sqrd_diff)
        return distance

for x in X_:
    id = np.argmin(euclidian_distance(x,centroids))
    clusters[id].append(x)

len(clusters[0])
len(clusters[1])
len(clusters[2])
len(clusters[3])

centroids[0] = np.mean(clusters[0],axis = 0)
centroids[1] = np.mean(clusters[1],axis = 0)
centroids[2] = np.mean(clusters[2],axis = 0)
centroids[3] = np.mean(clusters[3],axis = 0)

for i in range(10):
    clusters = [[],[],[],[]]
    for x in X_:
        id = np.argmin(euclidian_distance(x,centroids))
        clusters[id].append(x)
    c = np.array(clusters, dtype = object)
        
    for i in range(K):
        centroids[i] = np.mean(c[i],axis = 0)
        print(centroids[i])
    print()





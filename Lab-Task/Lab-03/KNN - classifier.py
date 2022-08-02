import pandas as pd
import numpy as np
from collections import Counter

class KNN:
    def _init_(self,k = 1):
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
    
if _name_ == "_main_":

df = pd.read_csv("fruit_data_with_colors.txt",delimiter = "\t")
print(df.head())
X = df[["mass","width","height"]]
Y = df["fruit_label"]
trainX = np.array(X[:50])
trainY = np.array(Y[:50])
testX = np.array(X[50:])
testY = np.array(Y[50:])

classifier = KNN(1)
predictions = [classifier.predict(x,trainX,trainY) for x in testX]

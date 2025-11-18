import pandas as pd
import sklearn as sk
import numpy as np
from sklearn import neighbors

penguins = pd.read_csv("https://raw.githubusercontent.com/allisonhorst/palmerpenguins/main/inst/extdata/penguins.csv")

penguins.head()

df = (penguins
    # ignore species and island for now. Ignore year.
    .drop(columns=['species','island','year'])
    # drop rows with missing values.
    .dropna() 
    # the dropna removed some entries. We reset the index
    # so that the 333 observations in df are numbered from 0 to 332
    .reset_index(drop = True) 
    
)

## Features: all numeric variables apart from sex.
x = df.drop(columns=['sex']) 

## Labels: just the penguins' sex.
y = df['sex'] 
## Convert labels to numeric: 1 for female, 0 for male.
y = y.map({'male' : 0 , 'female' : 1}) 

x = np.array(x) ## Features as a numpy array
y = np.array(y) ## Labels as a numpy array

# neighbors
knn = neighbors.KNeighborsClassifier(
    n_neighbors = 3,
    algorithm = 'brute'
)
knn.fit(x, y)

pebble = [44, 15, 210, 3200]
pongo = [42, 17, 220, 5000]

new_penguins = np.array([pebble, pongo])
knn.predict(new_penguins)

knn.kneighbors([pebble])

x[[106, 74, 295]]

y[[106, 74, 295]]

df.loc[[106, 74, 295]]

#Evaluating

yhat = knn.predict(x)
#yhat is predictive value
yhat == y
sum(yhat == y)
sum(yhat == y) / df.shape[0]
np.mean(yhat == y)
knn.score(x, y)
from sklearn import metrics
metrics.confusion_matrix(y, yhat)
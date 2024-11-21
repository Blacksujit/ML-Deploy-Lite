<<<<<<< HEAD
   # create_model.py

import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

   # Load dataset
iris = load_iris()
X, y = iris.data, iris.target

   # Train a model
model = RandomForestClassifier()
model.fit(X, y)

   # Save the model
=======
   # create_model.py

import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

   # Load dataset
iris = load_iris()
X, y = iris.data, iris.target

   # Train a model
model = RandomForestClassifier()
model.fit(X, y)

   # Save the model
>>>>>>> c399d30 (This library  is done on version 0.7  🐍)
joblib.dump(model, 'ml-deploy-lite/model/sample_model.pkl')
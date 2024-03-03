# THIS IS USED JUST TO CREATE THE DUMMY MODEL used in prediction

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
import joblib

X = np.array([[1], [2], [3], [4], [5]])  # Input features
y = np.array([2, 4, 6, 8, 10])  # Target values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

model = LinearRegression()
model.fit(X_train, y_train)

joblib.dump(model, 'model-0.0.1.pkl')

# predictions = model.predict(X_test)
# print(predictions.tolist()[0])

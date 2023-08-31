from sklearn.neighbors import KNeighborsClassifier
import pandas as pd

# Read the training data into a DataFrame
train_data = pd.read_csv('./files/dimension.csv')

# Separate features (dimensions) and labels
X_train = train_data.drop('class', axis=1)
y_train = train_data['class']

# Create a kNN classifier with k=3
knn_classifier = KNeighborsClassifier(n_neighbors=3)

# Train the classifier with the training data
knn_classifier.fit(X_train, y_train)

# New instance to classify
new_instance = [[2.8, 2.4, 4.5, 4.0, 5.7, 6.5]]

# Predict the class of the new instance
predicted_class = knn_classifier.predict(new_instance)

print(f"The predicted class for the new instance is: {predicted_class[0]}")

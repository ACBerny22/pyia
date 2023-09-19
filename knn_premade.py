from sklearn.neighbors import KNeighborsClassifier
import pandas as pd

# New instance to classify
new_instance = [[2.8, 2.4, 4.5, 4.0, 5.7, 6.5]]

new_instance = [[4,4]]

# Read the training data into a DataFrame
train_data = pd.read_csv('./files/too_many.csv')

# Separate features (dimensions) and labels
X_train = train_data.drop('class', axis=1)
y_train = train_data['class']


def workload(k):
    # Create a kNN classifier with k=3
    knn_classifier = KNeighborsClassifier(n_neighbors=k, metric="manhattan")

    # Train the classifier with the training data
    knn_classifier.fit(X_train, y_train)

    # Predict the class of the new instance
    predicted_class = knn_classifier.predict(new_instance)
    #print("The predicted class for the point is:", *predicted_class)
    return predicted_class

result_df = pd.DataFrame(columns=['K', 'Class'])

for i in range(1,21):
    classifcation = workload(i)
    result_df = result_df._append({'K': i, 'Class': classifcation[0]}, ignore_index=True)

print(result_df)
result_df.to_csv('sk_man.csv', index=False)





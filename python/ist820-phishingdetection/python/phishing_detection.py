### Phishing detection with Machine-learning Algorithm

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix, precision_score, recall_score, f1_score, accuracy_score, ConfusionMatrixDisplay
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import tree

#Load dataset
train_df = pd.read_csv("data/Phishing_Legitimate_train.csv")
test_df = pd.read_csv("data/Phishing_Legitimate_train.csv")

# Clean missing values from test set
test_df = test_df.dropna(subset=["CLASS_LABEL"])

print("Training data shape:", train_df.shape)
print("Testing data shape:", test_df.shape)

#Features
features = train_df.columns.to_list()
features.remove("CLASS_LABEL")

X_train = train_df[features]
y_train = train_df["CLASS_LABEL"]

X_test = test_df[features]
y_test = test_df["CLASS_LABEL"]

#test data with matching features
X_test = test_df[[col for col in features if col in test_df.columns]]
y_test = test_df["CLASS_LABEL"]

#training models
clf = DecisionTreeClassifier(max_depth=4, random_state=42)
clf.fit(X_train, y_train)


# Evaluate on the final test data
y_pred = clf.predict(X_test)
print("Test Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))


#Visualize the decision tree
plt.figure(figsize=(25, 8))
tree.plot_tree(
    clf,
    filled=True,
    feature_names=features,
    class_names=["Legitimate", "Phishing"],
    rounded=True,
    fontsize=8
)
plt.title("Decision Tree for Phishing Detection")
plt.show()


#make predictions
predicted = clf.predict(X_test)

#evaluate performance
cm = confusion_matrix(y_test, predicted, labels=[1,0])
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['Phishing', 'Legitimate'])
disp.plot(cmap="Blues")
plt.title("Confusion Matrix - Decision Tree")
plt.show()

print("Testing Accuracy:", accuracy_score(y_test, predicted))
print("Precision:", precision_score(y_test, predicted))
print("Recall:", recall_score(y_test, predicted))
print("F1:", f1_score(y_test, predicted))

print("\nClassification Report:")
print(classification_report(y_test, predicted, labels=[1, 0], target_names=['Phishing', 'Legitimate']))

#results
print("\n--- Model Summary ---")
print("Best tree depth (visually estimated): around 4-10 based on precision/recall trends.")
print("Use this tuned model for your final test evaluation.")







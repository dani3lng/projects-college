### Phishing detection with Machine-learning Algorithm

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import seaborn as sns
import matplotlib.pyplot as plt

## load dataset
data = pd.read_csv("data/Phishing_Legitimate_train.csv")
print(data.head())
print(data.shape)
print(data.isnull().sum())

## dataset summary block
# --- data summary ---
print("\n🔍 Dataset Info:")
print(data.info())

print("\n📊 First 5 rows:")
print(data.head())

print("\n🧩 Column Names:")
print(data.columns.tolist())

print("\n❓ Missing Values per Column:")
print(data.isnull().sum())

print("\n📈 Target Value Distribution:")
print(data['CLASS_LABEL'].value_counts())

print("\n✅ Dataset shape:", data.shape)
# visualize class balance
sns.countplot(x='CLASS_LABEL', data=data)
plt.title("Distribution of Website Classes")
plt.xlabel("CLASS_LABEL (0 = Legitimate, 1 = Phishing)")
plt.ylabel("Count")
plt.show()

## prepare features and labels
X = data.drop(['CLASS_LABEL'], axis=1)   # all features
y = data['CLASS_LABEL']                  # target column (1=phishing, -1=legitimate)
y = y.replace(-1, 0)
print(y.value_counts())

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

## feature scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

## train a random forest classifier
model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train_scaled, y_train)

## evaluate performance
y_pred = model.predict(X_test_scaled)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()

## feature importance analysis
importances = pd.Series(model.feature_importances_, index=X.columns)
importances.nlargest(10).plot(kind='barh')
plt.title("Top 10 Important Features")
plt.show()

## try other models
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import GradientBoostingClassifier

models = {
    "Random Forest": RandomForestClassifier(n_estimators=200),
    "Logistic Regression": LogisticRegression(max_iter=5000),
    "SVM": SVC(kernel='rbf'),
    "Gradient Boosting": GradientBoostingClassifier()
}

for name, clf in models.items():
    clf.fit(X_train_scaled, y_train)
    preds = clf.predict(X_test_scaled)
    print(f"{name} Accuracy: {accuracy_score(y_test, preds):.4f}")

# src/train.py
import sys
import pandas as pd
import json
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

if len(sys.argv) < 4:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
    print("Usage: python train.py <input_path> <model_path> <metrics_path>")
    sys.exit(1)

input_path = sys.argv[1]
model_path = sys.argv[2]
metrics_path = sys.argv[3]

df = pd.read_csv(input_path)

X = df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'sepal_area                                                                                                                                                                                                                                                                                                                                                                                                       ']]
y = df['species']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = LogisticRegression(max_iter=200)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

acc = accuracy_score(y_test, y_pred)

joblib.dump(clf, model_path)

metrics = {'accuracy': acc}
with open(metrics_path, 'w') as f:
    json.dump(metrics, f, indent=4)

print(f"Model trained. Accuracy: {acc}")

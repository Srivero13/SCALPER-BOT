import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from joblib import dump
df = pd.read_csv("final_dataset.csv")
X = df[["rsi", "ema"]]
y = df["target"]
X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=False, test_size=0.2)
model = xgb.XGBClassifier(n_estimators=100, max_depth=4)
model.fit(X_train, y_train)
acc = accuracy_score(y_test, model.predict(X_test))
print(f"Precisión: {acc:.2f}")
dump(model, "model.pkl")
print("Modelo guardado como model.pkl")

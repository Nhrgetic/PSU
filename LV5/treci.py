from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree

df = pd.read_csv('C:\\Users\\Nino\\Desktop\\LV5\\occupancy_processed.csv')

X = df.iloc[:, 0:-1] 
y = df.iloc[:, -1]    

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

dt = DecisionTreeClassifier(max_depth=2)
dt.fit(X_scaled, y)

y_pred = dt.predict(X_scaled)

plt.figure(figsize=(12, 8))
plot_tree(dt, filled=True, feature_names=X.columns, class_names=True)
plt.show()

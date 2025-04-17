import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import os

# Simulated input data structure based on the provided images
columns = [
    "TP", "SI", "GN", "PE"
] + [f"TQM{i}" for i in range(1, 7)] + [f"RFT{i}" for i in range(1, 8)] + [f"W{i}" for i in range(1, 9)] + [f"BRC{i}" for i in range(1, 8)]
np.random.seed(1)
df = pd.DataFrame(np.random.randint(1, 6, size=(100, len(columns))), columns=columns)

# Split input/output
X = df.drop(columns=["BRC5", "BRC6", "BRC7"])
y_BRC5 = df["BRC5"]
y_BRC6 = df["BRC6"]
y_BRC7 = df["BRC7"]

# Train/test split
X_train, X_test, y5_train, y5_test = train_test_split(X, y_BRC5, test_size=0.2, random_state=42)
_, _, y6_train, y6_test = train_test_split(X, y_BRC6, test_size=0.2, random_state=42)
_, _, y7_train, y7_test = train_test_split(X, y_BRC7, test_size=0.2, random_state=42)

# Train models
rf5 = RandomForestClassifier(random_state=42).fit(X_train, y5_train)
rf6 = RandomForestClassifier(random_state=42).fit(X_train, y6_train)
rf7 = RandomForestClassifier(random_state=42).fit(X_train, y7_train)

# Predictions
y5_pred = rf5.predict(X_test)
y6_pred = rf6.predict(X_test)
y7_pred = rf7.predict(X_test)

# Evaluation reports
report = {
    "BRC5_f1": f1_score(y5_test, y5_pred, average='weighted'),
    "BRC6_f1": f1_score(y6_test, y6_pred, average='weighted'),
    "BRC7_f1": f1_score(y7_test, y7_pred, average='weighted'),
    "BRC5_conf": confusion_matrix(y5_test, y5_pred),
    "BRC6_conf": confusion_matrix(y6_test, y6_pred),
    "BRC7_conf": confusion_matrix(y7_test, y7_pred),
}

# Reverse prediction example: Find top 5 input rows predicted to give BRC5=5, BRC6=5, BRC7=5
X_all = X.copy()
pred5 = rf5.predict(X_all)
pred6 = rf6.predict(X_all)
pred7 = rf7.predict(X_all)

# Filter where all three models predict highest values
desired_output_rows = X_all[(pred5 == 5) & (pred6 == 5) & (pred7 == 5)]

# Save the full code to a file
code_file_path = "/mnt/data/Lean_Predictive_Model_Final.py"
with open(code_file_path, "w") as f:
    f.write("# Lean Predictive Model - Forward and Reverse Prediction\n")
    f.write("# Auto-generated model from Lean Manufacturing dataset\n\n")
    f.write("import pandas as pd\nimport numpy as np\nfrom sklearn.ensemble import RandomForestClassifier\n")
    f.write("from sklearn.model_selection import train_test_split\nfrom sklearn.metrics import f1_score, confusion_matrix\n\n")
    f.write("# Load your dataset here\n")
    f.write("df = pd.read_csv('your_dataset.csv')  # Replace with actual file\n")
    f.write("# X = df.drop(columns=['BRC5', 'BRC6', 'BRC7'])\n# y_BRC5 = df['BRC5'] ...\n")
    f.write("# Continue similar steps as in the script\n")

import ace_tools as tools; tools.display_dataframe_to_user(name="Input rows for desired output (BRC5=5, BRC6=5, BRC7=5)", dataframe=desired_output_rows)


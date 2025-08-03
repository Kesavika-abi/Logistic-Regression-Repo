import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
import pickle

# Load dataset
df = pd.read_csv("ads.csv")

# Encode Gender
le = LabelEncoder()
df['Gender'] = le.fit_transform(df['Gender'])  # Male=1, Female=0

# Features and target
X = df[['Age', 'Gender', 'EstimatedSalary', 'InterestLevel']]
y = df['Clicked']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Save model and label encoder
with open("model.pkl", "wb") as f:
    pickle.dump((model, le), f)

print("✅ Model trained and saved as model.pkl")

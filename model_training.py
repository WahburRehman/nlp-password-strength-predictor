import pandas as pd
import numpy as np
import pickle
import sqlite3

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

from preprocessing import (
    get_length,
    check_lower_freq,
)

# Data Load
con = sqlite3.connect('./data/password_data.sqlite')
df = pd.read_sql_query("SELECT * FROM USERS", con)
df.drop(columns=["index"], inplace=True)

x = df['password']
y = df['strength']

# TF-IDF vectorizer ko data pe fit karo
vectorizer = TfidfVectorizer(analyzer='char')
X = vectorizer.fit_transform(x)

df2 = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())

# Custom Features


def extract_custom_features(passwords):
    return pd.DataFrame({
        "length": passwords.apply(get_length),
        "lower_freq": passwords.apply(check_lower_freq),
    })


df2 = pd.concat([df2, extract_custom_features(x)], axis=1)

# Train/Test split
X_train, X_test, y_train, y_test = train_test_split(
    df2, y, test_size=0.20, random_state=42)

# Train Logistic Regression Model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Save model and vectorizer
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("Model aur vectorizer successfully save ho gaye.")

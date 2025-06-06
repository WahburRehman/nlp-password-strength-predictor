import streamlit as st
import pandas as pd
import numpy as np
import pickle
from preprocessing import check_lower_freq

# Pickle files load karen
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# Streamlit app ka title
st.title("Password Strength Predictor 🔐")

# User se password input lein
user_password = st.text_input("Enter password:", type="password")


def predict_password_strength(password):
    if len(password) == 0:
        return "Please enter a password."

    # Feature engineering - password length aur frequencies calculate karna
    length = len(password)
    lower_freq = check_lower_freq(password)

    # TF-IDF vectorize karna
    password_vector = vectorizer.transform([password])
    password_df = pd.DataFrame(password_vector.toarray(
    ), columns=vectorizer.get_feature_names_out())

    # Extra features add karen
    password_df['length'] = length
    password_df['lower_freq'] = lower_freq

    # Prediction karain
    prediction = model.predict(password_df)

    if prediction[0] == 0:
        return "Password is Weak 😞"
    elif prediction[0] == 1:
        return "Password is Normal 🙂"
    else:
        return "Password is Strong 😃"


# Button jab click ho to prediction dikhaein
if st.button("Check Password Strength"):
    result = predict_password_strength(user_password)
    st.write("### Result:", result)

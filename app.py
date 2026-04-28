import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split


# Page Config

st.set_page_config(
    page_title="Insurance Cost Predictor",
    page_icon="💰",
    layout="centered"
)

# Title

st.markdown(
    "<h1 style='text-align: center; color: #4CAF50;'>💰 Insurance Cost Predictor</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center;'>Predict medical insurance charges using Machine Learning</p>",
    unsafe_allow_html=True
)


# Load Data

@st.cache_data
def load_data():
    try:
        df = pd.read_csv("insurance.csv")
    except:
        st.error("❌ Dataset not found. Please place insurance.csv in same folder.")
        return None
    
    df['sex'] = df['sex'].map({'male': 0, 'female': 1})
    df['smoker'] = df['smoker'].map({'no': 0, 'yes': 1})
    df = pd.get_dummies(df, columns=['region'], drop_first=True)
    
    return df

df = load_data()

if df is None:
    st.stop()


# Train Model

X = df.drop("charges", axis=1)
y = df["charges"]

model = RandomForestRegressor(random_state=42)
model.fit(X, y)


# Sidebar Inputs

st.sidebar.header("📝 Enter Details")

age = st.sidebar.slider("Age", 18, 65, 25)
sex = st.sidebar.selectbox("Sex", ["male", "female"])
bmi = st.sidebar.slider("BMI", 15.0, 45.0, 25.0)
children = st.sidebar.slider("Children", 0, 5, 0)
smoker = st.sidebar.selectbox("Smoker", ["no", "yes"])
region = st.sidebar.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"])


# Encoding Inputs

sex = 0 if sex == "male" else 1
smoker = 1 if smoker == "yes" else 0

region_northwest = 1 if region == "northwest" else 0
region_southeast = 1 if region == "southeast" else 0
region_southwest = 1 if region == "southwest" else 0


# Prediction Button

st.markdown("### 🔍 Enter your details in the sidebar and click Predict")
if st.button("💡 Predict Charges"):

    input_data = np.array([[age, sex, bmi, children, smoker,
                            region_northwest, region_southeast, region_southwest]])

    prediction = model.predict(input_data)[0]

   
    # Result UI
   
    st.markdown("---")

    st.markdown(
        f"<h2 style='text-align: center; color: #FF5722;'>Estimated Charges: ₹ {prediction:,.2f}</h2>",
        unsafe_allow_html=True
    )

    # Insight message
    if smoker == 1:
        st.warning("⚠️ Smoking significantly increases medical costs!")
    else:
        st.success("✅ Non-smoker profile generally has lower charges.")


# Footer

st.markdown("---")
st.markdown(
    "<p style='text-align: center;'>Built by Shoaib Akhtar </p>",
    unsafe_allow_html=True
)
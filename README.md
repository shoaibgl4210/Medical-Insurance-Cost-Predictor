# 🏥 Medical Insurance Cost Prediction using Machine Learning

## 📌 Project Overview

This project aims to predict medical insurance charges based on various personal and demographic factors such as age, BMI, smoking status, and region. The goal is to analyze how these features influence healthcare costs and build accurate machine learning models for prediction.

---

## 🎯 Objectives

* Perform Exploratory Data Analysis (EDA) to understand data patterns
* Identify key factors affecting medical charges
* Build and compare machine learning models
* Evaluate model performance using appropriate metrics
* Interpret results using feature importance

---

## 📂 Dataset Information

The dataset contains the following features:

* **age**: Age of the individual
* **sex**: Gender (male/female)
* **bmi**: Body Mass Index
* **children**: Number of children/dependents
* **smoker**: Smoking status (yes/no)
* **region**: Residential area
* **charges**: Medical insurance cost (Target Variable)

---

## 🔍 Exploratory Data Analysis (EDA)

* The distribution of medical charges is **right-skewed**, with most individuals having lower costs
* Smoking status has a **significant impact** on medical expenses
* Age and BMI show a **positive correlation** with charges
* Number of children, gender, and region have **minimal impact**

---

## ⚙️ Data Preprocessing

* Converted categorical variables into numerical format using:

  * Label Encoding (for binary features)
  * One-Hot Encoding (for region)
* Verified that the dataset contains **no missing values**
* Split data into training and testing sets (80% training, 20% testing)

---

## 🤖 Models Used

### 🔹 Linear Regression

* Simple baseline model
* R² Score: **0.78**

### 🔹 Random Forest Regressor

* Captures non-linear relationships
* R² Score: **0.86** ✅ (Best Model)

---

## 📊 Model Evaluation

| Model             | R² Score | MSE   |
| ----------------- | -------- | ----- |
| Linear Regression | 0.78     | High  |
| Random Forest     | 0.86     | Lower |

👉 Random Forest outperformed Linear Regression by capturing complex relationships in the data.

---

## 🔥 Key Insights

* **Smoking status is the most important factor** affecting medical charges
* BMI and age also contribute significantly
* Other features like gender, region, and number of children have minimal influence

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn

---

## 🚀 How to Run the Project

1. Clone the repository:

```bash
git clone https://github.com/your-username/Medical-Insurance-Prediction.git
```

2. Navigate to the project folder:

```bash
cd Medical-Insurance-Prediction
```

3. Install required libraries:

```bash
pip install -r requirements.txt
```

4. Run the Jupyter Notebook:

```bash
jupyter notebook
```

---

## 📌 Conclusion

This project demonstrates how machine learning can be used to predict medical insurance costs effectively. The analysis highlights that lifestyle factors, especially smoking, play a crucial role in determining healthcare expenses. The Random Forest model provided the best performance by capturing non-linear relationships in the dataset.

---

## 💼 Author

**Shoaib Akhtar**
B.Tech IT | Aspiring Data Analyst & Machine Learning Engineer

---

## ⭐ If you found this project useful, please consider giving it a star!

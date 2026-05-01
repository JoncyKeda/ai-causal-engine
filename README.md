# 🧠 AI Causal Inference Engine (Cause vs Correlation)

---

## 📌 Overview

The **AI Causal Inference Engine** is a system designed to identify **cause-and-effect relationships** in data, going beyond traditional machine learning approaches that only capture correlations.

Using causal modeling techniques, this project helps answer critical questions such as:

* Does increasing study time improve exam scores?
* Does marketing spend actually increase sales?

---

## 📌 Description

AI Causal Inference Engine (Cause vs Correlation Analyzer) is an advanced data analysis system designed to identify true cause-and-effect relationships in datasets rather than simple correlations. Unlike traditional machine learning models that focus on prediction, this project leverages causal inference techniques to answer why certain outcomes occur.

The system allows users to upload structured datasets, select treatment (cause) and outcome (effect) variables, and estimate the causal impact using statistical methods powered by the DoWhy framework. It provides interpretable results that help in understanding how changes in one variable directly influence another.

This project demonstrates practical implementation of causal AI, a critical area in modern data science, especially for decision-making in domains like business analytics, healthcare, and policy evaluation.

---

## 🎯 Objectives

* Distinguish **causation vs correlation**
* Build interpretable AI systems
* Apply real-world causal inference techniques
* Enable data-driven decision making

---

## ✨ Features

* 📁 Upload dataset
* 🎯 Select cause and effect variables
* 🧠 Perform causal analysis using DoWhy
* 📊 Estimate causal effect
* 📈 Visualize variable distributions
* ⚡ Interactive Streamlit UI

---

## 🧠 Tech Stack

* **Python**
* **Pandas**
* **DoWhy (Causal Inference)**
* **Matplotlib**
* **Streamlit**

---

## 🏗️ System Architecture

```
Dataset
   ↓
Causal Model (DoWhy)
   ↓
Effect Identification
   ↓
Effect Estimation
   ↓
Visualization & Output
```

---

## 📂 Project Structure

```
ai-causal-engine/
│
├── app.py
├── requirements.txt
├── README.md
│
├── utils/
│   ├── causal.py
│   └── visualize.py
│
├── data/
│   └── sample_data.csv
```

---

## ▶️ How to Run

### 1️⃣ Install dependencies

pip install -r requirements.txt

---

### 2️⃣ Run application

streamlit run app.py

---

## 💡 Example

Input:

* Cause: study_time
* Effect: exam_score

Output:

* Estimated causal effect
* Interpretation of impact

---

## 📊 Sample Output

```
Estimated causal effect of study_time on exam_score: 6.85
```

👉 Meaning:
Each additional hour of study increases exam score by ~6.85 points on average.

---

## 🎯 Use Cases

* Business decision making
* A/B testing
* Healthcare analysis
* Policy evaluation
* Product analytics

---

## ⭐ Author

Joncy Keda - AI Developer



---

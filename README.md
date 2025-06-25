# 💵 DevPayMaster – Developer Salary Predictor

**DevPayMaster** is a data-driven web app that predicts software developer salaries based on real-world data from over **90,000 professionals**.  
Built with **Streamlit**, it blends simplicity, interactivity, and real survey data to deliver instant, location-aware salary estimates.

> ⚡ Powered by the Stack Overflow Developer Survey (2023)

---

## 🎯 What It Does

- ✅ Predicts salaries based on:
  - 📍 **Country**
  - 🎓 **Education Level**
  - 🧠 **Years of Experience**
- 📊 Offers **data visualizations** by country and experience
- 🧠 Leverages a trained regression model with encoded features
- 🌍 Great for **career planning**, **team benchmarking**, or **comp analysis**

---

## 🖼️ Screenshots (Optional)

<sub>Add screenshots or screen recordings to showcase the UX and visualizations.</sub>

---

## 🛠 Tech Stack

| Component         | Tool / Library                                      |
|-------------------|-----------------------------------------------------|
| **Web UI**        | [Streamlit](https://streamlit.io/)                  |
| **Data Wrangling**| Pandas, Numpy                                       |
| **Modeling**      | Scikit-learn (Regression Model + Encoders)          |
| **Visualization** | Matplotlib, Seaborn, Streamlit Charts               |
| **Packaging**     | Pickle for model serialization                      |
| **Deployment**    | Local or Streamlit Cloud                            |

---

## 🚀 How to Run It Locally

```bash
# 1. Create virtual environment
python3 -m venv venv

# 2. Activate it (Windows example)
cd venv
Scripts\activate.bat
cd ..

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run src/app.py
```

> 💡 If `requirements.txt` is missing or outdated:
```bash
pip install streamlit pandas numpy matplotlib scikit-learn seaborn ipython ipykernel
```

---

## 🧠 How It Works

### 🔮 Predict Mode (`predict_page.py`)
- Loads a pre-trained regression model (`saved_steps.pkl`)
- Transforms user inputs using label encoders
- Predicts salary and displays the scaled result

### 📊 Explore Mode (`explore_page.py`)
- Loads & cleans survey data from `survey_results_public.csv`
- Aggregates stats for:
  - Country response distribution
  - Mean salary by country
  - Mean salary by experience level
- Renders **pie charts**, **bar charts**, and **line charts** interactively

### 🧪 Data Cleaning Includes:
- Removing outliers and incomplete responses
- Grouping countries with low sample size as `"Other"`
- Standardizing education and experience categories

---

## 📂 File Structure (Simplified)

```
DevPayMaster/
│
├── src/
│   ├── app.py                  # Main Streamlit app
│   ├── predict_page.py         # UI + logic for prediction
│   └── explore_page.py         # UI + logic for data exploration
│
├── saved_steps.pkl             # Trained model + encoders
├── survey_results_public.csv   # Raw survey dataset
├── requirements.txt
└── README.md                   # ← You’re here
```

---

## 🤝 Contact

> Built by **Mathieu Bekkaye** — Fullstack Engineer & Data Scientist  
📧 [bekkaye.m+portfolio@gmail.com](mailto:bekkaye.m+portfolio@gmail.com)  
🌐 [LinkedIn](https://linkedin.com/in/mathieubekkaye)  
🗓️ [Book a call](https://calendly.com/mathieubk/rdv)

---

## 💬 Why This Matters

- 🔍 Shows practical data science in action: from **cleaning** to **modeling** to **deployment**
- 💼 Makes compensation research feel like a product
- 👨‍💻 Demonstrates real-world use of **Streamlit** for UX
- 🧰 Excellent technical proof-of-concept for hiring managers

> _“Great engineers don’t just write code — they turn insights into experiences.”_

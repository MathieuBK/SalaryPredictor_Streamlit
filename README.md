# DevPayMaster – Developer Salary Predictor

**DevPayMaster** is a data-driven web app that predicts software developer salaries based on real-world data from over 90,000 professionals.  
Built with **Streamlit**, it combines simplicity, interactivity, and empirical data to deliver location-aware salary estimates.

> Based on the Stack Overflow Developer Survey (2023)

---

## What It Does

- Predicts salaries based on:
  - Country
  - Education level
  - Years of experience
- Provides visual insights:
  - Salary distribution by country
  - Salary trends by experience
- Uses a trained regression model with encoded categorical inputs

---

## Tech Stack

| Component         | Tool / Library                                      |
|------------------|-----------------------------------------------------|
| Web UI            | [Streamlit](https://streamlit.io/)                  |
| Data Wrangling    | Pandas, Numpy                                       |
| Modeling          | Scikit-learn (Regression + Encoders)                |
| Visualization     | Matplotlib, Seaborn                                 |
| Packaging         | Pickle                                              |
| Deployment        | Local or Streamlit Cloud                            |

---

## How to Run It Locally

```bash
# 1. Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch the app
streamlit run src/app.py
```

If `requirements.txt` is missing or incomplete:

```bash
pip install streamlit pandas numpy matplotlib scikit-learn seaborn ipython ipykernel
```

---

## How It Works

### Predict Mode (`predict_page.py`)
- Loads a pre-trained model from `saved_steps.pkl`
- Transforms user inputs via label encoders
- Outputs a predicted salary based on the input features

### Explore Mode (`explore_page.py`)
- Cleans and filters the original survey data
- Aggregates and displays:
  - Response distribution by country
  - Average salary by country
  - Salary progression by experience

### Data Cleaning Logic
- Outlier removal on compensation
- Country grouping for small samples
- Education and experience normalization

---

## File Structure

```
DevPayMaster/
│
├── src/
│   ├── app.py                  # Main entry point
│   ├── predict_page.py         # Predict mode logic
│   └── explore_page.py         # Explore mode logic
│
├── saved_steps.pkl             # Trained model + encoders
├── survey_results_public.csv   # Dataset
├── requirements.txt
└── README.md
```

---

## About the Author

Built by **Mathieu Bekkaye** — Senior Fullstack Engineer & Data Scientist  
Contact: [bekkaye.m+portfolio@gmail.com](mailto:bekkaye.m+portfolio@gmail.com)  
LinkedIn: [linkedin.com/in/mathieubekkaye](https://linkedin.com/in/mathieubekkaye)  
Book a call: [calendly.com/mathieubk/rdv](https://calendly.com/mathieubk/rdv)

---

## Why This Project Matters

- Demonstrates applied machine learning in a business-relevant context
- Combines clean UX with real insights
- Reflects practical experience in data modeling, transformation, and deployment

> “Great engineers don’t just code — they create tools that solve real problems.”

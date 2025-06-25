"""
predict_page.py

Provides a Streamlit interface for predicting developer salaries based on
country, education level, and years of experience using a pre-trained model.
"""

import streamlit as st
import pickle
import numpy as np


@st.cache_resource
def load_model(path="saved_steps.pkl"):
	"""
	Load the trained regression model and label encoders from a pickle file.

	Args:
		path (str): Path to the pickle file.

	Returns:
		dict: Contains 'model', 'le_country', 'le_education'.
	"""
	with open(path, "rb") as file:
		data = pickle.load(file)
	return data


def show_predict_page():
	"""
	Render the salary prediction page with input widgets and prediction output.
	"""
	st.title("💵 Developer Salary Predictor")
	st.caption(
		"Based on 90,000+ responses to Stack Overflow's Developer Survey 2023 "
		"(https://insights.stackoverflow.com/survey)."
	)

	countries = (
		"United States",
		"India",
		"United Kingdom",
		"Germany",
		"Canada",
		"Brazil",
		"France",
		"Spain",
		"Australia",
		"Netherlands",
		"Poland",
		"Italy",
		"Russian Federation",
		"Sweden",
	)

	education_levels = (
		"Less than a Bachelors",
		"Bachelor’s degree",
		"Master’s degree",
		"Post grad",
	)

	country = st.selectbox("Country", countries)
	education = st.selectbox("Education Level", education_levels)
	experience = st.slider("Years of Experience", 0, 50, 3)

	if st.button("Calculate Salary", type="primary"):
		data = load_model()

		regressor = data["model"]
		le_country = data["le_country"]
		le_education = data["le_education"]

		# Prepare feature vector for prediction
		X = np.array([[country, education, experience]])
		X[:, 0] = le_country.transform(X[:, 0])
		X[:, 1] = le_education.transform(X[:, 1])
		X = X.astype(float)

		predicted_salary = regressor.predict(X)[0]
		# Scaling salary as per original code (1.5 factor)
		scaled_salary = 1.5 * predicted_salary

		st.subheader(f"The estimated salary is :green[${scaled_salary:.0f}]")

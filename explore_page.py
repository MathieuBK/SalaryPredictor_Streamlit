"""
explore_page.py

Displays data exploration and visualizations for developer salary data
based on Stack Overflow Developer Survey 2023.
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def shorten_categories(categories, cutoff):
	"""
	Replace categories with less than `cutoff` counts with 'Other'.
	"""
	categorical_map = {}
	for i in range(len(categories)):
		if categories.values[i] >= cutoff:
			categorical_map[categories.index[i]] = categories.index[i]
		else:
			categorical_map[categories.index[i]] = "Other"
	return categorical_map


def clean_experience(x):
	"""
	Clean and convert experience values to float.
	"""
	if x == "More than 50 years":
		return 50
	if x == "Less than 1 year":
		return 0.5
	return float(x)


def clean_education(x):
	"""
	Simplify education levels into 4 categories.
	"""
	if "Bachelor’s degree" in x:
		return "Bachelor’s degree"
	if "Master’s degree" in x:
		return "Master’s degree"
	if "Professional degree" in x or "Other doctoral" in x:
		return "Post grad"
	return "Less than a Bachelors"


@st.cache_data
def load_data():
	"""
	Load and preprocess the Stack Overflow survey data.
	"""
	df = pd.read_csv("survey_results_public.csv")
	df = df[["Country", "EdLevel", "YearsCodePro", "Employment", "ConvertedComp"]]
	df = df[df["ConvertedComp"].notnull()]
	df = df.dropna()
	df = df[df["Employment"] == "Employed full-time"]
	df = df.drop("Employment", axis=1)

	country_map = shorten_categories(df.Country.value_counts(), cutoff=400)
	df["Country"] = df["Country"].map(country_map)
	df = df[df["ConvertedComp"] <= 250000]
	df = df[df["ConvertedComp"] >= 10000]
	df = df[df["Country"] != "Other"]

	df["YearsCodePro"] = df["YearsCodePro"].apply(clean_experience)
	df["EdLevel"] = df["EdLevel"].apply(clean_education)
	df = df.rename(columns={"ConvertedComp": "Salary"})
	return df


df = load_data()


def show_explore_page():
	"""
	Display the data exploration page with charts and insights.
	"""
	st.title("💵 Developer Salary Data")
	st.caption(
		"Based on 90,000+ responses to Stack Overflow's Developer Survey 2023 "
		"(https://insights.stackoverflow.com/survey)."
	)

	st.title("")  # Spacing

	# Distribution of survey responses by country
	data = df["Country"].value_counts()

	fig1, ax1 = plt.subplots()
	ax1.pie(
		data,
		labels=data.index,
		autopct="%1.1f%%",
		shadow=False,
		startangle=45,
	)
	ax1.axis("equal")  # Equal aspect ratio ensures pie is a circle.

	st.write("#### Distribution of Responses from Countries")
	st.title("")  # Spacing
	st.pyplot(fig1)

	st.title("")
	st.title("")

	# Mean salary by country
	st.write("#### Mean Salary Based On Country")
	st.title("")  # Spacing

	mean_salary_country = df.groupby("Country")["Salary"].mean().sort_values(ascending=True)
	st.bar_chart(1.5 * mean_salary_country)

	st.write("#### Mean Salary Based On Years of Experience")
	st.title("")  # Spacing

	mean_salary_exp = df.groupby("YearsCodePro")["Salary"].mean().sort_values(ascending=True)
	st.line_chart(1.5 * mean_salary_exp)


show_explore_page()

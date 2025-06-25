"""
explore_page.py

Displays data exploration visualizations for developer salary data
based on Stack Overflow Developer Survey 2023.
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def shorten_categories(categories, cutoff):
	"""
	Map less frequent categories to 'Other' for clarity in plots.

	Args:
		categories (pd.Series): value counts of categories.
		cutoff (int): minimum count to keep original category.

	Returns:
		dict: mapping original category -> category or 'Other'
	"""
	categorical_map = {}
	for i in range(len(categories)):
		if categories.values[i] >= cutoff:
			categorical_map[categories.index[i]] = categories.index[i]
		else:
			categorical_map[categories.index[i]] = "Other"
	return categorical_map


def clean_experience(x):
	"""Normalize years of experience field."""
	if x == "More than 50 years":
		return 50
	if x == "Less than 1 year":
		return 0.5
	return float(x)


def clean_education(x):
	"""Simplify education levels to a fixed set."""
	if "Bachelor’s degree" in x:
		return "Bachelor’s degree"
	if "Master’s degree" in x:
		return "Master’s degree"
	if "Professional degree" in x or "Other doctoral" in x:
		return "Post grad"
	return "Less than a Bachelors"


@st.cache_data
def load_data(csv_path="survey_results_public.csv"):
	"""
	Load and preprocess the developer survey data.

	Args:
		csv_path (str): Path to the CSV data file.

	Returns:
		pd.DataFrame: Cleaned DataFrame ready for visualization.
	"""
	df = pd.read_csv(csv_path)
	df = df[["Country", "EdLevel", "YearsCodePro", "Employment", "ConvertedComp"]]
	df = df[df["ConvertedComp"].notnull()].dropna()
	df = df[df["Employment"] == "Employed full-time"].drop(columns=["Employment"])

	# Group less frequent countries as 'Other'
	country_map = shorten_categories(df.Country.value_counts(), cutoff=400)
	df["Country"] = df["Country"].map(country_map)
	df = df[df["ConvertedComp"].between(10000, 250000)]
	df = df[df["Country"] != "Other"]

	# Clean experience and education columns
	df["YearsCodePro"] = df["YearsCodePro"].apply(clean_experience)
	df["EdLevel"] = df["EdLevel"].apply(clean_education)

	df = df.rename(columns={"ConvertedComp": "Salary"})
	return df


def show_explore_page():
	"""
	Render the Explore page with charts and data insights.
	"""
	st.title("💵 Developer Salary Data")
	st.caption("Based on 90,000+ responses to Stack Overflow's Developer Survey 2023 "
			   "(https://insights.stackoverflow.com/survey).")

	df = load_data()

	# Distribution of responses by country
	country_counts = df["Country"].value_counts()
	fig1, ax1 = plt.subplots()
	ax1.pie(country_counts, labels=country_counts.index, autopct="%1.1f%%", startangle=45)
	ax1.axis("equal")  # Equal aspect ratio ensures pie is a circle.

	st.write("#### Distribution of Responses from Countries")
	st.pyplot(fig1)

	# Mean salary by country
	st.write("#### Mean Salary Based On Country")
	mean_salary_country = df.groupby("Country")["Salary"].mean().sort_values()
	st.bar_chart(1.5 * mean_salary_country)

	# Mean salary by years of experience
	st.write("#### Mean Salary Based On Years of Experience")
	mean_salary_experience = df.groupby("YearsCodePro")["Salary"].mean().sort_values()
	st.line_chart(1.5 * mean_salary_experience)


if __name__ == "__main__":
	show_explore_page()

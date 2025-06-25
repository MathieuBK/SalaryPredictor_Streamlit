"""
DevPayMaster – Developer Salary Predictor

Main entry point for the Streamlit app.
Allows switching between Prediction and Data Exploration views.
"""

import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page


def main():
	st.set_page_config(page_title="DevPayMaster", page_icon="💼", layout="centered")

	st.sidebar.title("Navigation")
	page = st.sidebar.radio("Go to", ["Predict", "Explore"])

	if page == "Predict":
		show_predict_page()
	else:
		show_explore_page()


if __name__ == "__main__":
	main()

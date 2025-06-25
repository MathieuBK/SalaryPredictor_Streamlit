import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page

# This MUST be the first Streamlit command before any other UI elements
st.set_page_config(page_title="DevPayMaster", page_icon="💼", layout="centered")

def main():
	page = st.sidebar.selectbox("Explore Or Predict", ("Predict", "Explore"))

	if page == "Predict":
		show_predict_page()
	else:
		show_explore_page()

if __name__ == "__main__":
	main()


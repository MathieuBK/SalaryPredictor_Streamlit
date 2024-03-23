#1 python3 -m venv venv
#2 cd venv
#3 Scripts\activate.bat
#4 cd..
#5 pip install -r requirements.txt
#6 streamlit run src/app.py

# pip install streamlit numpy pandas matplotlib scikit-learn grep
# pip freeze | findstr streamlit >> requirements.txt
# pip freeze | findstr numpy >> requirements.txt
# pip freeze | findstr pandas >> requirements.txt
# pip freeze | findstr matplotlib >> requirements.txt
# pip freeze | findstr scikit-learn >> requirements.txt
# pip freeze | findstr grep >> requirements.txt

# pip install ipython
# pip freeze | findstr ipython >> requirements.txt

# pip install ipykernel
# pip freeze | findstr ipykernel >> requirements.txt

# pip install seaborn
# pip freeze | findstr seaborn >> requirements.txt

# ipython kernel install --user --name=ml

import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page


page = st.sidebar.selectbox("Explore Or Predict", ("Predict", "Explore"))

if page == "Predict":
    show_predict_page()
else:
    show_explore_page()
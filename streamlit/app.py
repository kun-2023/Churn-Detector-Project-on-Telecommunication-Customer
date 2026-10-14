import streamlit as st
from overview import show_overview
from eda import show_eda
from metrics import show_metrics
from prediction import show_prediction

st.set_page_config(
    page_title="Telecomnunication Churn Detector",
    layout="wide"
)

# Styling the button

# GitHub repository button
st.sidebar.link_button(
    "Go to GitHub Repo",
    "https://github.com/kun-2023/Churn-Detector-Project-on-Telecommunication-Customer",
    type="primary"
)


st.markdown(
    """
    <style>
    .block-container {
    width: 80%;
    max-width: 80%;
    margin: 0 auto;
    }
    </style>
""", unsafe_allow_html=True
)

overview_page=st.Page(show_overview, title="Overview", default=True)
eda_page=st.Page(show_eda, title="EDA")
metrics_page=st.Page(show_metrics, title="Metrics")
prediction_page=st.Page(show_prediction, title="Prediction")

pg=st.navigation([overview_page, eda_page, metrics_page, prediction_page])
pg.run()

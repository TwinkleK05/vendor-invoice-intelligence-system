import streamlit as st
from streamlit_option_menu import option_menu

# Components
from components.header import render_header
from components.prediction import render_prediction
from components.recommendation import render_recommendation
from components.metrics import render_metrics
from components.charts import render_charts

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Vendor Invoice Intelligence",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# LOAD CSS
# =========================================================

with open("styles.css") as css:
    st.markdown(
        f"<style>{css.read()}</style>",
        unsafe_allow_html=True
    )

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("#Invoice Intelligence")

    st.caption(
        "AI-Powered Procurement Analytics Platform"
    )

    st.divider()

    selected = option_menu(
        menu_title=None,

        options=[
            "Dashboard",
            "About"
        ],

        icons=[
            "speedometer2",
            "info-circle"
        ],

        default_index=0,

        styles={
            "container": {
                "padding": "0!important",
                "background-color": "#384C76"
            },

            "icon": {
                "color": "#60A5FA",
                "font-size": "18px"
            },

            "nav-link": {
                "font-size": "16px",
                "margin": "6px 0",
                "padding": "12px",
                "border-radius": "10px",
                "--hover-color": "#162033"
            },

            "nav-link-selected": {
                "background-color": "#2563EB"
            }
        }
    )

# =========================================================
# DASHBOARD
# =========================================================

if selected == "Dashboard":

    render_header()

    result = render_prediction()

    if result:

        st.divider()

        render_recommendation(result)

        st.divider()

        render_metrics(result)

        st.divider()

        render_charts(result)

# =========================================================
# ABOUT
# =========================================================

else:

    render_header()

    st.subheader("About Invoice Intelligence")

    st.write(
        """
Invoice Intelligence is an AI-powered procurement analytics platform that combines
Machine Learning, FastAPI, and Streamlit to assist procurement teams in estimating
freight costs and identifying invoices that may require manual review.

---

### Features

- Freight Cost Prediction
- Invoice Risk Detection
- Executive Business Summary
- Decision Support Dashboard
- Interactive Analytics

---

### Technology Stack

- Python
- FastAPI
- Streamlit
- Scikit-Learn
- SQLite
- Plotly
- Pandas
- Joblib

---

### Machine Learning Models

**Regression**

Linear Regression

**Classification**

Random Forest Classifier
"""
    )
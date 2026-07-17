import streamlit as st


def render_header():
    """
    Render dashboard hero header.
    """

    with st.container(border=True):

        left, right = st.columns([5, 1])

        with left:

            st.title("Vendor Invoice Intelligence System")

            st.caption(
                "AI-Powered Freight Cost Prediction & Procurement Analytics Platform"
            )

        with right:

            st.success("● Service Online")
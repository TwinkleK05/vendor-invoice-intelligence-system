import streamlit as st


def render_metrics(result):
    """
    Render dashboard KPI cards.
    """

    st.subheader("Decision Support")

    invoice_amount = result["invoice_amount"]
    predicted_freight = result["predicted_freight"]
    freight_ratio = result["freight_ratio"]
    risk_status = result["risk_status"]

    col1, col2, col3, col4 = st.columns(4)

    # ----------------------------------------------------
    # Invoice Amount
    # ----------------------------------------------------

    with col1:

        with st.container(border=True):

            st.metric(
                label="Invoice Amount",
                value=f"${invoice_amount:,.2f}"
            )

            st.caption("Current invoice value")

    # ----------------------------------------------------
    # Predicted Freight
    # ----------------------------------------------------

    with col2:

        with st.container(border=True):

            st.metric(
                label="Predicted Freight",
                value=f"${predicted_freight:,.2f}"
            )

            st.caption("Regression prediction")

    # ----------------------------------------------------
    # Freight Ratio
    # ----------------------------------------------------

    with col3:

        with st.container(border=True):

            st.metric(
                label="Freight Ratio",
                value=f"{freight_ratio:.2f}%"
            )

            st.caption("Freight as % of invoice")

    # ----------------------------------------------------
    # Risk Status
    # ----------------------------------------------------

    with col4:

        with st.container(border=True):

            if risk_status == "Low Risk":

                st.metric(
                    label="Risk Status",
                    value="Low Risk"
                )

            else:

                st.metric(
                    label="Risk Status",
                    value="Flagged"
                )

            st.caption("Classification result")
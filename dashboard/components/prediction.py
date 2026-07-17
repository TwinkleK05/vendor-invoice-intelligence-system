import streamlit as st
import requests

# ==========================================================
# API Endpoint
# ==========================================================

API_URL = "http://127.0.0.1:8000/analyze"


# ==========================================================
# Prediction Form
# ==========================================================

def render_prediction():
    """
    Render Invoice Analysis form.

    Returns
    -------
    dict
        API response containing both regression and
        classification predictions.
    """

    st.subheader("Analyze Invoice")

    st.write(
        "Enter invoice information below to estimate freight cost "
        "and evaluate invoice risk."
    )

    with st.container(border=True):

        col1, col2 = st.columns(2)

        with col1:

            invoice_amount = st.number_input(
                "Invoice Amount ($)",
                min_value=0.0,
                value=10000.0,
                step=100.0,
                format="%.2f"
            )

            invoice_quantity = st.number_input(
                "Invoice Quantity",
                min_value=1,
                value=20,
                step=1
            )

        with col2:

            total_item_quantity = st.number_input(
                "Total Item Quantity",
                min_value=1,
                value=200,
                step=1
            )

            total_item_dollars = st.number_input(
                "Total Item Value ($)",
                min_value=0.0,
                value=10000.0,
                step=100.0,
                format="%.2f"
            )

        st.write("")

        analyze = st.button(
            "Analyze Invoice",
            use_container_width=True
        )

    if not analyze:
        return None

    payload = {

        "invoice_quantity": float(invoice_quantity),

        "invoice_dollars": float(invoice_amount),

        "total_item_quantity": float(total_item_quantity),

        "total_item_dollars": float(total_item_dollars)

    }

    try:

        with st.spinner("Analyzing invoice..."):

            response = requests.post(
                API_URL,
                json=payload,
                timeout=15
            )

        if response.status_code != 200:

            st.error(
                f"API Error ({response.status_code})"
            )

            return None

        result = response.json()

        result["invoice_amount"] = invoice_amount

        return result

    except requests.exceptions.ConnectionError:

        st.error(
            "Unable to connect to the FastAPI server."
        )

    except requests.exceptions.Timeout:

        st.error(
            "Request timed out."
        )

    except Exception as e:

        st.error(str(e))

    return None
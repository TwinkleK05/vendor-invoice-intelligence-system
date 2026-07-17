import streamlit as st


def render_recommendation(result):
    """
    Render Executive Summary after invoice analysis.
    """

    predicted_freight = result["predicted_freight"]
    invoice_amount = result["invoice_amount"]
    freight_ratio = result["freight_ratio"]
    risk_status = result["risk_status"]

    st.subheader("Executive Summary")

    # =====================================================
    # Business Logic
    # =====================================================

    if risk_status == "Flagged":

        status_color = "red"

        assessment = (
            "The invoice has been classified as requiring "
            "manual review based on the learned risk patterns."
        )

        recommendation = (
            "Verify supplier details, freight charges and "
            "invoice consistency before approval."
        )

    else:

        status_color = "green"

        assessment = (
            "The invoice appears consistent with historical "
            "procurement records and is unlikely to require "
            "additional verification."
        )

        recommendation = (
            "Proceed with the standard procurement approval "
            "workflow."
        )

    # =====================================================
    # Layout
    # =====================================================

    left, right = st.columns([2, 1])

    with left:

        with st.container(border=True):

            st.markdown("### Invoice Analysis")

            st.write("")

            st.markdown(
                f"""
**Estimated Freight**

${predicted_freight:,.2f}

---

**Freight Ratio**

{freight_ratio:.2f}% of invoice value

---

**Assessment**

{assessment}

---

**Recommendation**

{recommendation}
"""
            )

    with right:

        with st.container(border=True):

            st.markdown("### Risk Status")

            st.write("")

            if status_color == "green":

                st.success(risk_status)

            else:

                st.error(risk_status)

            st.metric(
                "Invoice Amount",
                f"${invoice_amount:,.2f}"
            )

            st.metric(
                "Predicted Freight",
                f"${predicted_freight:,.2f}"
            )
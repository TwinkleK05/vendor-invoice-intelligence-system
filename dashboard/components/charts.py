import streamlit as st
import plotly.graph_objects as go


def render_charts(result):
    """
    Render Decision Support analytics.
    """

    invoice_amount = result["invoice_amount"]
    predicted_freight = result["predicted_freight"]
    freight_ratio = result["freight_ratio"]
    risk_status = result["risk_status"]

    col1, col2 = st.columns(2)

    # =====================================================
    # DONUT CHART
    # =====================================================

    with col1:

        fig = go.Figure()

        fig.add_trace(
            go.Pie(
                labels=[
                    "Freight",
                    "Remaining Invoice Value"
                ],
                values=[
                    predicted_freight,
                    invoice_amount - predicted_freight
                ],
                hole=0.72,
                marker=dict(
                    colors=[
                        "#2563EB",
                        "#334155"
                    ]
                ),
                textinfo="percent+label"
            )
        )

        fig.update_layout(
            title="Freight Distribution",
            template="plotly_dark",
            paper_bgcolor="#162033",
            plot_bgcolor="#162033",
            font=dict(
                family="platino linotype, serif",
                color="white"
            ),
            height=420,
            margin=dict(
                l=20,
                r=20,
                t=60,
                b=20
            )
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # =====================================================
    # RISK GAUGE
    # =====================================================

    with col2:

        gauge_value = 25 if risk_status == "Low Risk" else 85

        gauge_color = (
            "#22C55E"
            if risk_status == "Low Risk"
            else "#EF4444"
        )

        fig = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=gauge_value,
                number={
                    "suffix": "%",
                    "font": {"size": 40}
                },
                title={
                    "text": "Risk Indicator"
                },
                gauge={
                    "axis": {
                        "range": [0, 100]
                    },
                    "bar": {
                        "color": gauge_color
                    },
                    "steps": [
                        {
                            "range": [0, 40],
                            "color": "#1E3A8A"
                        },
                        {
                            "range": [40, 70],
                            "color": "#2563EB"
                        },
                        {
                            "range": [70, 100],
                            "color": "#334155"
                        }
                    ]
                }
            )
        )

        fig.update_layout(
            template="plotly_dark",
            paper_bgcolor="#162033",
            plot_bgcolor="#162033",
            font=dict(
                family="Palatino Linotype, serif",
                color="white"
            ),
            height=420,
            margin=dict(
                l=20,
                r=20,
                t=60,
                b=20
            )
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # =====================================================
    # MODEL SUMMARY
    # =====================================================

    st.subheader("Model Summary")

    with st.container(border=True):

        c1, c2, c3 = st.columns(3)

        with c1:
            st.markdown("### Regression")
            st.write("Linear Regression")
            st.caption("Freight Cost Prediction")

        with c2:
            st.markdown("### Classification")
            st.write("Random Forest")
            st.caption("Invoice Risk Detection")

        with c3:
            st.markdown("### Current Analysis")
            st.write(risk_status)
            st.caption(
                f"Freight Ratio: {freight_ratio:.2f}%"
            )
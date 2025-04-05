import streamlit as st
import matplotlib.pyplot as plt
from lang import get_language_dict

def render_risk_tab(t):
    st.subheader(t["risk_tab"])

    asset_type = st.selectbox(t["asset_type"], ["Stock", "Forex", "Crypto", "Commodity", "Option", "ETF"])
    capital = st.number_input(t["capital"], value=10000.0)
    leverage = st.number_input(t["leverage"], value=1.0, min_value=1.0)
    risk_pct = st.slider(t["risk_pct"], 0.5, 10.0, 2.0)
    entry = st.number_input(t["entry"])
    stop = st.number_input(t["stop"])
    tp = st.number_input(t["tp1"])

    if st.button(t["calculate"]):
        risk_per_unit = abs(entry - stop)
        if risk_per_unit == 0:
            st.error(t["risk_error"])
        else:
            effective_capital = capital * leverage
            risk_amount = effective_capital * (risk_pct / 100)
            units = int(risk_amount / risk_per_unit)
            rr = abs(tp - entry) / risk_per_unit
            st.success(f"{t['suggested_qty']} {units}")
            st.info(f"💡 R:R = {rr:.2f}")

            # Optional R:R bar chart
            fig, ax = plt.subplots()
            ax.barh(["Entry"], [1], color="gray")
            ax.barh(["TP"], [rr], color="green")
            ax.barh(["SL"], [-1], color="red")
            ax.set_xlim(-max(rr, 1.5), max(rr, 1.5))
            ax.set_title(f"Risk/Reward Ratio: {rr:.2f}")
            st.pyplot(fig)

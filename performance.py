import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def render_performance_tab(t):
    st.subheader(t["performance_tab"])

    df = st.session_state.trades.copy()
    if df.empty:
        st.info(t["no_data"])
        return

    # Filters
    col1, col2 = st.columns(2)
    with col1:
        tickers = st.multiselect(t["filter_ticker"], df["Ticker"].unique())
        if tickers:
            df = df[df["Ticker"].isin(tickers)]
    with col2:
        dates = st.date_input(t["filter_date"], [])
        if len(dates) == 2:
            df = df[(df["Date"] >= pd.to_datetime(dates[0])) & (df["Date"] <= pd.to_datetime(dates[1]))]

    if df.empty:
        st.info(t["no_data"])
        return

    # Metrics
    df["R:R"] = (df["TP1"] - df["Entry"]) / (df["Entry"] - df["Stop"]).replace(0, 1)
    df["Cumulative P&L"] = df["P&L"].cumsum()

    total = len(df)
    wins = len(df[df["P&L"] > 0])
    losses = len(df[df["P&L"] <= 0])
    win_rate = (wins / total) * 100
    avg_rr = df["R:R"].mean()
    expectancy = df["P&L"].mean()
    drawdown = df["Cumulative P&L"].cummax() - df["Cumulative P&L"]
    max_drawdown = drawdown.max()

    st.metric(t["total_trades"], total)
    st.metric(t["wins"], wins)
    st.metric(t["losses"], losses)
    st.metric(t["win_rate"], f"{win_rate:.2f}%")
    st.metric(t["avg_rr"], f"{avg_rr:.2f}")
    st.metric(t["expectancy"], f"{expectancy:.2f}")
    st.metric(t["drawdown"], f"{max_drawdown:.2f}")

    # Equity curve
    fig1, ax1 = plt.subplots()
    ax1.plot(df["Date"], df["Cumulative P&L"], marker="o")
    ax1.set_title(t["equity_curve"])
    st.pyplot(fig1)

    # Pie chart
    fig2, ax2 = plt.subplots()
    ax2.pie([wins, losses], labels=[t["wins"], t["losses"]], autopct='%1.1f%%', startangle=90)
    ax2.set_title(t["win_pie"])
    st.pyplot(fig2)

    # Monthly P&L
    df["Month"] = pd.to_datetime(df["Date"]).dt.to_period("M").astype(str)
    monthly = df.groupby("Month")["P&L"].sum()
    fig3, ax3 = plt.subplots()
    ax3.bar(monthly.index, monthly.values)
    ax3.set_title(t["monthly"])
    ax3.set_ylabel("P&L")
    ax3.set_xlabel("Month")
    st.pyplot(fig3)

    # Top Trades
    st.markdown("### 🏆 " + t["top_trades"])
    top = df.sort_values("P&L", ascending=False).head(5)
    st.dataframe(top[["Date", "Ticker", "P&L", "Strategy", "Tag"]])

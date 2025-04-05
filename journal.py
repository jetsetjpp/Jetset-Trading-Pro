import streamlit as st
import pandas as pd
from datetime import datetime
from utils import save_screenshot, detect_sentiment, calculate_pnl, render_image, import_trades, export_trades

def render_journal_tab(t):
    st.subheader(t["journal_tab"])

    if "trades" not in st.session_state:
        st.session_state.trades = pd.DataFrame(columns=[
            "Date", "Time", "Ticker", "Type", "Entry", "Stop", "TP1", "TP2",
            "Exit", "Qty", "Fees", "Strategy", "Notes", "Tag", "Sentiment", "Screenshot", "P&L"
        ])

    with st.form("entry_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            date = st.date_input(t["date"], datetime.today())
            time = st.time_input(t["time"], datetime.now().time())
            ticker = st.text_input(t["ticker"])
            trade_type = st.selectbox(t["type"], [t["buy"], t["sell"]])
            entry = st.number_input(t["entry"], value=0.0)
            stop = st.number_input(t["stop"], value=0.0)
            tp1 = st.number_input(t["tp1"], value=0.0)
            tp2 = st.number_input(t["tp2"], value=0.0)
        with col2:
            exit = st.number_input(t["exit"], value=0.0)
            qty = st.number_input(t["qty"], value=0)
            fees = st.number_input(t["fees"], value=0.0)
            strat = st.text_input(t["strategy"])
            notes = st.text_area(t["notes"])
            tag = st.selectbox(t["tag"], ["Jetset Trading", "Breakout", "Pullback", "News"])
            screenshot = st.file_uploader(t["upload"], type=["png", "jpg", "jpeg"])
        submit = st.form_submit_button(t["save"])

        if submit:
            sentiment = detect_sentiment(notes)
            pnl = calculate_pnl(entry, exit, qty, fees, trade_type)
            filepath = save_screenshot(screenshot) if screenshot else ""
            new = pd.DataFrame([{
                "Date": date, "Time": time.strftime("%H:%M"), "Ticker": ticker, "Type": trade_type,
                "Entry": entry, "Stop": stop, "TP1": tp1, "TP2": tp2, "Exit": exit, "Qty": qty,
                "Fees": fees, "Strategy": strat, "Notes": notes, "Tag": tag, "Sentiment": sentiment,
                "Screenshot": filepath, "P&L": pnl
            }])
            st.session_state.trades = pd.concat([st.session_state.trades, new], ignore_index=True)
            st.success("Trade saved!")

    st.dataframe(st.session_state.trades)

    # Screenshot preview
    st.markdown("### 🔍 " + t["upload"])
    if not st.session_state.trades.empty:
        options = st.session_state.trades.apply(lambda r: f"{r['Date']} - {r['Ticker']} - {r['Time']}", axis=1)
        selected = st.selectbox("Select", options)
        idx = st.session_state.trades.index[options.tolist().index(selected)]
        row = st.session_state.trades.loc[idx]
        st.write(f"**{row['Date']} {row['Time']} - {row['Ticker']}**")
        st.write(f"💼 {row['Type']} 🎯 {row['Entry']} 🛑 {row['Stop']} 🎯 TP1: {row['TP1']} ✅ {row['Exit']}")
        render_image(row["Screenshot"])

    # Set Exit Price
    st.markdown("### 🟢 " + t["update_exit"])
    open_trades = st.session_state.trades[st.session_state.trades["Exit"] == 0.0]
    if not open_trades.empty:
        opts = open_trades.apply(lambda r: f"{r['Date']} - {r['Ticker']}", axis=1)
        sel = st.selectbox("Select trade", opts)
        idx = open_trades.index[opts.tolist().index(sel)]
        new_exit = st.number_input("New Exit Price", min_value=0.0)
        if st.button(t["set_exit"]):
            row = st.session_state.trades.loc[idx]
            new_pnl = calculate_pnl(row["Entry"], new_exit, row["Qty"], row["Fees"], row["Type"])
            st.session_state.trades.at[idx, "Exit"] = new_exit
            st.session_state.trades.at[idx, "P&L"] = new_pnl
            st.success("Exit updated")

    # Delete Trade
    st.markdown("### " + t["delete_trade"])
    if not st.session_state.trades.empty:
        opts = st.session_state.trades.apply(lambda r: f"{r['Date']} - {r['Ticker']} - {r['Time']}", axis=1)
        sel = st.selectbox("Delete", opts)
        idx = st.session_state.trades.index[opts.tolist().index(sel)]
        if st.button(t["confirm_delete"]):
            st.session_state.trades.drop(idx, inplace=True)
            st.session_state.trades.reset_index(drop=True, inplace=True)
            st.success("Deleted")

    # Export
    st.markdown("### 📤 " + t["export"])
    if not st.session_state.trades.empty:
        excel = export_trades(st.session_state.trades.copy())
        st.download_button("📥 Excel", data=excel, file_name="journal.xlsx")

    # Import
    uploaded = st.file_uploader(t["import"], type="xlsx")
    if uploaded:
        st.session_state.trades = import_trades(uploaded)
        st.success("Imported trades from Excel!")

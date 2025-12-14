# streamlit_app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="AI Patrol Dashboard", layout="wide")

st.title("🚓 AI Patrol Simulation Dashboard")

df = pd.read_csv("patrol_simulation_log.csv")

# Risk Line Chart
st.subheader("📉 Average Risk Level Over Time")
st.line_chart(df.set_index("step")["average_risk"])

# Events Handled
st.subheader("📈 Cumulative Events Handled")
st.line_chart(df.set_index("step")["events_handled"])

# Zone Summary
st.subheader("🗺️ Final Zone Risk Status")
final_step = df[df["step"] == df["step"].max()]
st.dataframe(final_step)

st.markdown("---")
st.caption("Built with ❤️ using TensorFlow Probability, TomTom API, and Streamlit.")

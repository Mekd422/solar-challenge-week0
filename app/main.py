import streamlit as st
import pandas as pd
import utils


# --- Page Setup ---
st.set_page_config(page_title="Solar Potential Dashboard", layout="wide")

st.title("Solar Potential Across Countries")

# --- Sidebar: Country selection ---
selected_countries = st.multiselect(
    "Select countries to display:",
    ["Benin", "Sierra Leone", "Togo"],
    default=["Benin", "Sierra Leone", "Togo"]
)

if not selected_countries:
    st.warning("Please select at least one country.")
    st.stop()

# --- Load Data ---
data_dict = {}
for country in selected_countries:
    data_dict[country] = utils.load_country_data(country)

# --- Metric Selection ---
metric = st.selectbox("Select metric to visualize:", ["GHI", "DNI", "DHI"])

# --- Boxplot ---
st.subheader(f"Boxplot of {metric}")
utils.plot_metric_boxplot(data_dict, metric)

# --- Summary Table ---
st.subheader("Summary Statistics")
summary_df = pd.DataFrame()
for country, df in data_dict.items():
    stats = df[[metric]].agg(['mean','median','std']).T
    stats['Country'] = country
    summary_df = pd.concat([summary_df, stats])

summary_df = summary_df[['Country','mean','median','std']].reset_index().rename(columns={'index':'Metric'})
st.dataframe(summary_df)

st.markdown("""
---
*This dashboard uses cleaned solar irradiance data from Benin, Sierra Leone, and Togo.*
""")

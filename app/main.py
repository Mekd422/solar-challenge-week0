# app/main.py
import streamlit as st
from datetime import datetime
import pandas as pd
from utils import summary_stats, line_chart, box_chart

# -------- PAGE CONFIG --------
st.set_page_config(
    page_title="☀️ Solar Energy Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------- CUSTOM STYLES --------
st.markdown("""
<style>
#MainMenu, footer, header {visibility: hidden;}
.metric-card {
    background-color: #f9f9f9;
    border-radius: 10px;
    padding: 20px;
    margin: 10px;
    text-align: center;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
}
.css-1d391kg {padding-top: 1rem;} 
</style>
""", unsafe_allow_html=True)

# -------- MAIN TITLE --------
st.title("☀️ Solar Farm Data Explorer")
st.markdown("#### Gain insights into solar irradiance, temperature, and humidity trends across multiple countries.")

# -------- FILE UPLOADER --------
st.sidebar.header("Upload Country Data")
uploaded_files = st.sidebar.file_uploader(
    "Upload one CSV per country",
    type=["csv"],
    accept_multiple_files=True
)

data_dict = {}
if uploaded_files:
    for f in uploaded_files:
        df = pd.read_csv(f, parse_dates=["Timestamp"])
        country_name = f.name.split(".")[0].replace("_", " ").title()
        data_dict[country_name] = df
    st.sidebar.success(f"Loaded {len(data_dict)} files!")

# -------- TOP FILTERS --------
if data_dict:
    countries = list(data_dict.keys())
    selected_countries = st.multiselect("Select Countries", countries, default=countries)
    metric = st.selectbox("Select Metric", ['GHI', 'DNI', 'DHI', 'Tamb', 'RH'])
else:
    selected_countries = []
    metric = None
    st.warning("Please upload CSV files to activate the dashboard.")

# -------- SIDEBAR --------
with st.sidebar:
    st.header("⚙️ Advanced Filters")
    date_filter = st.checkbox("Enable Date Range Filter")
    start_date, end_date = None, None
    if date_filter:
        start_date = st.date_input("Start Date", datetime(2025,1,1))
        end_date = st.date_input("End Date", datetime(2025,12,31))

# -------- DATA VISUALIZATION --------
tab1, tab2, tab3 = st.tabs(["📈 Trends", "📊 Summary Stats", "🌍 Country Comparison"])

with tab1:
    st.subheader(f"{metric} Over Time")
    if selected_countries and data_dict:
        for c in selected_countries:
            df = data_dict[c]
            if date_filter:
                df = df[(df["Timestamp"] >= pd.Timestamp(start_date)) & (df["Timestamp"] <= pd.Timestamp(end_date))]
            st.plotly_chart(line_chart(df, metric, c), use_container_width=True)
    else:
        st.warning("Please select at least one country and ensure data is uploaded.")

with tab2:
    st.subheader("📊 Summary Statistics")
    if selected_countries and data_dict:
        stats = [ {"Country": c, **summary_stats(data_dict[c], metric)} for c in selected_countries ]
        st.dataframe(pd.DataFrame(stats), use_container_width=True)

with tab3:
    st.subheader("🌍 Cross-Country Comparison")
    if selected_countries and data_dict:
        dfs = []
        for c in selected_countries:
            df = data_dict[c].copy()
            df["Country"] = c
            dfs.append(df)
        if dfs:
            combined = pd.concat(dfs)
            st.plotly_chart(box_chart(combined, metric), use_container_width=True)
    else:
        st.warning("No data to display. Please select countries and upload data.")

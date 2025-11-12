# app/utils.py
import pandas as pd
import plotly.express as px
import streamlit as st

# -------- DATA LOADING --------
@st.cache_data
def load_data(country):
    """Load cleaned CSV data for a given country"""
    path = f"../data/{country.lower().replace(' ', '_')}_clean.csv"
    df = pd.read_csv(path, parse_dates=["Timestamp"])
    return df

# -------- SUMMARY STATISTICS --------
def summary_stats(df, metric):
    return {
        "Mean": round(df[metric].mean(), 2),
        "Median": round(df[metric].median(), 2),
        "Std Dev": round(df[metric].std(), 2)
    }

# -------- PLOTS --------
def line_chart(df, metric, country):
    fig = px.line(
        df,
        x="Timestamp",
        y=metric,
        title=f"{metric} Trend: {country}",
        color_discrete_sequence=["#FFB703"]
    )
    return fig

def box_chart(df, metric):
    fig = px.box(
        df,
        x="Country",
        y=metric,
        color="Country",
        title=f"{metric} Distribution Across Countries",
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    return fig

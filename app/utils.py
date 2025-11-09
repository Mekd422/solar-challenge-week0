import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt

# Load cleaned CSV by country name
def load_country_data(country):
    file_map = {
        "Benin": "../data/benin_clean.csv",
        "Sierra Leone": "../data/sierra-leone_clean.csv",
        "Togo": "../data/togo_clean.csv"
    }
    return pd.read_csv(file_map[country])

# Generate boxplot for a metric (GHI, DNI, DHI) across countries
def plot_metric_boxplot(df_dict, metric):
    plt.figure(figsize=(8,6))
    combined_df = pd.DataFrame()
    for country, df in df_dict.items():
        temp = df[[metric]].copy()
        temp['Country'] = country
        combined_df = pd.concat([combined_df, temp], ignore_index=True)

    sns.boxplot(x='Country', y=metric, data=combined_df, palette='viridis')
    plt.title(f"{metric} Comparison Across Countries")
    plt.ylabel(metric)
    plt.xlabel("Country")
    plt.tight_layout()
    st.pyplot(plt.gcf())
    plt.clf()

#  10 Academy Week 0 – Solar Data Discovery Challenge  

## Project Overview  
This repository contains my work for **10 Academy’s Artificial Intelligence Mastery – Week 0 Challenge: Solar Data Discovery**.  

The project focuses on analyzing and comparing solar energy potential across **Benin**, **Togo**, and **Sierra Leone** using high-resolution solar radiation and environmental data.  

As an Analytics Engineer at *MoonLight Energy Solutions*, the goal is to perform end-to-end data profiling, cleaning, exploratory analysis, and cross-country comparison to support data-driven decisions on where to prioritize solar investment.

---

##  Business Objective  
The company seeks to identify regions with the **highest solar energy potential** and optimal environmental conditions for new solar installations.  
Our analysis delivers data-backed insights to guide strategic solar investments that maximize operational efficiency and sustainability.  

---

##  Project Objectives  
1.  Set up version control, development environment, and CI/CD workflows.  
2.  Profile, clean, and validate solar farm data for each country.  
3.  Perform detailed exploratory data analysis (EDA).  
4.  Compare irradiance metrics across Benin, Togo, and Sierra Leone.  
5.  Derive insights for solar energy potential ranking.  
6.  (Bonus) Develop an interactive Streamlit dashboard for visualization.

---

##  Tasks Summary  

| Task | Description | Branch | Status |
|:--|:--|:--|:--|
| **Task 1:** Git & Environment Setup | Repo creation, venv setup, CI workflow, basic README | `setup-task` |  Completed |
| **Task 2:** Data Profiling & EDA | Cleaning, outlier detection, time-series analysis | `eda-benin`, `eda-togo`, `eda-sierraleone` |  Completed |
| **Task 3:** Cross-Country Comparison | Compare irradiance metrics and rank countries | `compare-countries` | Completed |
| **Task 4:** Interactive Dashboard | Streamlit app for interactive visualization | `dashboard-dev` | 🔄 In progress |

---

##  Dataset Overview  
The data represents one full year of minute-level solar and environmental measurements.  

| Column | Description |
|:--|:--|
| `Timestamp` | Observation datetime |
| `GHI`, `DNI`, `DHI` | Global, Direct, and Diffuse solar irradiance (W/m²) |
| `ModA`, `ModB` | Sensor irradiance readings |
| `Tamb` | Ambient temperature (°C) |
| `RH` | Relative humidity (%) |
| `WS`, `WSgust` | Wind speed metrics (m/s) |
| `BP` | Barometric pressure (hPa) |
| `Cleaning` | 1 = Cleaning event occurred |
| `Precipitation` | Rain rate (mm/min) |
| `TModA`, `TModB` | Module temperatures (°C) |
| `Comments` | Additional notes – mostly null |

Each file contained ~525 600 rows; only `Comments` had >5 % missing values and was dropped.

---

##  Data Cleaning & Preparation  
1. Removed columns with >5 % missing values (`Comments`).  
2. Detected and handled outliers using **Z-score >|3|** threshold.  
3. Imputed missing numeric values using the median.  
4. Converted timestamps to datetime and extracted temporal features.  
5. Saved cleaned data as:  
   - `benin_clean.csv`  
   - `togo_clean.csv`  
   - `sierraleone_clean.csv`

---

##  Exploratory Data Analysis (EDA)  

### Key Findings per Country  

#### **Benin**
- Stable, high irradiance (GHI ≈ median > Togo & Sierra Leone).  
- Minimal missing data; clean sensor readings.  
- Clear midday irradiance peak and strong daily pattern.

#### **Togo**
- Average GHI: 230.55 W/m²; DNI: 151.26 W/m²; DHI: 116.44 W/m².  
- Ambient Temp: 27.75 °C ± 4.76 °C.  
- Humidity: ~55 %.  
- Moderate irradiance with typical tropical variability.

#### **Sierra Leone**
- Similar data completeness to others.  
- Lower irradiance overall, higher humidity and diffuse component.  
- Indicates more frequent cloud cover affecting direct radiation.

### General EDA Observations  
- Cleaning events slightly increased ModA/ModB readings → cleaner panels yield better performance.  
- RH inversely correlated with temperature and solar irradiance.  
- GHI, DNI, and DHI follow expected diurnal cycles.

---

##  Cross-Country Comparison  

| Metric | Highest Median | Lowest Median | Notes |
|:--|:--|:--|:--|
| **GHI** | Benin | Sierra Leone | Benin receives the most consistent solar radiation. |
| **DNI** | Benin | Sierra Leone | Direct irradiance strongest in Benin, moderate in Togo. |
| **DHI** | Sierra Leone ≈ Benin | – | Diffuse radiation relatively even across countries. |

**Statistical Test:** One-way ANOVA on GHI → *p < 0.05* → significant differences exist.  

**Solar Potential Ranking:**  
1️⃣ Benin   — Highest irradiance, most stable readings.  
2️⃣ Togo    — Moderate irradiance, favorable climate.  
3️⃣ Sierra Leone — Lower irradiance, higher humidity.  

---

##  Visualizations  
- Distribution histograms for irradiance and temperature.  
- Correlation heatmaps (GHI, DNI, DHI, Tamb, RH).  
- Boxplots for cross-country comparison.  
- Wind-rose and scatter plots for WS vs GHI analysis.  

---

##  Tools & Technologies  
| Category | Tools |
|:--|:--|
| **Language** | Python 3.10 + |
| **Libraries** | Pandas, NumPy, Matplotlib, Seaborn, SciPy, Plotly |
| **Dashboard** | Streamlit *(in progress)* |
| **Version Control** | Git, GitHub |
| **CI/CD** | GitHub Actions |
| **Environment** | venv / requirements.txt |




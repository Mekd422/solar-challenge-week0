# Solar Data Analysis – Tasks 2 & 3  

## Overview  
This stage of the *Solar Data Discovery* challenge focused on exploring, cleaning, and analyzing solar and environmental datasets from **Benin**, **Sierra Leone**, and **Togo**.  
The main goal was to understand each country’s solar potential by examining irradiance patterns, environmental conditions, and data quality, and then comparing them quantitatively and visually.  

---

## Objectives  
1. Perform data profiling and identify missing values or anomalies.  
2. Clean the datasets to ensure consistency and accuracy.  
3. Conduct exploratory data analysis (EDA) to understand trends and distributions.  
4. Compare **Global Horizontal Irradiance (GHI)**, **Direct Normal Irradiance (DNI)**, and **Diffuse Horizontal Irradiance (DHI)** across the three countries.  
5. Summarize results to identify the country with the highest solar energy potential.  

---

## Data Summary  
Each dataset contained **525,600 records**, representing minute-level sensor data over a year.  
All numerical columns were complete except for the `Comments` column, which contained 100% missing values and was dropped.  

| Feature | Description |
|:--|:--|
| `GHI`, `DNI`, `DHI` | Solar irradiance components (W/m²) |
| `ModA`, `ModB` | Module temperature sensors |
| `Tamb` | Ambient temperature |
| `RH` | Relative humidity |
| `WS`, `WSgust` | Wind speed metrics |
| `BP` | Barometric pressure |
| `Cleaning`, `Precipitation` | Maintenance and weather indicators |

---

## Data Cleaning Steps  
1. Removed columns with >5% missing values (`Comments`).  
2. Checked for duplicate timestamps – none found.  
3. Replaced invalid or extreme outliers using **Z-score filtering (|z| > 3)** and median imputation.  
4. Standardized datetime formats and extracted time-based features (`hour`, `day`, `month`).  
5. Verified numeric consistency and saved cleaned versions:  
   - `benin_clean.csv`  
   - `sierraleone_clean.csv`  
   - `togo_clean.csv`  

---

## Exploratory Data Analysis  

### Descriptive Statistics (Example – Togo)
| Metric | Mean | Std | Median | Min | Max |
|:--|--:|--:|--:|--:|--:|
| GHI | 230.55 | 322.53 | 2.10 | –12.7 | 1424.0 |
| DNI | 151.26 | 250.96 | 0.00 | 0 | 1004.5 |
| DHI | 116.44 | 156.52 | 2.50 | 0 | 805.7 |
| Tamb (°C) | 27.75 | 4.76 | 27.2 | 14.9 | 41.4 |
| RH (%) | 55.01 | 28.78 | 59.3 | 3.3 | 99.8 |

### Observations  
- GHI, DNI, and DHI follow clear diurnal patterns with near-zero nighttime values.  
- Temperature and humidity vary within expected tropical ranges.  
- Cleaning events correlate with slight improvements in module sensor readings.  

---

## Cross-Country Comparison  

### Boxplot Summaries  
- **GHI:** Benin shows the highest median and upper range values.  
- **DNI:** Benin leads, followed by Togo, while Sierra Leone records the lowest direct irradiance.  
- **DHI:** Comparable across countries, slightly higher in Sierra Leone due to higher cloudiness.  

*(Figures 1–3: GHI, DNI, and DHI Comparison Boxplots)*  

### Statistical Analysis  
A one-way **ANOVA test** on GHI across countries yielded **p < 0.05**, confirming statistically significant differences in solar irradiance.  

| Country | GHI Level | DNI Level | Solar Potential | Summary |
|:--|:--|:--|:--|:--|
| **Benin** | High | High |  Very High | Most stable and intense irradiance. |
| **Togo** | Moderate – High | Moderate | High | Balanced potential, good reliability. |
| **Sierra Leone** | Low | Low |  Moderate | High humidity and cloud variability. |

---

## Key Insights  
- **Benin** demonstrates the strongest solar potential overall.  
- **Togo** provides reliable irradiance with moderate variability — good for hybrid solar setups.  
- **Sierra Leone** has the lowest irradiance, influenced by higher humidity and cloud coverage.  
- Clean, complete data now ready for dashboard visualization and predictive modeling.  

---

## Tools and Libraries  
| Category | Tools |
|:--|:--|
| Data Analysis | Python, Pandas, NumPy, SciPy |
| Visualization | Matplotlib, Seaborn, Plotly |
| Version Control | Git, GitHub |
| Environment | venv, requirements.txt |





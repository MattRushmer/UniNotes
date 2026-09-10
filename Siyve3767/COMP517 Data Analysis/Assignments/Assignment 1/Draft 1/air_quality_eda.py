"""
COMP517 - Data Analysis
Assignment 1: Data Exploration and Analysis
Dataset: Global Air Quality 2023 (messy version)

This script performs the full EDA pipeline required by the assignment brief:
  1. Load and summarise the dataset
  2. Pre-process (missing values, duplicates, outliers)
  3. Explore and visualise the clean dataset
  4. Multivariate analysis (correlation, categorical x categorical, aggregation,
     temperature -> pollution risk relationship)

All figures are saved to the "figures" folder as PNG files, and all printed
output is what the accompanying report is based on. Run this file from the
"Draft 1" folder (it expects the dataset one level up, inside
"Dataset - Global Air Quality 2023").

Run with:  python air_quality_eda.py
"""

import os

import matplotlib
matplotlib.use("Agg")  # save figures to disk without opening windows
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set_theme(style="whitegrid")

DATA_PATH = os.path.join(
    "..", "Dataset - Global Air Quality 2023", "global_air_quality_data_messy.csv"
)
FIG_DIR = "figures"
os.makedirs(FIG_DIR, exist_ok=True)

POLLUTANTS = ["PM2.5", "PM10", "NO2", "SO2", "CO", "O3"]
WEATHER = ["Temperature", "Humidity", "Wind Speed"]
NUMERIC_COLS = POLLUTANTS + WEATHER


def savefig(name):
    path = os.path.join(FIG_DIR, name)
    plt.tight_layout()
    plt.savefig(path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"  saved {path}")


# ---------------------------------------------------------------------------
# 1. LOAD AND SUMMARISE
# ---------------------------------------------------------------------------
print("\n" + "=" * 70)
print("1. LOAD AND SUMMARISE")
print("=" * 70)

df = pd.read_csv(DATA_PATH)

print(f"\nShape: {df.shape[0]} rows x {df.shape[1]} columns")
print("\nFirst 5 rows:")
print(df.head())

print("\nColumn dtypes:")
print(df.dtypes)

print("\ndf.info():")
df.info()

print("\nMissing values per column:")
print(df.isnull().sum())

print("\nMissing values as % of rows:")
print((df.isnull().sum() / len(df) * 100).round(2))


# ---------------------------------------------------------------------------
# 2. PRE-PROCESSING
# ---------------------------------------------------------------------------
print("\n" + "=" * 70)
print("2. PRE-PROCESSING")
print("=" * 70)

# --- 2a. Standardise text fields (case/spacing issues introduced by the
# "messy" generator) before doing anything else, so that "SYDNEY", " Sydney",
# "sydney " etc. are treated as the same city.
print("\nUnique City values before cleaning:", df["City"].nunique())
print("Unique Country values before cleaning:", df["Country"].nunique())

# Note: no .astype(str) here on purpose -- casting to str before cleaning
# would turn any real missing City/Country value into the literal string
# "nan", which would then silently pass the isnull() check in Step 2c below
# and never get imputed. Both columns are already string-typed by
# pd.read_csv wherever a value exists, so .str.strip()/.str.title() work
# directly and leave genuine NaNs as NaN for Step 2c to handle.
df["City"] = df["City"].str.strip().str.title()
df["Country"] = df["Country"].str.strip().str.title()

# .str.title() mangles country acronyms (UAE -> Uae, UK -> Uk, USA -> Usa);
# restore the correct acronym casing for known cases.
ACRONYM_FIX = {"Uae": "UAE", "Uk": "UK", "Usa": "USA"}
df["Country"] = df["Country"].replace(ACRONYM_FIX)

print("Unique City values after cleaning:", df["City"].nunique())
print("Unique Country values after cleaning:", df["Country"].nunique())

# --- 2b. Parse Date (format is M/D/YYYY, confirmed by values such as 10/27
# which cannot be interpreted as D/M since there is no 27th month)
df["Date"] = pd.to_datetime(df["Date"], format="%m/%d/%Y", errors="coerce")
print("\nRows where Date failed to parse:", df["Date"].isna().sum())
df["Quarter"] = df["Date"].dt.month % 12 // 3 + 1
# Hemisphere-neutral labels: the dataset mixes Northern-Hemisphere countries
# (USA, Canada, Germany, ...) and Southern-Hemisphere countries (South
# Africa, Australia, ...), so calendar "Summer/Winter" season names would be
# correct for one group and backwards for the other. Grouping by calendar
# quarter (month range only, no hemisphere-specific season name) avoids
# that ambiguity while still testing for any time-of-year pattern.
quarter_map = {1: "Q1: Dec-Feb", 2: "Q2: Mar-May",
               3: "Q3: Jun-Aug", 4: "Q4: Sep-Nov"}
df["Quarter"] = df["Quarter"].map(quarter_map)

# --- 2c. Missing values -----------------------------------------------------
print("\n--- Handling missing values ---")
missing_before = df.isnull().sum()
print(missing_before[missing_before > 0])

for col in NUMERIC_COLS:
    if df[col].isnull().sum() == 0:
        print(f"{col}: no missing values, skipped")
        continue
    skew = df[col].skew()
    print(f"{col}: skew={skew:.2f} -> using {'median' if abs(skew) > 0.5 else 'mean'}")

# Impute per-Country rather than with one global statistic. A single global
# fill value gets repeated across every country's subgroup, which pins every
# country's *median* to that same imputed number once enough rows share it
# (verified: with a global fill, 9 of 10 top countries showed an identical
# PM2.5 median of 77.65, masking real country-to-country differences that
# only reappear once imputation is done within each country's own values).
for col in NUMERIC_COLS:
    if df[col].isnull().sum() == 0:
        continue
    skew = df[col].skew()
    method = "median" if abs(skew) > 0.5 else "mean"
    if method == "median":
        df[col] = df[col].fillna(df.groupby("Country")[col].transform("median"))
    else:
        df[col] = df[col].fillna(df.groupby("Country")[col].transform("mean"))
    # Backstop in case any country's own subgroup were entirely missing for
    # this column (not the case here, but avoids a silent leftover NaN).
    df[col] = df[col].fillna(df[col].mean())
    print(f"  filled {col} missing values with per-Country {method}")

# Categorical missing values, if any: mode for City/Country.
for col in ["City", "Country"]:
    if df[col].isnull().sum() > 0:
        mode_val = df[col].mode()[0]
        df[col] = df[col].fillna(mode_val)
        print(f"  filled {col} missing values with mode ({mode_val})")

# Date: the rows in this dataset are shuffled (not sorted by city or by
# date), so there is no meaningful order to interpolate a missing date
# from -- positionally interpolating between two unrelated cities' dates
# would produce a fabricated timestamp. Rows with an unparseable date are
# dropped instead, since a date cannot be safely guessed here.
if df["Date"].isnull().sum() > 0:
    before = df["Date"].isnull().sum()
    df = df.dropna(subset=["Date"])
    print(f"  dropped {before} rows with an unparseable Date")

print("\nMissing values after cleaning:")
print(df.isnull().sum())

# --- 2d. Duplicates ----------------------------------------------------------
print("\n--- Handling duplicates ---")
exact_dupes = df.duplicated().sum()
print(f"Exact duplicate rows (all columns identical): {exact_dupes}")

key_dupes = df.duplicated(subset=["City", "Country", "Date"]).sum()
print(f"Rows sharing the same City+Country+Date: {key_dupes}")

df = df.drop_duplicates()
print(f"Shape after dropping exact duplicates: {df.shape}")

# --- 2e. Outliers -------------------------------------------------------------
# Physical-validity filter is applied first, so the IQR bounds computed
# below are based on the same final dataset used everywhere downstream
# (avoids computing bounds on one version of df and plotting another).
before_rows = len(df)
df = df[(df["Humidity"] >= 0) & (df["Humidity"] <= 100)]
df = df[(df["Wind Speed"] >= 0)]
print(f"\nRemoved {before_rows - len(df)} rows with physically impossible "
      f"Humidity/Wind Speed values")

print("\n--- Handling outliers (IQR method) ---")
outlier_summary = {}
outlier_masks = {}
for col in NUMERIC_COLS:
    q1, q3 = df[col].quantile([0.25, 0.75])
    iqr = q3 - q1
    lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    mask = (df[col] < lower) | (df[col] > upper)
    outlier_summary[col] = mask.sum()
    outlier_masks[col] = mask
    print(f"{col}: {mask.sum()} outliers (bounds: {lower:.2f} to {upper:.2f})")

# Cross-check with z-score on PM2.5 (most safety-critical pollutant)
z = (df["PM2.5"] - df["PM2.5"].mean()) / df["PM2.5"].std()
print(f"\nPM2.5 z-score outliers (|z|>3): {(z.abs() > 3).sum()}")

# Decision: pollutant outliers are kept (real pollution spikes are the most
# important events in an air-quality dataset); no pollutant values were
# removed or transformed on outlier grounds.

# Scatterplots: outlier vs non-outlier points for the two headline
# pollutants, reusing the masks computed above rather than recomputing them.
for col in ["PM2.5", "PM10"]:
    is_outlier = outlier_masks[col]

    plt.figure(figsize=(8, 5))
    plt.scatter(df.index[~is_outlier], df.loc[~is_outlier, col],
                s=8, alpha=0.4, label="Non-outlier", color="steelblue")
    plt.scatter(df.index[is_outlier], df.loc[is_outlier, col],
                s=14, alpha=0.8, label="Outlier", color="crimson")
    plt.title(f"{col}: Outliers vs Non-Outliers (IQR method)")
    plt.xlabel("Row index")
    plt.ylabel(f"{col} concentration")
    plt.legend()
    savefig(f"outliers_{col.replace('.', '')}.png")

# Boxplots for all pollutants together (spread + outliers)
plt.figure(figsize=(10, 6))
sns.boxplot(data=df[POLLUTANTS])
plt.title("Boxplots of Pollutant Concentrations (Outlier Detection)")
plt.ylabel("Concentration")
plt.xlabel("Pollutant")
savefig("boxplot_pollutants.png")


# ---------------------------------------------------------------------------
# 3. EXPLORE AND VISUALISE THE CLEAN DATASET
# ---------------------------------------------------------------------------
print("\n" + "=" * 70)
print("3. EXPLORE AND VISUALISE THE CLEAN DATASET")
print("=" * 70)

print("\nSummary statistics (numeric columns):")
summary_stats = df[NUMERIC_COLS].describe().T
summary_stats = summary_stats.rename(columns={"50%": "median"})
print(summary_stats)
summary_stats.to_csv(os.path.join(FIG_DIR, "summary_statistics.csv"))

# Histograms for numeric columns
fig, axes = plt.subplots(3, 3, figsize=(14, 10))
for ax, col in zip(axes.flat, NUMERIC_COLS):
    sns.histplot(df[col], kde=True, ax=ax, color="teal")
    ax.set_title(f"Distribution of {col}")
    ax.set_xlabel(col)
    ax.set_ylabel("Frequency")
for ax in axes.flat[len(NUMERIC_COLS):]:
    ax.axis("off")
savefig("histograms_numeric.png")

# Bar chart: record count by top 10 countries
plt.figure(figsize=(10, 6))
top_countries = df["Country"].value_counts().head(10)
sns.barplot(x=top_countries.values, y=top_countries.index, hue=top_countries.index,
            palette="viridis", legend=False)
plt.title("Top 10 Countries by Number of Air Quality Records")
plt.xlabel("Number of Records")
plt.ylabel("Country")
savefig("bar_top_countries.png")

# Pie chart: record share by calendar quarter
plt.figure(figsize=(8, 6))
quarter_counts = df["Quarter"].value_counts().sort_index()
wedges, _, _ = plt.pie(quarter_counts.values, autopct="%1.1f%%", pctdistance=0.8,
                        colors=sns.color_palette("pastel"))
plt.title("Share of Records by Calendar Quarter")
plt.legend(wedges, quarter_counts.index, title="Quarter",
           loc="center left", bbox_to_anchor=(1.0, 0.5))
savefig("pie_quarter_share.png")

# Box plots for weather variables
plt.figure(figsize=(10, 6))
sns.boxplot(data=df[WEATHER])
plt.title("Boxplots of Weather Variables")
plt.ylabel("Value")
plt.xlabel("Variable")
savefig("boxplot_weather.png")


# ---------------------------------------------------------------------------
# 4. MULTIVARIATE ANALYSIS
# ---------------------------------------------------------------------------
print("\n" + "=" * 70)
print("4. MULTIVARIATE ANALYSIS")
print("=" * 70)

# --- 4a. Correlation heatmap ---
corr = df[NUMERIC_COLS].corr()
print("\nCorrelation matrix:")
print(corr.round(2))

strong_pairs = []
for i in range(len(corr.columns)):
    for j in range(i + 1, len(corr.columns)):
        r = corr.iloc[i, j]
        if abs(r) > 0.7:
            strong_pairs.append((corr.columns[i], corr.columns[j], round(r, 2)))
print("\nStrong correlations (|r| > 0.7):", strong_pairs if strong_pairs else "None found")

plt.figure(figsize=(9, 7))
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", center=0,
            square=True, cbar_kws={"label": "Pearson r"})
plt.title("Correlation Heatmap of Pollutant and Weather Variables")
savefig("correlation_heatmap.png")

# --- 4b. Categorical x categorical -> record count ---
# Rationale: Country and Quarter are both meaningful categorical groupings
# for an air-quality dataset (do certain countries have more/fewer records
# in certain parts of the year?), and every row is one record, so a
# Country x Quarter count grid is a genuine "how does count vary across two
# categorical variables" plot.
top5_countries = df["Country"].value_counts().head(5).index
cross = pd.crosstab(df[df["Country"].isin(top5_countries)]["Country"],
                     df[df["Country"].isin(top5_countries)]["Quarter"])
print("\nRecord counts, Country (top 5) x Quarter:")
print(cross)

plt.figure(figsize=(9, 5))
sns.heatmap(cross, annot=True, fmt="d", cmap="YlGnBu")
plt.title("Record Count by Country (Top 5) and Calendar Quarter")
plt.xlabel("Quarter")
plt.ylabel("Country")
savefig("heatmap_country_quarter_count.png")

# --- 4c. Aggregation: mean & median PM2.5 by Country (top 10 by volume) ---
agg = (df[df["Country"].isin(df["Country"].value_counts().head(10).index)]
       .groupby("Country")["PM2.5"].agg(["mean", "median"]).round(2)
       .sort_values("mean", ascending=False))
print("\nMean and median PM2.5 by Country (top 10 by record volume):")
print(agg)
agg.to_csv(os.path.join(FIG_DIR, "aggregation_pm25_by_country.csv"))

agg_plot = agg.reset_index().melt(id_vars="Country", value_vars=["mean", "median"],
                                   var_name="Statistic", value_name="PM2.5")
plt.figure(figsize=(11, 6))
sns.barplot(data=agg_plot, x="Country", y="PM2.5", hue="Statistic")
plt.title("Mean vs Median PM2.5 by Country")
plt.xlabel("Country")
plt.ylabel("PM2.5 Concentration")
plt.xticks(rotation=30, ha="right")
plt.legend(title="Statistic")
savefig("bar_agg_pm25_by_country.png")

# --- 4d. Temperature -> Air Quality Risk relationship (BMI -> risk analogue)
# Build a standard EPA-style PM2.5 risk category (like a "diabetes risk
# score"), then examine how it responds to Temperature (like "BMI"),
# analogous to the brief's "credit score range -> loan approval" /
# "BMI -> diabetes risk score" question.
# Breakpoints are the EPA's current 24-hour PM2.5 AQI breakpoints (in effect
# since the 6 May 2024 AQI revision, source: EPA AQS breakpoint table,
# https://aqs.epa.gov/aqsweb/documents/codetables/aqi_breakpoints.csv) --
# NOT the older pre-2024 breakpoints (which used 12/35.4/55.4/150.4/250.4)
# still widely quoted online.
def pm25_risk(value):
    if value <= 9.0:
        return "Good"
    elif value <= 35.4:
        return "Moderate"
    elif value <= 55.4:
        return "Unhealthy (Sensitive)"
    elif value <= 125.4:
        return "Unhealthy"
    elif value <= 225.4:
        return "Very Unhealthy"
    else:
        return "Hazardous"


risk_order = ["Good", "Moderate", "Unhealthy (Sensitive)", "Unhealthy",
              "Very Unhealthy", "Hazardous"]
df["AQ_Risk_Category"] = pd.Categorical(df["PM2.5"].apply(pm25_risk),
                                         categories=risk_order, ordered=True)
df["AQ_Risk_Score"] = df["AQ_Risk_Category"].cat.codes + 1  # 1 (Good) - 6 (Hazardous)

temp_bins = [-30, 0, 10, 20, 30, 50]
temp_labels = ["<0C", "0-10C", "10-20C", "20-30C", ">30C"]
df["Temperature_Band"] = pd.cut(df["Temperature"], bins=temp_bins, labels=temp_labels)

risk_by_temp = df.groupby("Temperature_Band", observed=True)["AQ_Risk_Score"].agg(
    ["mean", "std", "median"]).round(2)
print("\nAir Quality Risk Score by Temperature Band:")
print(risk_by_temp)
risk_by_temp.to_csv(os.path.join(FIG_DIR, "risk_score_by_temperature_band.csv"))

plt.figure(figsize=(9, 6))
sns.boxplot(data=df, x="Temperature_Band", y="AQ_Risk_Score", order=temp_labels,
            hue="Temperature_Band", palette="coolwarm", legend=False)
plt.title("Air Quality Risk Score by Temperature Band\n"
          "(1=Good ... 6=Hazardous)")
plt.xlabel("Temperature Band")
plt.ylabel("Air Quality Risk Score")
savefig("boxplot_risk_by_temperature.png")

print("\nAll figures and summary tables saved to the 'figures' folder.")
print("EDA pipeline complete.")

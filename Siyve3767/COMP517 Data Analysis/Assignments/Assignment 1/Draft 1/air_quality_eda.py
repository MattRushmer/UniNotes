# COMP517 Assignment 1 - Data Exploration and Analysis
# Dataset: Global Air Quality 2023 (messy version)
#
# This just runs through the EDA steps we covered in class:
#   1. load the data and have a look at it
#   2. clean it up (missing values, duplicates, outliers)
#   3. explore/visualise the clean data
#   4. look at a few relationships between variables
#
# Everything gets printed to the console (that's what the report is built
# from) and all the charts get saved into the "figures" folder as PNGs.
# Run it from inside this "Draft 1" folder with:  python air_quality_eda.py

import os

import matplotlib
matplotlib.use("Agg")  # don't try to pop up a window, just save the files
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set_theme(style="whitegrid")

DATA_PATH = os.path.join(
    "..", "Dataset - Global Air Quality 2023", "global_air_quality_data_messy.csv"
)
FIG_DIR = "figures"
os.makedirs(FIG_DIR, exist_ok=True)

# grouping these so I'm not retyping the same list of columns everywhere
POLLUTANTS = ["PM2.5", "PM10", "NO2", "SO2", "CO", "O3"]
WEATHER = ["Temperature", "Humidity", "Wind Speed"]
NUMERIC_COLS = POLLUTANTS + WEATHER


def savefig(name):
    # small helper so every plot gets saved the same way instead of
    # copy-pasting these three lines under every single chart
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

# --- 2a. Clean up City/Country text -----------------------------------------
# the "messy" dataset has stuff like "SYDNEY", " Sydney", "sydney " all as
# separate values, so strip the spaces and make the case consistent first
print("\nUnique City values before cleaning:", df["City"].nunique())
print("Unique Country values before cleaning:", df["Country"].nunique())

df["City"] = df["City"].str.strip().str.title()
df["Country"] = df["Country"].str.strip().str.title()

# .title() also wrecks acronyms like UAE/UK/USA (turns them into
# Uae/Uk/Usa), so fix those specific ones back up manually
ACRONYM_FIX = {"Uae": "UAE", "Uk": "UK", "Usa": "USA"}
df["Country"] = df["Country"].replace(ACRONYM_FIX)

print("Unique City values after cleaning:", df["City"].nunique())
print("Unique Country values after cleaning:", df["Country"].nunique())

# --- 2b. Parse the Date column ----------------------------------------------
# dates are in M/D/YYYY format (you can tell because some values like 10/27
# only make sense if the first number is the month)
df["Date"] = pd.to_datetime(df["Date"], format="%m/%d/%Y", errors="coerce")
print("\nRows where Date failed to parse:", df["Date"].isna().sum())


def month_to_quarter(month):
    # grouping months into calendar quarters instead of "Summer/Winter"
    # since the countries in this dataset are on both sides of the equator,
    # so a season name would be wrong for half of them
    if month in (12, 1, 2):
        return "Q1: Dec-Feb"
    elif month in (3, 4, 5):
        return "Q2: Mar-May"
    elif month in (6, 7, 8):
        return "Q3: Jun-Aug"
    else:
        return "Q4: Sep-Nov"


df["Quarter"] = df["Date"].dt.month.apply(month_to_quarter)

# --- 2c. Missing values ------------------------------------------------------
print("\n--- Handling missing values ---")
missing_before = df.isnull().sum()
print(missing_before[missing_before > 0])

# only the 6 pollutant columns have gaps, so just loop over NUMERIC_COLS and
# skip anything that's already complete
for col in NUMERIC_COLS:
    if df[col].isnull().sum() == 0:
        print(f"{col}: no missing values, skipped")
        continue
    skew = df[col].skew()
    print(f"{col}: skew={skew:.2f} -> using {'median' if abs(skew) > 0.5 else 'mean'}")

# filling with a country-level average instead of one overall average -
# otherwise every country ends up sharing the exact same filled-in number,
# which flattens out any real difference between countries
for col in NUMERIC_COLS:
    if df[col].isnull().sum() == 0:
        continue
    skew = df[col].skew()
    if abs(skew) > 0.5:
        method = "median"
        country_avg = df.groupby("Country")[col].median()
    else:
        method = "mean"
        country_avg = df.groupby("Country")[col].mean()
    df[col] = df[col].fillna(df["Country"].map(country_avg))
    df[col] = df[col].fillna(df[col].mean())  # just in case, shouldn't trigger
    print(f"  filled {col} missing values with per-Country {method}")

# City/Country themselves don't have gaps in this dataset, but check anyway
for col in ["City", "Country"]:
    if df[col].isnull().sum() > 0:
        mode_val = df[col].mode()[0]
        df[col] = df[col].fillna(mode_val)
        print(f"  filled {col} missing values with mode ({mode_val})")

# rows are in random order (not sorted by city/date), so there's no sensible
# neighbouring value to guess a missing date from - just drop those rows
if df["Date"].isnull().sum() > 0:
    before = df["Date"].isnull().sum()
    df = df.dropna(subset=["Date"])
    print(f"  dropped {before} rows with an unparseable Date")

print("\nMissing values after cleaning:")
print(df.isnull().sum())

# --- 2d. Duplicates -----------------------------------------------------------
print("\n--- Handling duplicates ---")
exact_dupes = df.duplicated().sum()
print(f"Exact duplicate rows (all columns identical): {exact_dupes}")

key_dupes = df.duplicated(subset=["City", "Country", "Date"]).sum()
print(f"Rows sharing the same City+Country+Date: {key_dupes}")

df = df.drop_duplicates()
print(f"Shape after dropping exact duplicates: {df.shape}")

# --- 2e. Outliers ---------------------------------------------------------------
# get rid of physically impossible readings first, before working out the
# outlier bounds below (otherwise the bounds and the plots wouldn't match)
before_rows = len(df)
df = df[(df["Humidity"] >= 0) & (df["Humidity"] <= 100)]
df = df[(df["Wind Speed"] >= 0)]
print(f"\nRemoved {before_rows - len(df)} rows with physically impossible "
      f"Humidity/Wind Speed values")

print("\n--- Handling outliers (IQR method) ---")
outlier_masks = {}
for col in NUMERIC_COLS:
    q1, q3 = df[col].quantile([0.25, 0.75])
    iqr = q3 - q1
    lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    mask = (df[col] < lower) | (df[col] > upper)
    outlier_masks[col] = mask
    print(f"{col}: {mask.sum()} outliers (bounds: {lower:.2f} to {upper:.2f})")

# double check PM2.5 with the z-score method too since it's the pollutant
# that matters most for health (from MATH503 - anything with |z| > 3)
z_scores = (df["PM2.5"] - df["PM2.5"].mean()) / df["PM2.5"].std()
print(f"\nPM2.5 z-score outliers (|z|>3): {(z_scores.abs() > 3).sum()}")

# both methods agree there aren't really any outliers here, so nothing gets
# removed on outlier grounds - a real pollution spike is exactly the kind of
# thing we'd want to keep, not throw away

# scatter plot of outlier vs non-outlier points, just for the two pollutants
# people usually care about most
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

# boxplots of all the pollutants together, another way to see spread/outliers
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

# histograms for every numeric column, one grid of subplots
fig, axes = plt.subplots(3, 3, figsize=(14, 10))
for ax, col in zip(axes.flat, NUMERIC_COLS):
    sns.histplot(df[col], kde=True, ax=ax, color="teal")
    ax.set_title(f"Distribution of {col}")
    ax.set_xlabel(col)
    ax.set_ylabel("Frequency")
for ax in axes.flat[len(NUMERIC_COLS):]:
    ax.axis("off")  # hides the last empty subplot (9 slots, only 9 cols so fine, but just in case)
savefig("histograms_numeric.png")

# bar chart - which countries have the most records
plt.figure(figsize=(10, 6))
top_countries = df["Country"].value_counts().head(10)
sns.barplot(x=top_countries.values, y=top_countries.index, hue=top_countries.index,
            palette="viridis", legend=False)
plt.title("Top 10 Countries by Number of Air Quality Records")
plt.xlabel("Number of Records")
plt.ylabel("Country")
savefig("bar_top_countries.png")

# pie chart - how records are split across the calendar quarters
plt.figure(figsize=(8, 6))
quarter_counts = df["Quarter"].value_counts().sort_index()
wedges, _, _ = plt.pie(quarter_counts.values, autopct="%1.1f%%", pctdistance=0.8,
                        colors=sns.color_palette("pastel"))
plt.title("Share of Records by Calendar Quarter")
plt.legend(wedges, quarter_counts.index, title="Quarter",
           loc="center left", bbox_to_anchor=(1.0, 0.5))
savefig("pie_quarter_share.png")

# boxplots for the weather variables
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

# quick loop through the matrix to pull out anything worth mentioning
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

# --- 4b. Categorical x categorical: record counts by Country and Quarter ---
# just seeing if some countries reported a lot more in certain quarters
top5_countries = df["Country"].value_counts().head(5).index
top5_df = df[df["Country"].isin(top5_countries)]
cross = top5_df.groupby(["Country", "Quarter"]).size().unstack(fill_value=0)
print("\nRecord counts, Country (top 5) x Quarter:")
print(cross)

plt.figure(figsize=(9, 5))
sns.heatmap(cross, annot=True, fmt="d", cmap="YlGnBu")
plt.title("Record Count by Country (Top 5) and Calendar Quarter")
plt.xlabel("Quarter")
plt.ylabel("Country")
savefig("heatmap_country_quarter_count.png")

# --- 4c. Aggregation: mean & median PM2.5 by Country (top 10 by volume) ---
top10_countries = df["Country"].value_counts().head(10).index
agg = (df[df["Country"].isin(top10_countries)]
       .groupby("Country")["PM2.5"].agg(["mean", "median"]).round(2)
       .sort_values("mean", ascending=False))
print("\nMean and median PM2.5 by Country (top 10 by record volume):")
print(agg)
agg.to_csv(os.path.join(FIG_DIR, "aggregation_pm25_by_country.csv"))

# pandas can plot mean/median as grouped bars straight off the dataframe,
# no need to reshape anything
plt.figure(figsize=(11, 6))
agg.plot(kind="bar", ax=plt.gca())
plt.title("Mean vs Median PM2.5 by Country")
plt.xlabel("Country")
plt.ylabel("PM2.5 Concentration")
plt.xticks(rotation=30, ha="right")
plt.legend(title="Statistic")
savefig("bar_agg_pm25_by_country.png")

# --- 4d. Does Temperature affect the Air Quality Risk score? ---
# turning PM2.5 into a risk category is basically the same idea as turning
# BMI into a diabetes risk category from the lecture examples. Breakpoints
# below are the EPA's current PM2.5 AQI breakpoints (updated May 2024 -
# double checked these against the EPA breakpoint table since a lot of
# pages online still show the older, pre-2024 numbers).


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


# turning the risk category into a 1-6 score just with a plain dictionary,
# so it can be averaged/plotted like a normal number
RISK_SCORE = {
    "Good": 1,
    "Moderate": 2,
    "Unhealthy (Sensitive)": 3,
    "Unhealthy": 4,
    "Very Unhealthy": 5,
    "Hazardous": 6,
}
df["AQ_Risk_Category"] = df["PM2.5"].apply(pm25_risk)
df["AQ_Risk_Score"] = df["AQ_Risk_Category"].map(RISK_SCORE)


def temperature_band(temp):
    # same idea as month_to_quarter above, just bucketing temperature
    # instead of bucketing months
    if temp <= 0:
        return "<0C"
    elif temp <= 10:
        return "0-10C"
    elif temp <= 20:
        return "10-20C"
    elif temp <= 30:
        return "20-30C"
    else:
        return ">30C"


df["Temperature_Band"] = df["Temperature"].apply(temperature_band)
temp_order = ["<0C", "0-10C", "10-20C", "20-30C", ">30C"]

risk_by_temp = df.groupby("Temperature_Band")["AQ_Risk_Score"].agg(
    ["mean", "std", "median"]).round(2).reindex(temp_order)
print("\nAir Quality Risk Score by Temperature Band:")
print(risk_by_temp)
risk_by_temp.to_csv(os.path.join(FIG_DIR, "risk_score_by_temperature_band.csv"))

plt.figure(figsize=(9, 6))
sns.boxplot(data=df, x="Temperature_Band", y="AQ_Risk_Score", order=temp_order,
            hue="Temperature_Band", palette="coolwarm", legend=False)
plt.title("Air Quality Risk Score by Temperature Band\n"
          "(1=Good ... 6=Hazardous)")
plt.xlabel("Temperature Band")
plt.ylabel("Air Quality Risk Score")
savefig("boxplot_risk_by_temperature.png")

print("\nAll figures and summary tables saved to the 'figures' folder.")
print("EDA pipeline complete.")

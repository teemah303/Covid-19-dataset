import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("CORD-19 Data Explorer")
st.write("Simple exploration of COVID-19 research papers")

# Load data (use smaller sample for performance)
df = pd.read_csv("metadata.csv", low_memory=False)
df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")
df["year"] = df["publish_time"].dt.year
df["journal"].fillna("Unknown", inplace=True)

# Interactive filter
years = st.slider("Select year range", 2018, 2023, (2019, 2021))
filtered = df[(df["year"] >= years[0]) & (df["year"] <= years[1])]

# Show sample
st.write(filtered.head())

# Plot publications per year
year_counts = filtered["year"].value_counts().sort_index()
fig, ax = plt.subplots()
ax.bar(year_counts.index, year_counts.values)
st.pyplot(fig)

# Top journals
top_journals = filtered["journal"].value_counts().head(10)
fig, ax = plt.subplots()
sns.barplot(x=top_journals.values, y=top_journals.index, ax=ax)
st.pyplot(fig)

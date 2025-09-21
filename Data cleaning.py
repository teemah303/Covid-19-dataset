df = df.dropna(subset=["publish_time", "title"])
df["journal"].fillna("Unknown", inplace=True)

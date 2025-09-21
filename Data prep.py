df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")
df["year"] = df["publish_time"].dt.year
df["abstract_word_count"] = df["abstract"].fillna("").apply(lambda x: len(x.split()))

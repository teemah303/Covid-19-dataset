import matplotlib.pyplot as plt
import seaborn as sns

# Publications by year
year_counts = df["year"].value_counts().sort_index()
plt.bar(year_counts.index, year_counts.values)
plt.title("Publications by Year")
plt.show()

# Top journals
top_journals = df["journal"].value_counts().head(10)
sns.barplot(x=top_journals.values, y=top_journals.index)
plt.title("Top 10 Journals")
plt.show()

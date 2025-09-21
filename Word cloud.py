from wordcloud import WordCloud

text = " ".join(df["title"].dropna().tolist())
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

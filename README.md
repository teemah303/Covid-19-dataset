CORD-19 Data Explorer

This project is a beginner-friendly data analysis and visualization assignment using the CORD-19 metadata dataset. It demonstrates fundamental data science workflows including data loading, cleaning, exploration, visualization, and deployment with Streamlit.

⸻

🚀 Project Overview

The project walks through:
	•	Loading and exploring the metadata.csv file from the CORD-19 dataset.
	•	Performing basic data cleaning (handling missing values, date conversion).
	•	Conducting simple data analysis (papers per year, top journals, word frequency).
	•	Creating visualizations with Matplotlib/Seaborn/WordCloud.
	•	Building a simple Streamlit application for interactive exploration.

⸻

📂 Dataset Information

We use the metadata.csv file from the CORD-19 Research Challenge.
This file contains metadata about research papers including:
	•	Paper titles and abstracts
	•	Publication dates
	•	Authors and journals
	•	Source information

⚠️ Note: The full dataset is large. For this assignment, we work with just the metadata file or a smaller sample.

⸻

🛠️ Tools & Requirements
	•	Python 3.7+
	•	pandas (data manipulation)
	•	matplotlib, seaborn (visualization)
	•	wordcloud (title frequency)
	•	streamlit (web application)
	•	Jupyter Notebook (optional, for exploration)
 Install dependencies:
 pip install pandas matplotlib seaborn streamlit wordcloud
 📌 Tasks Completed

🔹 Part 1: Data Loading & Exploration
	•	Loaded metadata.csv into a DataFrame
	•	Checked shape, data types, missing values, and statistics

🔹 Part 2: Data Cleaning & Preparation
	•	Removed rows with missing critical values (e.g., publish_time)
	•	Filled missing journals with "Unknown"
	•	Converted publish_time → datetime & extracted year
	•	Created new feature: abstract_word_count

🔹 Part 3: Analysis & Visualization
	•	Papers per year (trend over time)
	•	Top 10 journals publishing COVID-19 research
	•	Word frequency cloud of paper titles
	•	Distribution by source

🔹 Part 4: Streamlit Application

A simple interactive web app with:
	•	Year range filter (slider)
	•	Sample data viewer
	•	Bar chart of publications by year
	•	Top journals bar chart
 Run the app:
 streamlit run app.py📸 Example Outputs
	•	Publications by year (bar chart)
	•	Top 10 journals (horizontal bar chart)
	•	Word cloud of titles

(Add screenshots here after running your notebook/app)

⸻

📖 Reflections
	•	Challenges: Handling missing data and managing the dataset size.
	•	Learnings: Improved confidence in Pandas, basic visualization, and deploying Streamlit apps.
	•	Next steps: Expand analysis with NLP (abstract/topic modeling), add more interactive filters to Streamlit.
 📎 Repository Structure
 Frameworks_Assignment/
│
├── app.py              # Streamlit app
├── analysis.ipynb      # Jupyter Notebook for exploration
├── metadata.csv        # Dataset (or sample of it)
├── README.md           # Documentation
└── requirements.txt    # Dependencies
✨ Author

Developed as part of a Data Analysis & Streamlit assignment.
 

import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from preprocessing import clean_text

df = pd.read_csv("dataset/jobs.csv")

df["text"] = df["title"] + " " + df["description"] + " " + df["skills"]

df["text"] = df["text"].apply(clean_text)

X = df["text"]
y = df["label"]

model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", LogisticRegression())
])

model.fit(X, y)

joblib.dump(model, "model/fake_job_model.pkl")

print("Model trained successfully!")
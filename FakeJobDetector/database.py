import sqlite3

conn = sqlite3.connect("jobs.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS job_predictions(
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT,
company TEXT,
prediction TEXT
)
""")

conn.commit()

def save_prediction(title, company, result):
    cursor.execute(
        "INSERT INTO job_predictions(title,company,prediction) VALUES(?,?,?)",
        (title, company, result)
    )
    conn.commit()
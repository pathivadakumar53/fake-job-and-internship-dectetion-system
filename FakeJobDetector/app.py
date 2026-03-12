import streamlit as st
import joblib

# Load ML model
model = joblib.load("model/fake_job_model.pkl")

st.title("🔍 Fake Job & Internship Detection System")

st.write("Enter job details to check whether the job posting is **Fake or Real**.")

# Input fields
title = st.text_input("Job Title")
company = st.text_input("Company Name")
salary = st.text_input("Salary")
description = st.text_area("Job Description")
skills = st.text_input("Required Skills")

if st.button("Check Job"):

    # Check if required fields are empty
    if title == "" or description == "":
        st.warning("⚠ Please enter Job Title and Description")
    
    else:

        # Salary fraud detection
        if salary and salary.isdigit():
            if int(salary) > 200000:
                st.warning("⚠ Suspiciously high salary detected")

        # Combine text for ML model
        text = title + " " + company + " " + description + " " + skills

        # Prediction
        prediction = model.predict([text])[0]
        probability = model.predict_proba([text])

        confidence = max(probability[0]) * 100

        # Show result
        if prediction == 1:
            st.error("🚨 Fake Job Detected")
        else:
            st.success("✅ Real Job Posting")

        st.write(f"Confidence Score: **{confidence:.2f}%**")
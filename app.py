import streamlit as st
from model import load_dataset, build_symptom_disease_map, get_possible_diseases

# Load and prepare data
df = load_dataset()
symptom_map = build_symptom_disease_map(df)
all_symptoms = sorted(symptom_map.keys())

# App UI
st.set_page_config(page_title="AI Symptom Checker", layout="centered")
st.title("🤖 AI-Powered Symptom Checker")
st.markdown("Select your symptoms to find possible diseases.")

# Multi-select input
selected_symptoms = st.multiselect("🩺 Select Symptoms:", all_symptoms)

if st.button("🔍 Check Possible Diseases"):
    if not selected_symptoms:
        st.warning("Please select at least one symptom.")
    else:
        diseases = get_possible_diseases(selected_symptoms, symptom_map)
        if diseases:
            st.success("✅ Possible Diseases Found:")
            for dis in diseases:
                st.markdown(f"- {dis}")
        else:
            st.error("❌ No diseases found for the selected symptoms.")

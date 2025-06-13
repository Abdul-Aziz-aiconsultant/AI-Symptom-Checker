import pandas as pd

data = {
    "symptoms": [
        "fever", "fever", "fever", "headache", "headache", 
        "cough", "cough", "fatigue", "chest pain", "shortness of breath"
    ],
    "disease": [
        "Flu", "covid-19", "Malaria", "Migraine", "Brain Tumor", 
        "covid-19", "Tuberculosis", "Anemia", "Heart Attack", "Asthma"
    ]
}

df = pd.DataFrame(data)
df.to_csv("data/symptom_disease_dataset.csv", index=False)

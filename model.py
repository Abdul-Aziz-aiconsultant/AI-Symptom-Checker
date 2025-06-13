import pandas as pd

def load_dataset():
    return pd.read_csv("data/symptom_disease_dataset.csv")

def build_symptom_disease_map(df):
    symptom_map = {}
    for _, row in df.iterrows():
        disease = row['Disease']
        symptoms = row['Symptoms'].split(',')
        for symptom in symptoms:
            s = symptom.strip().lower()
            if s not in symptom_map:
                symptom_map[s] = set()
            symptom_map[s].add(disease)
    return symptom_map

def get_possible_diseases(user_symptoms, symptom_map):
    disease_counter = {}
    for symptom in user_symptoms:
        symptom = symptom.lower()
        if symptom in symptom_map:
            for disease in symptom_map[symptom]:
                disease_counter[disease] = disease_counter.get(disease, 0) + 1
    # Sort diseases by most matched symptoms
    sorted_diseases = sorted(disease_counter.items(), key=lambda x: x[1], reverse=True)
    return [d[0] for d in sorted_diseases]

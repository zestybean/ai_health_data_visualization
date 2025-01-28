import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from datetime import datetime

# Load the data
patients = pd.read_csv('data/mimic_data/PATIENTS.csv')

admissions = pd.read_csv('data/mimic_data/ADMISSIONS.csv')

diagnosis = pd.read_csv('data/mimic_data/DIAGNOSES_ICD.csv')

icu_stays = pd.read_csv('data/mimic_data/ICUSTAYS.csv')

diagnosis_labes = pd.read_csv('data/mimic_data/D_ICD_DIAGNOSES.csv')

df = patients

#Calculate the age of the patients function
def calculate_age(dob, dod):
    dob_date = datetime.strptime(dob, '%Y-%m-%d %H:%M:%S')
    dod_date = datetime.strptime(dod, '%Y-%m-%d %H:%M:%S')  
    age = (dod_date - dob_date).days // 365
    return age

df["age"] = df.apply(lambda row: calculate_age(row["dob"], row["dod"]), axis=1)

filtered_df = df[df['age'] < 130]

print(filtered_df["age"].describe())


# Plot the age distribution
plt.figure(figsize=(12, 6))

# Plot the age distribution
plt.subplot(1, 2, 1)

#Plot 1
sns.histplot(filtered_df["age"], bins=20, kde=True)
plt.title("Patients - Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")

#Plot 2
plt.subplot(1, 2, 2)
sns.violinplot(data=filtered_df, x='gender', y='age', inner='box')
plt.title("Gender Distribution within Age Bins")
plt.xlabel("Gender")
plt.ylabel("Age")

plt.tight_layout()
plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
patients = pd.read_csv('data/mimic_data/patients.csv')

admissions = pd.read_csv('data/mimic_data/admissions.csv')

diagnosis = pd.read_csv('data/mimic_data/diagnosis.csv')
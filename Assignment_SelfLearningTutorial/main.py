import pandas as pd
import numpy as np
import tensorflow as tf
import sklearn
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('../Assignment_MIMIC_SQL/database.db')

# Fetch ICU stays and mortality labels
query_icu = """
SELECT icu.SUBJECT_ID, icu.HADM_ID, icu.ICUSTAY_ID, 
       adm.ADMITTIME, adm.DEATHTIME, 
       CASE 
           WHEN adm.DEATHTIME IS NOT NULL AND adm.DEATHTIME <= icu.OUTTIME THEN 1 
           ELSE 0 
       END AS MORTALITY
FROM ICUSTAYS icu
JOIN ADMISSIONS adm ON icu.HADM_ID = adm.HADM_ID;
"""
icu_stays = pd.read_sql(query_icu, conn)

# Fetch vital signs
query_vitals = """
SELECT ce.SUBJECT_ID, ce.HADM_ID, ce.ICUSTAY_ID, 
       ce.ITEMID, ce.CHARTTIME, ce.VALUE
FROM CHARTEVENTS ce
WHERE ce.ITEMID IN (211, 220045, 220179, 220180, 220210, 220277, 223761)
AND ce.VALUE IS NOT NULL;
"""
vitals = pd.read_sql(query_vitals, conn)

# Fetch lab test results
query_labs = """
SELECT le.SUBJECT_ID, le.HADM_ID, 
       le.ITEMID, le.CHARTTIME, le.VALUE
FROM LABEVENTS le
WHERE le.ITEMID IN (50809, 50912, 51300)
AND le.VALUE IS NOT NULL;
"""
labs = pd.read_sql(query_labs, conn)

# Close the connection
conn.close()

# Display sample data
print("ICU Stays:\n", icu_stays.head())
print("Vitals:\n", vitals.head())
print("Labs:\n", labs.head())


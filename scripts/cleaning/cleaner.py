## Packages
import pandas as pd
import numpy as np

## Raw data
raw = pd.read_csv('data/raw/raw_diabetic_data.csv')
clean = pd.read_csv('data/clean_diabetic_data.csv')
raw.columns
df = raw

## Assembling the data dictionary
# print(clean['medical_specialty'].unique())  # ~  Utilized for obtaining all unique values for each column

## Race
race_dict = {'Caucasian': 1, 'AfricanAmerican': 2, 'Hispanic': 3, 'Asian': 4, 'Other': 5, '?': 0}
df['race'] = df['race'].map(race_dict)

## Gender
gender_dict = {'Unknown/Invalid': 0, 'Male': 1, 'Female': 2}
df['gender'] = df['gender'].map(gender_dict)

## Age
age_dict = {'[0-10)': 10, '[10-20)': 20, '[20-30)': 30, '[30-40)': 40, '[40-50)': 50, '[50-60)': 60, '[60-70)': 70, '[70-80)': 80, '[80-90)': 90, '[90-100)': 100}
df['age'] = df['age'].map(age_dict)

## Weight
df = df.drop(columns=['weight'])

## Payer code
df = df.drop(columns=['payer_code'])

## Medical specialty
med_spec_dict = {
    '?': 0,
    'Pediatrics-Endocrinology': 1,
    'InternalMedicine': 2,
    'Family/GeneralPractice': 3,
    'Cardiology': 4,
    'Surgery-General': 5,
    'Orthopedics': 6,
    'Gastroenterology': 7,
    'Surgery-Cardiovascular/Thoracic': 8,
    'Nephrology': 9,
    'Orthopedics-Reconstructive': 10,
    'Psychiatry': 11,
    'Emergency/Trauma': 12,
    'Pulmonology': 13,
    'Surgery-Neuro': 14,
    'Obsterics&Gynecology-GynecologicOnco': 15,
    'ObstetricsandGynecology': 16,
    'Pediatrics': 17,
    'Hematology/Oncology': 18,
    'Otolaryngology': 19,
    'Surgery-Colon&Rectal': 20,
    'Pediatrics-CriticalCare': 21,
    'Endocrinology': 22,
    'Urology': 23,
    'Psychiatry-Child/Adolescent': 24,
    'Pediatrics-Pulmonology': 25,
    'Neurology': 26,
    'Anesthesiology-Pediatric': 27,
    'Radiology': 28,
    'Pediatrics-Hematology-Oncology': 29,
    'Psychology': 30,
    'Podiatry': 31,
    'Gynecology': 32,
    'Oncology': 33,
    'Pediatrics-Neurology': 34,
    'Surgery-Plastic': 35,
    'Surgery-Thoracic': 36,
    'Surgery-PlasticwithinHeadandNeck': 37,
    'Ophthalmology': 38,
    'Surgery-Pediatric': 39,
    'Pediatrics-EmergencyMedicine': 40,
    'Rhumatology': 41,
    'AllergyandImmunology': 42,
    'Surgery-Maxillofacial': 43,
    'Pediatrics-InfectiousDiseases': 44,
    'Pediatrics-AllergyandImmunology': 45,
    'Dentistry': 46,
    'Surgeon': 47,
    'Surgery-Vascular': 48,
    'Osteopath': 49,
    'Psychiatry-Addictive': 50,
    'Surgery-Cardiovascular': 51,
    'PhysicianNotFound': 52,
    'Hematology': 53,
    'Proctology': 54,
    'Obstetrics': 55,
    'SurgicalSpecialty': 56,
    'Radiologist': 57,
    'Pathology': 58,
    'Dermatology': 59,
    'SportsMedicine': 60,
    'Speech': 61,
    'Hospitalist': 62,
    'OutreachServices': 63,
    'Cardiology-Pediatric': 64,
    'Perinatology': 65,
    'Neurophysiology': 66,
    'Endocrinology-Metabolism': 67,
    'DCPTEAM': 68,
    'Resident': 69,
}
df['medical_specialty'] = df['medical_specialty'].map(med_spec_dict)

## Serum phospholipid fatty acid composition levels
serum_dict = {'None': 0, 'Norm': 1, '>200': 2, '>300': 3}
df['max_glu_serum'] = df['max_glu_serum'].map(serum_dict)

## A1C
a1c_dict = {'None': 0, 'Norm': 1, '>7': 7, '>8': 8}
df['A1Cresult'] = df['A1Cresult'].map(a1c_dict)

## Metformin
metformin_dict = {'No': 0, 'Steady': 1, 'Up': 10, 'Down': 5}
df['metformin'] = df['metformin'].map(metformin_dict)

## Repaglinide
repaglinide_dict = {'No': 0, 'Steady': 1, 'Up': 10, 'Down': 5}
df['repaglinide'] = df['repaglinide'].map(repaglinide_dict)

## Nateglinide
nateglinide_dict = {'No': 0, 'Steady': 1, 'Up': 10, 'Down': 5}
df['nateglinide'] = df['nateglinide'].map(nateglinide_dict)

## Chlorpropamide
chlorpropamide_dict = {'No': 0, 'Steady': 1, 'Up': 10, 'Down': 5}
df['chlorpropamide'] = df['chlorpropamide'].map(chlorpropamide_dict)

## Glimepiride
glimepiride_dict = {'No': 0, 'Steady': 1, 'Up': 10, 'Down': 5}
df['glimepiride'] = df['glimepiride'].map(glimepiride_dict)

## Acetohexamide
acetohexamide_dict = {'No': 0, 'Steady': 1, 'Up': 10, 'Down': 5}
df['acetohexamide'] = df['acetohexamide'].map(acetohexamide_dict)

## Glipizide
glipizide_dict = {'No': 0, 'Steady': 1, 'Up': 10, 'Down': 5}
df['glipizide'] = df['glipizide'].map(glipizide_dict)

## Glyburide
glyburide_dict = {'No': 0, 'Steady': 1, 'Up': 10, 'Down': 5}
df['glyburide'] = df['glyburide'].map(glyburide_dict)

## Tolbutamide
tolbutamide_dict = {'No': 0, 'Steady': 1}
df['tolbutamide'] = df['tolbutamide'].map(tolbutamide_dict)

## Pioglitazone
pioglitazone_dict = {'No': 0, 'Steady': 1, 'Up': 10, 'Down': 5}
df['pioglitazone'] = df['pioglitazone'].map(pioglitazone_dict)

## Rosiglitazone
rosiglitazone_dict = {'No': 0, 'Steady': 1, 'Up': 10, 'Down': 5}
df['rosiglitazone'] = df['rosiglitazone'].map(rosiglitazone_dict)

## Acarbose
acarbose_dict = {'No': 0, 'Steady': 1, 'Up': 10, 'Down': 5}
df['acarbose'] = df['acarbose'].map(acarbose_dict)

## Miglitol
miglitol_dict = {'No': 0, 'Steady': 1, 'Up': 10, 'Down': 5}
df['miglitol'] = df['miglitol'].map(miglitol_dict)

## Troglitazone
troglitazone_dict = {'No': 0, 'Steady': 1}
df['troglitazone'] = df['troglitazone'].map(troglitazone_dict)

## Tolazamide
tolazamide_dict = {'No': 0, 'Steady': 1, 'Up': 10, 'Down': 5}
df['tolazamide'] = df['tolazamide'].map(tolazamide_dict)

## Examide
examide_dict = {'No': 0}
df['examide'] = df['examide'].map(examide_dict)

## Citoglipton
citoglipton_dict = {'No': 0}
df['citoglipton'] = df['citoglipton'].map(citoglipton_dict)

## Insulin
insulin_dict = {'No': 0, 'Steady': 1, 'Up': 10, 'Down': 5}
df['insulin'] = df['insulin'].map(insulin_dict)

## Glyburide-metformin
glyburide_metformin_dict = {'No': 0, 'Steady': 1, 'Up': 10, 'Down': 5}
df['glyburide-metformin'] = df['glyburide-metformin'].map(glyburide_metformin_dict)

## Glipizide-metformin
glipizide_metformin_dict = {'No': 0, 'Steady': 1}
df['glipizide-metformin'] = df['glipizide-metformin'].map(glipizide_metformin_dict)

## Glimepiride-pioglitazone
glimepiride_pioglitazone_dict = {'No': 0, 'Steady': 1}
df['glimepiride-pioglitazone'] = df['glimepiride-pioglitazone'].map(glimepiride_pioglitazone_dict)

## Metformin-rosiglitazone
metformin_rosiglitazone_dict = {'No': 0, 'Steady': 1}
df['metformin-rosiglitazone'] = df['metformin-rosiglitazone'].map(metformin_rosiglitazone_dict)

## Metformin-pioglitazone
metformin_pioglitazone_dict = {'No': 0, 'Steady': 1}
df['metformin-pioglitazone'] = df['metformin-pioglitazone'].map(metformin_pioglitazone_dict)

## Change
change_dict = {'No': 0, 'Ch': 1}
df['change'] = df['change'].map(change_dict)

## DiabetesMed
diabetesMed_dict = {'No': 0, 'Yes': 1}
df['diabetesMed'] = df['diabetesMed'].map(diabetesMed_dict)

## Readmitted
readmitted_dict = {'NO': 0, '>30': 0, '<30': 1}
df['readmitted'] = df['readmitted'].map(readmitted_dict)


## Saving the clean data
df.to_csv('data/clean_diabetic_data.csv')



## Removing NaN values from the cleaned set
clean['medical_specialty'] = clean['medical_specialty'].fillna(0)
clean.columns

## Dropping unknown column
clean = clean.drop(columns=['Unnamed: 0'])

## Resaving to CSV
clean.to_csv('data/clean_diabetic_data.csv')
## Packages
import pandas as pd
import numpy as np

## Raw data
raw = pd.read_csv('data/raw/raw_diabetic_data.csv')
raw.columns
# print(raw['medical_specialty'].unique())  ~  Utilized for obtaining all unique values for each column

#clean = 0

## Saving the clean data
#clean.to_csv('data/clean/clean_diabetic_data.csv')
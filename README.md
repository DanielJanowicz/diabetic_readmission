# Diabetic Readmission Rates (<30 days)
Utilize a dataset from the UCI Machine Learning Repository from 130 hospitals in the United States from 1999-2008 to explore the correlation between certain variables and the their relation to readmission of diabetic patients.

## Prerequisites: 
- [Python 3.10.9](https://www.python.org/downloads/) or later for Windows, MacOS & Linux
- [Anaconda Navigator](https://www.anaconda.com/) compatible with Python 3.9 or later.
- [Pip 21.3](https://pip.pypa.io/en/stable/) or later

## Packages: 
```python
    # Default packages
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt  # Graphs & plots
    import seaborn as sns   # Data visualizations
    import csv # Some extra functionalities for csv  files - reading it as a dictionary
    from lightgbm import LGBMClassifier # sklearn is for machine learning and statistical modeling including classification, regression, clustering and dimensionality reduction 

    from sklearn.model_selection import train_test_split, cross_validate   #break up dataset into train and test sets
    from sklearn.linear_model import LogisticRegression
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import cross_val_score
    from sklearn.preprocessing import StandardScaler, MinMaxScaler


    # Packages relating to missing data
    import missingno as msno
    import re    # This library is used to perform regex pattern matching

    # Required functions from sklearn
    from sklearn.linear_model import LogisticRegression, LinearRegression
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.svm import LinearSVC
    from sklearn.ensemble import GradientBoostingClassifier
    from catboost import CatBoostClassifier
    import xgboost as xgb
    from sklearn.metrics import roc_auc_score, accuracy_score, precision_score, recall_score, classification_report, make_scorer
    from sklearn.linear_model import SGDClassifier
    from sklearn.model_selection import GridSearchCV, RandomizedSearchCV, train_test_split
```

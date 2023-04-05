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

    from sklearn.model_selection import KFold,cross_val_score, RepeatedStratifiedKFold,StratifiedKFold
    from sklearn.impute import SimpleImputer
    from sklearn.pipeline import Pipeline
    from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
    from sklearn.preprocessing import OneHotEncoder,StandardScaler,PowerTransformer
    from sklearn.compose import ColumnTransformer
    from sklearn.pipeline import Pipeline
    from sklearn.impute import KNNImputer,SimpleImputer
    from sklearn.compose import make_column_transformer
    from imblearn.pipeline import make_pipeline
    from sklearn.svm import SVC
    from sklearn.impute import SimpleImputer
    from sklearn.dummy import DummyClassifier
    from imblearn.over_sampling import SMOTE
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.metrics import confusion_matrix, accuracy_score, balanced_accuracy_score,\
                                precision_score, recall_score, roc_auc_score,\
                                plot_confusion_matrix, classification_report, plot_roc_curve, f1_score

    import plotly 
    import plotly.express as px
    import plotly.graph_objs as go
    import plotly.offline as py
    from plotly.offline import iplot
    from plotly.subplots import make_subplots
    import plotly.figure_factory as ff

    import warnings
    warnings.filterwarnings("ignore")
```

# Diabetic Readmission Rates (<30 days)
Utilize a dataset from the UCI Machine Learning Repository from 130 hospitals in the United States from 1999-2008 to explore the correlation between certain variables and the their relation to readmission of diabetic patients.

## Prerequisites: 
- [Python 3.10.9](https://www.python.org/downloads/) or later for Windows, MacOS & Linux
- [Anaconda Navigator](https://www.anaconda.com/) compatible with Python 3.9 or later.
- [Pip 21.3](https://pip.pypa.io/en/stable/) or later

## Packages: 
```python
    import pandas as pd
    import numpy as np
    import strealit as st
    from sklearn.metrics import accuracy_score
    from sklearn.model_selection import train_test_split
    from supervised.automl import AutoML
    import datetime as dt
    import re
```

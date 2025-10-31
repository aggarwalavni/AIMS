import pandas as pd
import numpy as np

data = {'Age': [25, np.nan, 22, 28, np.nan, 30]}
df = pd.DataFrame(data)
age_values = []
for value in df['Age']:
    if not pd.isnull(value):   
        age_values.append(value)   

mean_age = sum(age_values) / len(age_values)

imputed_age = []

for value in df['Age']:
    if pd.isnull(value):
        imputed_age.append(mean_age)   
    else:
        imputed_age.append(value)      

df['Age'] = imputed_age

print("After Imputation dataframe:")
print(df)


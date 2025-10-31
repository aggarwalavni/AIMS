import pandas as pd

data = {'Fries': ['Small fries', 'Medium fries', 'Large fries', 'Extra large fries' 'Medium fries', 'Small fries']}
df = pd.DataFrame(data)
size_order = ['Small fries', 'Medium fries', 'Large fries','Extra large fries']

encoded_val = []
for val in df['Fries']:
    for i in range(len(size_order)):
        if val == size_order[i]:
            encoded_val.append(i)
            break

df['Encoded'] = encoded_val
print("After Manual Ordinal Encoding Dataframe:")
print(df)


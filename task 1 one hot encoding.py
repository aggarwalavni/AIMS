import pandas as pd

data = {'Colour': ['Red', 'Yellow', 'Blue', 'Green','Red','Yellow','Red']}
df = pd.DataFrame(data)

unique_val = list(df['Colour'].unique())

for val in unique_val:
    new_col = [] 
    new_col.append(val) 
    for clr in df['Colour']: 
        if clr == val:
            new_col.append(1)
        else:
            new_col.append(0)
    
    df[val] = new_col 

print("One Hot Encoded DataFrame:")
print(df)
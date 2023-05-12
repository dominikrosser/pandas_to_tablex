# create a dataframe with some multicolumns
import pandas as pd
import numpy as np
S = [ "Stone", "Wood" ]
data = {}
for s in zip(S):
    data[(s, 'Ix')] = np.array([0.0, 0.0, 0.0, 0.0])
    data[(s, 'VH')] = np.array([0.0, 0.0, 0.0, 0.0])
df = pd.DataFrame(data)
df.columns = pd.MultiIndex.from_tuples(df.columns, names=['Material', 'Measurement'])

# Convert it to tablex
import pandas_to_tablex as ptt
tablex_string = ptt.df_to_tablex(df, latex_file="example_outputs/tmp.tex", typst_file="example_outputs/output.typ")
print(tablex_string)
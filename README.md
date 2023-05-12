# pandas_to_tablex
Convert a (simple) pandas [https://pandas.pydata.org/] dataframe with multicolumns to a tablex typst [https://github.com/PgBiel/typst-tablex] table in python. Pandoc must be installed for this to work. This tool might be unstable.

The tool uses pandas.to_latex() to create a latex document. Then it calls pandoc to convert the document to typst, and then it does some post processing by replacing '#table' with '#tablex' and inserting the multicolumns with some regular expressions and search/replace.

# Installation
- Install pandoc [https://pandoc.org/installing.html]
- Copy the file pandas_to_tablex.py to next to your project or clone this repository.
- `pip install pandas`

# Usage
```python
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
```

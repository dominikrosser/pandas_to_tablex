import pandas as pd
import subprocess
import re
import os

def df_to_tablex(df, latex_file='temp.tex', typst_file='temp.typ'):
    # Save the DataFrame to a LaTeX file
    df.to_latex(latex_file)

    # Call pandoc to convert the LaTeX file to a typst file
    subprocess.run(['pandoc', latex_file, '-o', typst_file])

    # Read the typst content
    with open(typst_file, 'r') as file:
        content = file.read()

    # Post-process the content
    content = post_process_typst(content)

    # Write the processed content back to the typst file
    with open(typst_file, 'w') as file:
        file.write(content)

    # Clean up the temporary LaTeX file
    os.remove(latex_file)

    return content

def post_process_typst(content):
    # Insert import statement
    content = '#import "tablex.typ": tablex, colspanx, rowspanx\n' + content

    # Replace #table( with #tablex(
    content = content.replace("#table(", "#tablex(")

    # Replace sequences of cells that should be merged
    content = re.sub(r'\[\((.*?),\)\],\s+\[\]', r'colspanx(2)[\1], ()', content, flags=re.DOTALL)

    return content
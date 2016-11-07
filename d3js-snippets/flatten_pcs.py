"""
Flattens the list TSV of segment with pitch class vector in rows to a TSV
where each fow is an active pitch class.

The pitch class labels are symbolic names (eg. C-B).
"""

import pandas as pd

def flatten_pcs(input_file, output_file):
    df = pd.read_csv(input_file, sep='\t')
    pcs_cols = list(df.columns[-12:])

    df_flat = pd.DataFrame.from_records([
        (row['start'], row['end'], pc)
        for (i, row) in df.iterrows()
        for (pc, active) in zip(pcs_cols, row[pcs_cols])
        if active == 1], columns=['start', 'end', 'pc'])

    df_flat.to_csv(output_file, sep='\t', index=None)

if __name__ == '__main__':
    flatten_pcs(
        '02_-_The_Night_Before.lab.pcs.tsv',
        '02_-_The_Night_Before.lab.pcs.flat.tsv')

import pandas as pd
import ast
import glob
import re
import os


def parse_as_list(x):
    if isinstance(x, list):
        return x
    if isinstance(x, str):
        try:
            return ast.literal_eval(x)
        except Exception:
            return [x]
    return [x]


def expand_nested_lists(data):

    data = data.map(parse_as_list)
    expanded_rows = []

    for _, row in data.iterrows():
        lengths = [len(v) for v in row if isinstance(v, list)]
        max_len = max(lengths) if lengths else 1

        # create new rows
        for i in range(max_len):
            new_row = {}
            for col in data.columns:
                val = row[col]
                # if column is list and has ith element, take it; else reuse same value
                if isinstance(val, list) and len(val) > i:
                    new_row[col] = val[i]
                elif isinstance(val, list) and len(val) == 1:
                    new_row[col] = val[0]
                else:
                    new_row[col] = val
            expanded_rows.append(new_row)

    return pd.DataFrame(expanded_rows)


def clean_all_csv_files(input_path, output_path):
    files = glob.glob(input_path)
    for file in files:
        df = pd.read_csv(file)
        df = expand_nested_lists(df)
        match_id = re.search(r'[^\\\/]+(?=\_.)', file).group(0)
        df["match_id"] = match_id
        filename = os.path.basename(file)

        output_file = f'{output_path}/{filename}'
        df.to_csv(output_file, index=False)
        print(f"Saved: {output_file}")

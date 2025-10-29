import pandas as pd
import ast
import glob
import re

def ensure_list(x):
    if isinstance(x, list):
        return x
    if isinstance(x, str):
        try:
            return ast.literal_eval(x)
        except Exception:
            return [x]
    return [x]


def dynamic_explode(data):

    data = data.applymap(ensure_list)
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

path = 'matches/*.csv'
files = glob.glob(path)
for file in files:
    df = pd.read_csv(file)
    df = dynamic_explode(df)
    regex = r'[^\\\/]+(?=\_.)'
    matchId = re.search(regex, file).group(0)
    df["match_id"] = matchId
    df.to_csv(file, index=False)
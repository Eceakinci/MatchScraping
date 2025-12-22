import pandas as pd
import glob
from dotenv import load_dotenv
import os

load_dotenv()
OUTPUT_DIR_CLEAN = os.getenv("OUTPUT_DIR_CLEAN")

files = glob.glob(f"{OUTPUT_DIR_CLEAN}/*.csv")
dfs = []

for f in files:
    df = pd.read_csv(f)

    stat_type = f.split("_")[-1].replace(".csv", "")
    df["stat_type"] = stat_type

    dfs.append(df)

long_df = pd.concat(dfs, ignore_index=True)

long_df.to_csv("data/all_stats_long.csv", index=False)

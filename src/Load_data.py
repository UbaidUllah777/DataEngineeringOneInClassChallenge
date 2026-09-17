from pathlib import Path

import pandas as pd


def sales_data_collect():
    # Build a reliable path from this file so it works from any working directory.
    project_root = Path(__file__).resolve().parent.parent
    csv_path = project_root / "data" / "retail_sales_ontario_synthetic.csv"
    sales = pd.read_csv(csv_path, low_memory=False)
    return sales
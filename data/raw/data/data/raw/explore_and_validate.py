import os
import glob
import pandas as pd

# 1. Load and Inspect all 10 CSVs
csv_files = glob.glob("data/raw/*.csv")
print(f"Found {len(csv_files)} CSV files for processing.\n")

for file in csv_files:
    print("="*50)
    print(f"Dataset: {os.path.basename(file)}")
    print("="*50)
    
    df = pd.read_csv(file)
    
    print("\n--- Shape ---")
    print(df.shape)
    
    print("\n--- Data Types ---")
    print(df.dtypes)
    
    print("\n--- Head (Top 3 rows) ---")
    print(df.head(3))
    
    # Quick anomaly check
    print("\n--- Potential Anomalies ---")
    missing = df.isnull().sum().sum()
    duplicates = df.duplicated().sum()
    print(f"Missing Values: {missing}")
    print(f"Duplicate Rows: {duplicates}")
    print("\n")

# ---------------------------------------------------------
# Mock setup for demonstration (Replace with actual data loads)
# ---------------------------------------------------------
# Let's assume you have 'fund_master' and 'nav_history' loaded as DataFrames:
# fund_master = pd.read_csv('data/raw/fund_master.csv')
# nav_history = pd.read_csv('data/raw/nav_history.csv')

print("="*50)
print("FUND MASTER EXPLORATION & VALIDATION")
print("="*50)

try:
    # 2. Explore Fund Master (Uncomment when files are ready)
    # print("Unique Fund Houses:", fund_master['fund_house'].nunique())
    # print("Categories:", fund_master['category'].unique())
    # print("Sub-Categories:", fund_master['sub_category'].unique())
    # print("Risk Grades:", fund_master['risk_grade'].unique())
    
    # 3. Validate AMFI Codes
    # master_codes = set(fund_master['scheme_code'].unique())
    # history_codes = set(nav_history['scheme_code'].unique())
    
    # missing_in_history = master_codes - history_codes
    # if not missing_in_history:
    #     print("Validation Passed: Every code in fund_master exists in nav_history.")
    # else:
    #     print(f"Validation Failed: {len(missing_in_history)} codes are missing from nav_history.")
    pass
except KeyError as e:
    print(f"Column missing during exploration: {e}")

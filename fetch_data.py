import os
import json
import requests
import pandas as pd
from datetime import datetime

# Ensure directories exist
os.makedirs('data/raw', exist_ok=True)

def fetch_and_save_nav(scheme_code, filename):
    url = f"https://api.mfapi.in/mf/{scheme_code}"
    print(f"Fetching data for scheme: {scheme_code}...")
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        # Save raw JSON response
        raw_path = f"data/raw/{filename}.json"
        with open(raw_path, 'w') as f:
            json.dump(data, f, indent=4)
            
        # Parse and save as raw CSV
        if 'data' in data and len(data['data']) > 0:
            df = pd.DataFrame(data['data'])
            df['scheme_code'] = scheme_code
            df['scheme_name'] = data['meta']['scheme_name']
            
            csv_path = f"data/raw/{filename}.csv"
            df.to_csv(csv_path, index=False)
            print(f"Successfully saved {csv_path}")
        else:
            print(f"No NAV data found for {scheme_code}")
            
    except Exception as e:
        print(f"Error fetching {scheme_code}: {e}")

# 1. Fetch HDFC Top 100 Direct (125497)
fetch_and_save_nav(125497, "hdfc_top_100_direct")

# 2. Fetch 5 key Bluechip schemes
bluechip_schemes = {
    119551: "sbi_bluechip",
    120503: "icici_bluechip",
    118632: "nippon_large_cap",
    119092: "axis_bluechip",
    120841: "kotak_bluechip"
}

for code, name in bluechip_schemes.items():
    fetch_and_save_nav(code, f"nav_{name}")

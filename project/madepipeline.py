import os
import pandas as pd
import sqlite3
from urllib.request import urlopen
import io


data_urls = [
    "https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.csv",
    "https://github.com/owid/co2-data/raw/master/owid-co2-data.csv"
]


data_dir = "../hamza-made/data"

# Ensure the data directory exists
os.makedirs(data_dir, exist_ok=True)

def download_data(url, header='infer', skiprows=None):
    try:
        response = urlopen(url)
        data = response.read().decode('utf-8')
        df = pd.read_csv(io.StringIO(data), header=header, skiprows=skiprows)
        print(f"Downloaded data from {url}:")
        return df
    except Exception as e:
        print(f"Error downloading data from {url}: {e}")
        return pd.DataFrame()
    
def delete_rows_before_year(df, year):
    try:
        df['year'] = pd.to_numeric(df['year'], errors='coerce')
        df = df[df['year'] >= year].reset_index(drop=True)
        return df
    except Exception as e:
        print(f"Error filtering data by year: {e}")
        return df
    
def first_url_delete_rows_before_year(df, year):
    try:
        df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
        df = df[df['Year'] >= year].reset_index(drop=True)
        return df
    except Exception as e:
        print(f"Error filtering data by year: {e}")
        return df
    
def drop_columns(df, columns_to_drop):
    try:
        df.drop(columns=columns_to_drop, inplace=True)
        return df
    except Exception as e:
        print(f"Error dropping columns: {e}")
        return df
    
def keep_columns(df, columns_to_keep):
    try:
        df = df[columns_to_keep]
        return df
    except Exception as e:
        print(f"Error keeping columns: {e}")
        return df

  
def save_to_sqlite(df, climate_change, climate):
    try:
        db_path = os.path.join(data_dir, climate_change)
        conn = sqlite3.connect(db_path)
        df.to_sql(climate, conn, if_exists='replace', index=False)
        conn.close()
    except Exception as e:
        print(f"Error saving data to SQLite: {e}")

def main():
     drop_columns_first_url= ['D-N', 'DJF', 'MAM', 'JJA', 'SON']
     keep_columns_second_url= ['country', 'year', 'cement_co2', 'co2', 'co2_growth_prct', 'coal_co2', 'gas_co2','oil_co2', 'share_global_co2']
     for i, url in enumerate(data_urls):
        if i == 0:
            # Skip the first row and use the second row as the header for the first URL
            df = download_data(url, header=1)
            df = first_url_delete_rows_before_year(df, 1950)
            df= drop_columns(df, drop_columns_first_url)
            print(df.head())
            
        else:
           df = download_data(url)
           if not df.empty and 'year' in df.columns:
                df = delete_rows_before_year(df, 1950)
                df= keep_columns(df, keep_columns_second_url)
                print(df.head())
        if not df.empty:
            save_to_sqlite(df, f"dataset{i+1}.db", "climate")
            
if __name__ == "__main__":
    main()

import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv('/home/ubuntu/pipeline/.env')

engine = create_engine(
    f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)

org_mapping = {
    'Business Entity Type 3': 'Business', 'Business Entity Type 2': 'Business', 'Business Entity Type 1': 'Business',
    'Government': 'Public', 'School': 'Public', 'Medicine': 'Public', 'Kindergarten': 'Public',
    'University': 'Public', 'Police': 'Public', 'Military': 'Public', 'Security Ministries': 'Public', 'Emergency': 'Public',
    'Self-employed': 'Self-employed',
    'Trade: type 7': 'Trade_Services', 'Trade: type 2': 'Trade_Services', 'Trade: type 3': 'Trade_Services',
    'Trade: type 6': 'Trade_Services', 'Trade: type 1': 'Trade_Services', 'Trade: type 5': 'Trade_Services', 'Trade: type 4': 'Trade_Services',
    'Services': 'Trade_Services', 'Hotel': 'Trade_Services', 'Restaurant': 'Trade_Services', 'Bank': 'Trade_Services',
    'Insurance': 'Trade_Services', 'Culture': 'Trade_Services', 'Legal Services': 'Trade_Services', 'Advertising': 'Trade_Services',
    'Postal': 'Trade_Services', 'Mobile': 'Trade_Services', 'Telecom': 'Trade_Services', 'Cleaning': 'Trade_Services', 'Realtor': 'Trade_Services',
    'Industry: type 11': 'Industry_Construction', 'Industry: type 1': 'Industry_Construction', 'Industry: type 4': 'Industry_Construction',
    'Industry: type 7': 'Industry_Construction', 'Industry: type 3': 'Industry_Construction', 'Industry: type 9': 'Industry_Construction',
    'Industry: type 2': 'Industry_Construction', 'Industry: type 12': 'Industry_Construction', 'Industry: type 5': 'Industry_Construction',
    'Industry: type 10': 'Industry_Construction', 'Industry: type 13': 'Industry_Construction', 'Industry: type 8': 'Industry_Construction',
    'Industry: type 6': 'Industry_Construction', 'Construction': 'Industry_Construction', 'Housing': 'Industry_Construction',
    'Agriculture': 'Industry_Construction', 'Electricity': 'Industry_Construction',
    'Transport: type 2': 'Transport', 'Transport: type 4': 'Transport', 'Transport: type 3': 'Transport', 'Transport: type 1': 'Transport',
    'Security': 'Other', 'Other': 'Other', 'XNA': 'Other', 'Religion': 'Other'
}

print("Starting ETL pipeline - cleaning stage...")
chunksize = 2000
first = True

for i, chunk in enumerate(pd.read_csv('/home/ubuntu/data/application_train.csv', chunksize=chunksize, low_memory=False)):
    # Handle outliers in DAYS_EMPLOYED
    chunk = chunk.copy()
    chunk['DAYS_EMPLOYED'] = chunk['DAYS_EMPLOYED'].replace(365243, np.nan)

    # Convert days to years
    chunk['YEARS_BIRTH'] = abs(chunk['DAYS_BIRTH']) / 365
    chunk['YEARS_EMPLOYED'] = abs(chunk['DAYS_EMPLOYED']) / 365

    # Fill missing numerical values with median
    num_cols = chunk.select_dtypes(include=['number']).columns
    chunk[num_cols] = chunk[num_cols].fillna(chunk[num_cols].median())

    # Fill missing categorical values with Unknown
    cat_cols = chunk.select_dtypes(include=['object']).columns
    chunk[cat_cols] = chunk[cat_cols].fillna('Unknown')

    # Map organization types to broader categories
    chunk['ORGANIZATION_TYPE'] = chunk['ORGANIZATION_TYPE'].map(org_mapping).fillna('Other')

    # Write to PostgreSQL
    chunk.to_sql('app_train_clean', engine, if_exists='replace' if first else 'append', index=False)
    first = False
    print(f"Chunk {i+1} processed and loaded")

print("Cleaning stage complete!")

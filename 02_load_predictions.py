import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv('/home/ubuntu/pipeline/.env')

engine = create_engine(
    f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)

print("Loading predictions...")
chunksize = 10000
first = True

for i, chunk in enumerate(pd.read_csv('/home/ubuntu/data/predictions.csv', chunksize=chunksize)):
    chunk.to_sql('predictions', engine, if_exists='replace' if first else 'append', index=False)
    first = False
    print(f"Chunk {i+1} loaded")

print("Done!")

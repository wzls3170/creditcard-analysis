import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

engine = create_engine(
    f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)

print("开始分批写入...")
chunksize = 10000
first_chunk = True

for i, chunk in enumerate(pd.read_csv('/home/ubuntu/data/application_train.csv', chunksize=chunksize)):
    chunk.columns = chunk.columns.str.lower()
    chunk = chunk.dropna(subset=['target'])
    if first_chunk:
        chunk.to_sql('application_train', engine, if_exists='replace', index=False)
        first_chunk = False
    else:
        chunk.to_sql('application_train', engine, if_exists='append', index=False)
    print(f"已写入第 {i+1} 批")

print("完成!")

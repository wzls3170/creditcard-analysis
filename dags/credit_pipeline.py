from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'credit_risk_pipeline',
    default_args=default_args,
    description='Credit risk scoring pipeline',
    schedule_interval='0 1 * * *',
    start_date=datetime(2026, 1, 1),
    catchup=False,
) as dag:

    clean_data = BashOperator(
        task_id='clean_data',
        bash_command='''docker run --rm \
            --network host \
            -e DB_HOST=localhost \
            -e DB_PORT=5432 \
            -e DB_NAME=homecredit \
            -e DB_USER=pipeline_user \
            -e DB_PASSWORD=pipeline123 \
            -v /home/ubuntu/data:/home/ubuntu/data \
            credit-pipeline python 01_clean.py''',
    )

    load_predictions = BashOperator(
        task_id='load_predictions',
        bash_command='''docker run --rm \
            --network host \
            -e DB_HOST=localhost \
            -e DB_PORT=5432 \
            -e DB_NAME=homecredit \
            -e DB_USER=pipeline_user \
            -e DB_PASSWORD=pipeline123 \
            -v /home/ubuntu/data:/home/ubuntu/data \
            credit-pipeline python 02_load_predictions.py''',
    )

    clean_data >> load_predictions

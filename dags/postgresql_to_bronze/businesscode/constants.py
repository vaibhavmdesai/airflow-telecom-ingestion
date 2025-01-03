from datetime import datetime
import csv

postgres_conn_id = 'telecom_postgres' 
aws_conn_id='minio_connection'
s3_bucket = 'oabronze'
config_path = '/home/vd/data-engineering/projects/Telecom/telecom-env/code/configs/config.csv'
archive_date = datetime.today().strftime('%Y/%m/%d')
archive_suffix = datetime.today().strftime('%Y%m%d%H%M%S')

with open(config_path, newline='') as csvfile:
    csvreader = csv.DictReader(csvfile)
    table_list = [row for row in csvreader if row['is_active'] == 'Y']
import boto3
import os
import time
from datetime import datetime
import redis
import json

cluster_name = os.environ["CLUSTER_NAME"]
dest_bucket = os.environ["DEST_BUCKET"]
env_name = os.environ["ENV"]
aws_region = os.environ["AWS_REGION"]
redis_endpoint = os.environ["REDIS_ENDPOINT"]
redis_port = int(os.environ["REDIS_PORT"])

start_time = datetime.now()
backup_time = start_time.strftime("%Y-%m-%d-%H-%M-%S")

elasticache = boto3.client('elasticache', region_name=aws_region)
s3 = boto3.client('s3', region_name=aws_region)

backup_name = f'{env_name}-{cluster_name}-{backup_time}'

print(f'Backing up {cluster_name} to backup named {backup_name}')

response = elasticache.create_snapshot(
    CacheClusterId=cluster_name,
    SnapshotName=backup_name
)

while True:
    time.sleep(10)
    response = elasticache.describe_snapshots(
        SnapshotName=backup_name,
        ShowNodeGroupConfig=False
    )
    status = response['Snapshots'][0]['SnapshotStatus']
    print(f'{backup_name} is {status}')
    if status == "available":
        break

r = redis.Redis(host=redis_endpoint, port=redis_port, decode_responses=True)

data = {}
keys = r.keys('*')
for key in keys:
    data[key] = r.get(key)

json_data = json.dumps(data, indent=2)

s3_key = f'{env_name}/{backup_name}.json'
s3.put_object(Bucket=dest_bucket, Key=s3_key, Body=json_data)

time_to_complete = datetime.now() - start_time
print(f'{backup_name} was exported to s3://{dest_bucket}/{s3_key} in {time_to_complete}')

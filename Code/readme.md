
# Redis Snapshot Export to S3

This script backs up an AWS ElastiCache Redis cluster to an S3 bucket in JSON format. The process includes creating a snapshot of the Redis cluster, restoring the snapshot, exporting Redis data as JSON, and uploading it to S3.

## Prerequisites

- AWS CLI configured with access to ElastiCache and S3
- Redis Python client (`redis-py`) installed
- Boto3 Python SDK installed

## Environment Variables

Set the following environment variables before running the script:

- `CLUSTER_NAME`: Name of the ElastiCache Redis cluster
- `DEST_BUCKET`: Name of the S3 bucket to upload the JSON file
- `ENV`: Environment name (used in backup name)
- `AWS_REGION`: AWS region where the resources are located
- `REDIS_ENDPOINT`: Endpoint of the Redis instance to connect to
- `REDIS_PORT`: Port of the Redis instance (typically `6379`)

## Installation

1. Install required Python packages:

    
    pip install boto3 redis
    

2. Set the environment variables (replace with your values):

    
    export CLUSTER_NAME='your-cluster-name'
    export DEST_BUCKET='your-bucket-name'
    export ENV='your-environment'
    export AWS_REGION='your-region'
    export REDIS_ENDPOINT='your-redis-endpoint'
    export REDIS_PORT='your-redis-port'
    

## Usage

Run the script with Python:


python exporter.py


## Script Details

1. Create Snapshot: Initiates a snapshot of the specified ElastiCache Redis cluster.
2. Wait for Snapshot: Polls until the snapshot status is `available`.
3. Connect to Redis: Connects to the Redis instance using the provided endpoint and port.
4. Export Data: Retrieves all data from Redis and converts it to JSON format.
5. Upload to S3: Uploads the JSON data to the specified S3 bucket.

## Notes

- Ensure that the Redis instance is accessible from the machine where the script runs.
- The script assumes that all Redis keys and values are serializable to JSON. Adjust the script if necessary to handle special cases or large datasets.

import boto3

# Create an S3 client
s3 = boto3.client('s3')

# List all S3 buckets
response = s3.list_buckets()

# Get a list of bucket names
bucket_list = [bucket['Name'] for bucket in response['Buckets']]

# Print the list of buckets
print(bucket_list)

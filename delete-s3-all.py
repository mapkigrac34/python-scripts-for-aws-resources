import boto3
import sys

# Create an S3 client
s3 = boto3.client('s3')

# List all S3 buckets
response = s3.list_buckets()

# Get a list of bucket names
bucket_list = [bucket['Name'] for bucket in response['Buckets']]

# Check if the script should delete the bucket contents
delete_contents = input("Do you want to delete the bucket contents? (yes/no) ")

# Iterate through the list of buckets
for bucket_name in bucket_list:
    try:
        # Delete the bucket
        if delete_contents.lower() == "yes":
            # Delete the bucket and its contents
            s3.delete_bucket(Bucket=bucket_name, 
                             Bucket=bucket_name)
            print(f'Bucket {bucket_name} and its contents deleted.')
        else:
            # Delete the bucket but not its contents
            s3.delete_bucket(Bucket=bucket_name)
            print(f'Bucket {bucket_name} deleted.')
    except Exception as e:
        # Handle any errors that may occur when attempting to delete the bucket
        print(e)

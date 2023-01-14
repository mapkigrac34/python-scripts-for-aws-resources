import boto3

# Create an S3 client
s3 = boto3.client('s3')

# Define the names of the buckets you want to create
bucket_names = ['sheymengla-my-bucket-1', 'sheymengla-my-bucket-2', 'sheymengla-my-bucket-3']

# Create the buckets
for bucket_name in bucket_names:
    try:
        s3.create_bucket(Bucket=bucket_name)
        print(f'Bucket {bucket_name} created.')
    except Exception as e:
        # Handle any errors that may occur when attempting to create the bucket
        print(e)

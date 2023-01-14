import boto3

# Create an S3 client
s3 = boto3.client('s3')

# Define the names of the buckets you want to create
bucket_names = ['shey-my-bucket-1a', 'shey-my-bucket-12', 'shey-my-bucket-13']

# Create the buckets
for bucket_name in bucket_names:
    try:
        #create the bucket
        s3.create_bucket(Bucket=bucket_name)
        print(f'Bucket {bucket_name} created.')
        #enable versioning
        s3.put_bucket_versioning(Bucket=bucket_name, VersioningConfiguration={'Status': 'Enabled'})
        print(f'Versioning enabled for bucket {bucket_name}')
        # block public access
        s3.put_public_access_block(
            Bucket=bucket_name,
            PublicAccessBlockConfiguration={
                'BlockPublicAcls': True,
                'IgnorePublicAcls': True,
                'BlockPublicPolicy': True,
                'RestrictPublicBuckets': True
            }
        )
        print(f'Public access blocked for bucket {bucket_name}')
    except Exception as e:
        # Handle any errors that may occur when attempting to create the bucket
        print(e)

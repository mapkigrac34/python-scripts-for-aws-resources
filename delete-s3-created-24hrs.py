import boto3
import datetime

# Create an S3 client
s3 = boto3.client('s3')

# Get the current time
now = datetime.datetime.now()

# Get a list of all S3 buckets
response = s3.list_buckets()
buckets = response['Buckets']

# Iterate through the list of buckets
for bucket in buckets:
    # Get the creation date of the bucket
    creation_date = bucket['CreationDate']

    # Convert the creation date to a datetime object
    creation_datetime = datetime.datetime.strptime(creation_date, '%Y-%m-%dT%H:%M:%S.%fZ')

    # Calculate the time elapsed since the bucket was created
    time_elapsed = now - creation_datetime

    # Check if the bucket was created within the last 24 hours
    if time_elapsed.days == 0 and time_elapsed.seconds / 3600 < 24:
        # Delete the bucket
        try:
            s3.delete_bucket(Bucket=bucket['Name'])
            print(f'Bucket {bucket["Name"]} deleted.')
        except Exception as e:
            # Handle any errors that may occur when attempting to delete the bucket
            print(e)


import boto3

def lambda_handler(event, context):
    # Replace with the name of the bucket you want to delete
    bucket_name = 'my-bucket'

    # Create an S3 client
    s3 = boto3.client('s3')

    # Delete all objects in the bucket
    try:
        result = s3.list_objects(Bucket=bucket_name)
        for obj in result.get('Contents', []):
            s3.delete_object(Bucket=bucket_name, Key=obj['Key'])
    except Exception as e:
        # Handle any errors that may occur when attempting to delete the objects
        print(e)
        return e

    # Delete the bucket
    try:
        s3.delete_bucket(Bucket=bucket_name)
        print(f'Bucket {bucket_name} deleted.')
    except Exception as e:
        # Handle any errors that may occur when attempting to delete the bucket
        print(e)
        return e

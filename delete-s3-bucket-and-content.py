# You can use the boto3 library in Python to delete an S3 bucket and its contents. 
# First, you'll need to import the library and create a client for the S3 service:

import boto3

s3 = boto3.client('s3')

# Next, you'll need to use the list_objects_v2 method to get a list of the objects in the bucket, 
# and then use the delete_objects method to delete them. Here's an example of how you can do this:

bucket_name = 'elasticbeanstalk-us-east-1-812714054388'

# Get a list of the objects in the bucket
response = s3.list_objects_v2(Bucket=bucket_name)

# Collect all the object keys from the response
objects = []
for content in response.get('Contents', []):
    objects.append({'Key': content['Key']})

# Delete the objects
s3.delete_objects(Bucket=bucket_name, Delete={'Objects': objects})

# Finally, you can use the delete_bucket method to delete the bucket itself:
s3.delete_bucket(Bucket=bucket_name)

# It's worth noting that if you want to delete all versions of an object, you need to enable versioning on the bucket first, 
# and after that you can get the objects of different version and then delete all the version accordingly. 
#Also, you need to make sure that all the objects are deleted and no object is locked otherwise it will not allow you to delete the bucket.

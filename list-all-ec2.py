import boto3

# Create an EC2 client
ec2 = boto3.client('ec2')

# List all EC2 instances
response = ec2.describe_instances()

# Get a list of instances
instances = response['Reservations']

# Print the list of instances
for instance in instances:
    for i in instance['Instances']:
        print(i['InstanceId'])

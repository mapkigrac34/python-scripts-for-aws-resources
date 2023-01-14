# You can use the boto3 library in Python to interact with the AWS EC2 service and list information about instances, including their instance type, AMI ID, and public IP address.
# First, you'll need to import the library and create a client for the EC2 service

import boto3

ec2 = boto3.client('ec2')

# Then, you can use the describe_instances method to get information about all of the instances in your account, and iterate through the response to extract the information you're interested in.
# Here's an example of how you can do this:

response = ec2.describe_instances()
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        # Extract the instance information
        instance_type = instance["InstanceType"]
        ami_id = instance["ImageId"]
        public_ip = instance.get("PublicIpAddress")
        print("Instance Type: ",instance_type)
        print("AMI Id: ",ami_id)
        if public_ip:
            print("Public IP: ", public_ip)
        else:
            print("Public IP not assigned")

# You can use the filters argument in the describe_instances method to filter the instances based on your requirements.
# You can also filter by tag, region or Vpc.
describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']},{'Name': 'tag:Name','Values':['my_instances']}])

# You can also filter instances by there states,
instances = ec2.describe_instances(Filters=[{'Name': 'instance-state-name','Values':['running','stopped']}])

# This will give you the list of all running and stopped instances


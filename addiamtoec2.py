import boto3
import re

ec2 = boto3.resource('ec2')
client = boto3.client('ec2')
List=[]

for instance in ec2.instances.filter(Filters=[{'Name': 'tag:EXAMPLE', 'Values': ['EXAMPLE']}]):
    id = str(instance)
    id = re.sub('ec2.Instance\(id=\'', '', id)
    id = re.sub('\'\)', '', id)
    List.append(id)

for all in List:
    response = client.associate_iam_instance_profile(
        IamInstanceProfile={
            'Arn': 'arn:aws:iam::ID_HERE',
            'Name': 'NAME_HERE'
        },
        InstanceId=all
    )
    print(all)

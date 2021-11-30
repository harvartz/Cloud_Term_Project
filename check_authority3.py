import boto3

session = boto3.Session(
        aws_access_key_id = 'AKIAX6G2G4WHPRRNDCH2',
        aws_secret_access_key = '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',
        region_name = 'us-east-2'
        )

ec2_client = session.client('ec2')
ec2_resource = session.resource('ec2')

print(ec2_client)
print(ec2_resource)

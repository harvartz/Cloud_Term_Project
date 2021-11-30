import boto3

ec2_client = boto3.client(
        'ec2',
        aws_access_key_id = 'AKIAX6G2G4WHPRRNDCH2',
        aws_secret_access_key = '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',
        region_name = 'us-east-2'
        )
response = ec2_client.list_buckets()
print(response)


import boto3

ec2_resource = boto3.resource(
        'ec2',
        aws_access_key_id = 'AKIAX6G2G4WHPRRNDCH2',
        aws_secret_access_key = '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',
        region_name = 'us-east-2'
        )

instance = ec2_resource.Instance('i-02f0e133212865e7b')

print('Instance ID : ', instance.instance_id)
print('Instancetags : ', instance.tags)

import boto3

session = boto3.Session()
print("session.profile_name:", session.profile_name)

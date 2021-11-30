import boto3

client = boto3.client('ec2')
ec2 = boto3.resource('ec2')
instance = ec2.Instance('id')

instance_list = instance.instance_id( )

### Instance list

def instance:
    print('Instance :')
    for instance in ec2.instance.all:
        print(instance. 




### Template


print('                                                  ')
print('                                                  ')
print('--------------------------------------------------')
print('      Amazon AWS Control Panel using SDK          ')
print('                                                  ')
print(' Cloud Computing, Computer Science Department     ')
print('                  at Chungbuk National University ')
print('--------------------------------------------------')
print('                                                  ')
print(' 1. list instance            2. available zones   ')
print(' 3. start instance           4. available regions ')
print(' 5. stop instance            6. create instance   ')
print(' 7. reboot instance          8. list images       ')
print('                            99. quit              ')
print('                                                  ')
print('--------------------------------------------------')

print("Enter an integer: ")

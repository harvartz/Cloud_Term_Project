import boto3

client = boto3.client('ec2')
ec2 = boto3.resource('ec2')
instance = ec2.Instance('id')


### 1. Instance list
def list_Instances():
    for instance in ec2.instances.all():
        print(
            "Id: {0}\nPlatform: {1}\nType: {2}\nPublic IPv4: {3}\nAMI: {4}\nState: {5}\n".format(
            instance.id, instance.platform, instance.instance_type, instance.public_ip_address, instance.image.id, instance.state
             )
            )


### 2. available zones
def avail_zone():
    for instance in ec2.instances.all():

while True:

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


    number = int(input("Enter an ingeger: "))

    if number == 1:
        list_Instances()
    elif number == 99:
        print('\n')
        print('Thank you')
        print('\n')
        break
    

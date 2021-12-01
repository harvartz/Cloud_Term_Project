import boto3

### Create Object
client = boto3.client('ec2')
ec2 = boto3.resource('ec2')
instance = ec2.Instance('id')


### 1. Instance list
def list_Instances():

    print('\n')
    print('1. list instance\n')
    print('DESC : Show your instances\n\n')
    for instance in ec2.instances.all():
        print(
            "Id: {0}\nPlatform: {1}\nType: {2}\nPublic IPv4: {3}\nAMI: {4}\nState: {5}\n".format(
            instance.id, instance.platform, instance.instance_type, instance.public_ip_address, instance.image.id, instance.state
             )
            )


### 2. available zones
def avail_zone():
    print('\n')
    print('2. available zones\n')
    print('DESC : Show your avilable zones\n\n')
    
    response = client.describe_regions()
    print('Regions:', response['Regions'])
    print('\n\n')
    available_region = client.describe_availability_zones()
    print(available_region)


### 3. start instance
def start_instance():
    print('\n')
    print('3. start instance \n')
    print('DESC : Start your instance. \n')
    instance_id = str(input('Please Enter instance id :'))
    
    response = client.start_instances(
            InstanceIds=[
                instance_id,
            ],
    )

    print(response)

### 5. stop instance
def stop_instance():
    print('\n')
    print('3. start instance \n')
    print('DESC : Start your instance. \n')
    instance_id = str(input('Please Enter instance id :'))
    
    response = client.stop_instances(
            InstanceIds=[
                instance_id,
            ]
    )
    print(response)


### #. Main Template
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
    elif number == 2:
        avail_zone()
    elif number == 3:
        start_instance()
    elif number == 5:
        stop_instance()
    elif number == 99:
        print('\n')
        print('Thank you')
        print('\n')
        break
    

import boto3

### Create Object
client = boto3.client('ec2')
ec2 = boto3.resource('ec2')
instance = ec2.Instance('id')

images = ec2.Image('id')


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
def avail_zones():
    print('\n')
    print('2. available zones\n')
    print('DESC : Show your avilable zones\n\n')
    
    available_zones = client.describe_availability_zones()
    print('Zones: {0}'.format(available_zones))
    print('\n\n')

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

### 4. available regions
def avail_regions():
    print('\n')
    print('4. available regions\n')
    print('DESC : Show your avilable regions\n\n')
    
    response = client.describe_regions()
    print('Regions:', response['Regions'])
    print('\n\n')

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

### 6. create instance
def create_instance():
    print('\n')
    print('6. create instance \n')
    print('DESC : create new instance. \n')
    image_id = str(input('Please Enter ami id:'))
    ec2.create_instances(ImageId=image_id, MinCount=1, MaxCount=5)
 
### 7. reboot instance
def reboot_instance():
    print('\n')
    print('7. reboot instance \n')
    print('DESC : Reboot your instance. \n')
    instance_id = str(input('Please Enter instance id :'))

    response = client.reboot_instances(
            InstanceIds=[
                instance_id,
                ],
            )

### 8. list images
def list_images():
    print('\n')
    print('8. list images \n')
    print('DESC : Show your list images. \n')
    
#    response = client.describe_images(
#        ExecutableUsers=[
#            'string',
#        ],
#        Filters=[
#            {
#                'Name': images.ImageIds,
#                'Values': [
#                    'string',
#                ]
#            },
#        ],
#        ImageIds=[
#            images.id,
#        ],
#        Owners=[
#            'string',
#        ],
#        IncludeDeprecated=True|False,
#        DryRun=True|False

    for images in ec2.images.all():
        print(
            "Id: {0}\n".format(images.id)
            )


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
        avail_zones()
    elif number == 3:
        start_instance()
    elif number == 4:
        avail_regions()
    elif number == 5:
        stop_instance()
    elif number == 6:
        create_instance()
    elif number == 7:
        reboot_instance()
    elif number == 8:
        list_images()
    elif number == 99:
        print('\n')
        print('Thank you')
        print('\n')
        break
    

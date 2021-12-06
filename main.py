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
            "Id: {0}\nPlatform: {1}\nType: {2}\nAMI: {3}\nState: {4}\n".format(
            instance.id, instance.platform, instance.instance_type, instance.image.id, instance.state))

### 2. available zones
def avail_zones():
    print('\n')
    print('2. available zones\n')
    print('DESC : Show your avilable zones\n\n')
    
    available_zones = client.describe_availability_zones()
    
    for zones in available_zones['AvailabilityZones']:
        print('ID: {0}\nRegion: {1}\nZone: {2}\n\n   '.format(zones['ZoneId'], zones['RegionName'], zones['ZoneName']))

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

    print('Starting ... {0}'.format(instance_id))
    print('Successfully started instance : {0}'.format(response['StartingInstances'][0]['InstanceId']))

### 4. available regions
def avail_regions():
    print('\n')
    print('4. available regions\n')
    print('DESC : Show your avilable regions\n\n')
    available_region = client.describe_regions()

    for zones in available_region['Regions']:
        print('Region: {0}       Endpoint: {1}'.format(zones['RegionName'], zones['Endpoint']))

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
    print('Stoping ... {0}'.format(instance_id))
    print('Successfully stopped instnace : {0}'.format(response['StoppingInstances'][0]['InstanceId']))

### 6. create instance
def create_instance():
    print('\n')
    print('6. create instance \n')
    print('DESC : create new instance. \n')
    image_id = str(input('Please Enter ami id:'))
    create_in = ec2.create_instances(ImageId=image_id, InstanceType='t2.micro', MinCount=1, MaxCount=1, KeyName='seokjin-test')
    print('Successfully started created EC2 instances {0} based on AMI ID {1}'.format(create_in[0].instance_id, create_in[0].image_id))   


### 7. reboot instance
def reboot_instance():
    print('\n')
    print('7. reboot instance \n')
    print('DESC : Reboot your instance. \n')
    instance_id = str(input('Please Enter instance id :'))

    response = client.reboot_instances(
            InstanceIds=[
                instance_id,
                ]
            )
    print('Rebooting ... {0}'.format(instance_id))
    print('Sccessfully rebooted instance : {0}'.format(instance_id))

### 8. list images
def list_images():
    print('\n')
    print('8. list images \n')
    print('DESC : Show your list images. \n')
    
    ami_image = client.describe_images(Owners=['self'])
    for ami in ami_image['Images']:
        print("ImageId: {0},    Name : {1},     Owner: {2}".format(ami['ImageId'], ami['Name'], ami['OwnerId']))


### 9. terminate instance
def terminate_instance():
    print('\n')
    print('8. terminate instance \n')
    print('DESC : Terminate your instance. \n')
    instance_id = str(input('Please Enter instance id :'))

    response = client.terminate_instances(
            InstanceIds=[
                instance_id,
            ],
    )

    print('Successfully terminated instance : {0}'.format(response['TerminatingInstances'][0]['InstanceId']))
    
### 10. key Pair Info
#key_pair_info = ec2.KeyPairInfo('name')

def key_pair_info():

    while(True):
        print('\n')
        print('10. Key Pair Information \n')
        print('DESC : Get Key Pair information. \n')
    
        print('-----------------------------------------------')
        print('                                               ')
        print('         Amazon Key Pair Information           ')
        print('                                               ')
        print('         Please Enter Option Number            ')
        print('-----------------------------------------------')
        print(' 1. Key Pair Create      2. Key Pair list      ')
        print(' 3. Delete Key Pair     99. Exit               ')
        print('                                               ')
        print('-----------------------------------------------')
        number2 = int(input('Enter an number:'))
        
        def create_key():
            key_name = str(input('Please enter create Key name :'))
            keypair = client.create_key_pair(KeyName=key_name)

            print('Success create Key Pair ID : {0}, Name : {1}'.format(keypair['KeyPairId'], keypair['KeyName']))

        def list_key():
            key_list = client.describe_Key_pairs()
            for k in key_list['KeyPairs']:
            print("KeyPairId: {0},    KeyName : {1},    KeyType: {2}".format(k['KeyPairId'], k['KeyName'], k['KeyType']))

            print('list')

        def delete_key():
            key_name = str(input('Please enter delete Key name : '))
            response = client.delete_key_pair(KeyName=key_name)

            print('Success delete key {0}'.format(response))

        if number2 ==1 :
            create_key()
        elif number2 == 2:
            list_key()
        elif number2 == 3:
            delete_key()
        elif number2 == 99:
            break


### 11. create image
def create_image():
    print('\n')
    print('12. create image \n')
    print('DESC : create image. \n')
    instance_id = str(input('Please Enter instance id :'))
    image_name = str(input('Please Enter image name (more than 3 letters): '))
    client.create_image(InstanceId=instance_id, NoReboot=True, Name=image_name)
    
    print('Create Image Success')



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
    print(' 9. terminate instance      10. key pair info     ')   
    print('11. create image            99. quit              ')
    print('                                                  ')
    print('--------------------------------------------------')


    number = int(input("Enter an number: "))

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
    elif number == 9:
        terminate_instance()
    elif number == 10:
        key_pair_info()
    elif number == 11:
        create_image()
    elif number == 99:
        print('\n')
        print('Thank you')
        print('\n')
        break
    

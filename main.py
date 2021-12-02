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
def avail_zones():
    print('\n')
    print('2. available zones\n')
    print('DESC : Show your avilable zones\n\n')
    
    available_zones = client.describe_availability_zones()
    
    for zones in available_zones['AvailabilityZones']:
        print('ID: {0}\nRegion: {1}\nZone: {2}\n\n   '.format(zones['ZoneId'], zones['RegionName'], zones['ZoneName']))


#   print('Zones: {0}'.format(available_zones['AvailabilityZones'][0]['ZoneName']))
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
    create_in = ec2.create_instances(ImageId=image_id, MinCount=1, MaxCount=5)
   
#    print('Successfully started started EC2 instances {0} based on AMI {1}'.format(create_in['SubnetId'] ,create_in['ImageId']))


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
    print('Rebooting ... {0}'.format(instance_id))
    print('Sccessfully rebooted instance : {0}'.format(instance_id))

### 8. list images
def list_images():
    print('\n')
    print('8. list images \n')
    print('DESC : Show your list images. \n')
    
    img = client.describe_images(Owners=['self'])

    print("ImageId: {0},    Name : {1},     Owner: {2}".format(img['Images'][0]['ImageId'], img['Images'][0]['Name'], img['Images'][0]['OwnerId']))

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

    print(response)
    
### 10. reload instance
def reload_instance():
    print('\n')
    print('10. reload instance \n')
    print('DESC : Reload you instance. \n')
    instance_id = str(input('Please Enter instance id :'))
    
    
 

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
    print(' 9. terminate instance      10. reload instance   ')
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
    elif number == 9:
        terminate_instance()
    elif number == 10:
        reload_instance()
    elif number == 99:
        print('\n')
        print('Thank you')
        print('\n')
        break
    

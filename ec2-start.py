import boto3

ec2 = boto3.resource('ec2')
instance1 = ec2.Instance('i-00387bc334f900398')
instance2 = ec2.Instance('i-038ed8dcd5fd39518')


#print(instance.report_status())

instance1.stop()
instance2.stop()

#print (report_status




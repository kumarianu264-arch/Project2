import boto3
import pprint


AWS_ACCESS_KEY_ID = "AKIA" \
"YBWO4BNICL2BFWHQ"
AWS_SECRET_ACESS_KEY"8BaCeDF+e8777XudxpNFg/NH7Lt3BDfsk16Gf8Of"
AWS_REGION_ID = "ap-south-1"



aws_session = boto3.Session(region_name=AWS_REGION_ID, AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)


ec2_client = aws_session.client('ec2') #create session

AMI = "ami-0305d3d91b9f22e84"

"t3.micro" #instance type
key pair = anu2025
sec-grp = 


response = ec2_client.run_instances(
    imageId="ami-0305d3d91b9f22e84" ,
    instanceType="t3.micro",
    KeyName="anu2025" ,
    SecurityGroupIds=[]   #get from documentation
    MinCount=1,
    MaxCount=1,
    tagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'key': "Name",
                    'Value': 'FrontEnd'
                }
            ]
        }
)


pprint.pprint(response) #
def create_instances(count):
   for i in range(count):


run the prog in terminal #
prettify  and paste the output from the terminal

pprint.pprint(response)
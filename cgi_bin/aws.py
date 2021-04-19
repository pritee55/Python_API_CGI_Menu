#!/usr/bin/python3
print("content-type:text/html")
print()

import subprocess as sp
import cgi
import boto3
import os

field = cgi.FieldStorage()
btn = field.getvalue("btn")

output =(0,"")

if btn == 'createKeybtn':
	keyname = field.getvalue("keyname")
	output = sp.getstatusoutput("aws ec2 create-key-pair --key-name {}".format(keyname))
	if(output[0] == 0):
		print("Key-pair created successfully!! \n {}".format(output[1]))
if btn == 'deleteKeybtn':
	keyname = field.getvalue("keyname")
	output = sp.getstatusoutput("aws ec2 delete-key-pair --key-name {}".format(keyname))
	if(output[0] == 0):
		print("Key-pair deleted successfully!! \n {}".format(output[1]))

elif btn == 'createsgbtn':
	grpname = field.getvalue("grpname")
	description = field.getvalue("description")
	vpc =  field.getvalue("vpc")
	output = sp.getstatusoutput('aws ec2 create-security-group --group-name {} --description "{}" --vpc-id {}'.format(grpname,description,vpc))
	if(output[0] == 0):
		print("Security group successfully!! \n {}".format(output[1]))
elif btn == 'addrulesbtn':
	grpid = field.getvalue("grpid")
	protocol = field.getvalue("protocol")
	port = field.getvalue("port")
	output = sp.getstatusoutput("aws ec2 authorize-security-group-ingress --group-id {} --protocol {} --port {} --cidr 0.0.0.0/0".format(grpid,protocol,port))
	if(output[0] == 0):
		print("Inbound rules added successfully!! \n {}".format(output[1]))
elif btn == 'launchbtn':
    image = field.getvalue("image")
    instance = field.getvalue("instance")
    count = field.getvalue("count")
    sgid = field.getvalue("sgid")
    keyname =field.getvalue("keyname")
    print("Instance launched of Id {} successfully".format(image))
elif btn == 'ebsbtn':
	ebsname = field.getvalue("ebsname")
	size = field.getvalue("size")
	az = field.getvalue("az")
	print("EBS volume created successfully!! \n {}".format(output[1]))
elif btn == 'attachebsbtn':
	instance = field.getvalue("instance")
	volid = field.getvalue("volid")
	output = sp.getstatusoutput("aws ec2 attach-volume --volume-id {} --instance-id {} --device /dev/sdf".format(volid,instance))
	if(output[0] == 0):
		print("EBS attached successfully!! \n {}".format(output[1]))
elif btn == 's3btn':
	bucketname = field.getvalue("bucketname")
	region = field.getvalue("region")
	output = sp.getstatusoutput("aws s3 mb s3://{} --region {}".format(bucketname,region))
	if(output[0] == 0):
		print("S3 bucket created successfully!! \n {}".format(output[1]))
elif btn == 'distbtn':
	bucketname = field.getvalue("bucketname")
	output = sp.getstatusoutput("aws cloudfront create-distribution --origin-domain-name {}.s3.amazonaws.com".format(bucketname))
	if(output[0] == 0):
		print("Distribution launched successfully!! \n {}".format(output[1]))
elif btn == 'desec2':
    ec2 = boto3.client('ec2','ap-south-1',aws_access_key_id='AKIASDNQ6QG7MSVQ5FGG',aws_secret_access_key='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')
    response = ec2.describe_instances()
    print(response)
elif btn == 'deskey':
    ec2 = boto3.client('ec2','ap-south-1',aws_access_key_id='AKIASDNQ6QG7MSVQ5FGG',aws_secret_access_key='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')
    response = ec2.describe_key_pairs()
    print(response)
elif btn == 'dessg':
	output = sp.getstatusoutput("aws ec2 describe-security-groups")
	if(output[0] == 0):
		print("Info of Existing Security-groups \n {}".format(output[1]))
elif btn == 'stbtn':
	instance = field.getvalue("instance")
	task = field.getvalue("task")
	output = sp.getstatusoutput("aws ec2 {}-instances --instance-ids {}".format(task,instance))
	if(output[0] == 0):
		print("Instance {} successfully!!".format(task,output[1]))
elif btn == 'chngper':
	b_name = field.getvalue("b_name")
	img_name = field.getvalue("img_name")
	permission = field.getvalue("permission")

	output = sp.getstatusoutput("aws s3api put-object-acl --bucket {} --key {} --acl {}".format(b_name,img_name,permission))
	if(output[0] == 0):
		print("Perminssions changed successfully!! \n {}".format(output[1]))
elif btn == 'upload':
	img_path = field.getvalue("img_path")
	b_name = field.getvalue("b_name")
	output = sp.getstatusoutput('aws s3 cp "{}" s3://{}'.format(img_path,b_name))
	if(output[0] == 0):
		print("Image uploaded in bucket {} successfully!! \n {}".format(b_name,output[1]))

if(output[0] != 0):
	print("Something went wrong!! \n\n {}".format(output[1]))

print("Done")	

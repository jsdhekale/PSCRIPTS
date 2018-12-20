import boto3


INSTANCE_CSV = "running_instances.csv"


def make_instance_csv(client, filename):
	""" Get the list of running instances and
		right them to CSV
	"""
	try :
		resp = client.describe_instances(Filters=[{
						'Name': 'instance-state-name', 
						'Values': ['running']}
					])
	except Exception as e:
		print(str(e))
		return False
	with open(filename, "w") as f:
		for resv in resp['Reservations']:
			for inst in resv['Instances']:
				instance_id, instance_ip = inst['InstanceId'], \
					inst['PublicIpAddress']
				hostname = next(t for t in inst['Tags'] \
								if t['Key'] == 'Name')['Value']
				f.write("%s,%s,%s\n" % (hostname, instance_id, instance_ip))
	return True


def main():
	client = boto3.client('ec2')
	make_instance_csv(client, INSTANCE_CSV)


if __name__ == "__main__":
	main()
import boto3

INSTANCE_CSV = "running_instances.csv"


def read_instance_list(filename):
	il = []
	with open(filename, "r") as f:
		for line in f:
			parts = line.strip().split(",")
			il.append({
				'hostname': parts[0],
				'id': parts[1],
				'ip': parts[2]
			})
	print(il)
	return il


def find_ebs_volumes_of(client, instance_list):
	volume_list = []
	for inst in instance_list:
		resp = client.describe_instances(InstanceIds=[inst['id']])
		instance_dict = resp['Reservations'][0]['Instances'][0]
		volume_list.extend([dev['Ebs']['VolumeId']\
				for dev in instance_dict['BlockDeviceMappings']])
	return volume_list


def main():
	client = boto3.client('ec2')
	instance_list = read_instance_list(INSTANCE_CSV)
	print(find_ebs_volumes_of(client, instance_list))


if __name__ == "__main__":
	main()
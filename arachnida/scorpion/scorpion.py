#!/usr/bin/env python3

import os
import time
import argparse

from PIL import Image, ExifTags

EXTENSIONS = ["jpg", "jpeg", "png", "gif", "bmp"]

def	analyze_image(image) -> None:
	image_pil = Image.open(image)
	image_exif = image_pil.getexif()

	print("============================")
	print(f" · Name: {image}")
	print(f" · Size: " + "{:.2f}".format(os.stat(image).st_size / 1000000) +  "MB")
	print(f" · Creation: {time.ctime(os.path.getctime(image))}")
	print(f" · Last modified: {time.ctime(os.path.getmtime(image))}")
	for key, val in image_exif.items():
		if key in ExifTags.TAGS:
			print(f' · {ExifTags.TAGS[key]}: {val}')
	print("============================")
	pass

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("images", metavar="IMAGES", nargs="+", help="List of images to analyze")

	args = parser.parse_args()
	for file in args.images:
		if not os.path.exists(file):
			print(file + " doesn't exist.")
			continue
		if os.path.isdir(file):
			print(file + " is a directory.")
			continue
		extension = file.split(".")
		if extension[-1] not in EXTENSIONS:
			print(file + " is not an image.")
			continue
		analyze_image(file)
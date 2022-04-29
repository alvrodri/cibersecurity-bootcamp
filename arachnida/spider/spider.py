#!/usr/bin/env python3

import argparse
import requests
import os

from bs4 import BeautifulSoup

EXTENSIONS = [".jpg", ".jpeg", ".png", ".gif", ".bmp"]
IMAGES = list()

def	get_images(url) -> None:
	soup = BeautifulSoup(requests.get(url).text, "html.parser")
	for image in soup.findAll("img"):
		src = image.get("src")
		if src is not None and src != "":
			src = src if src.startswith("http") else url + "/" + src
			IMAGES.append(src)

def	parse_web(url, current, level) -> None:
	soup = BeautifulSoup(requests.get(url).text, "html.parser")
	if current != level:
		for link in soup.findAll("a"):
			parse_web(link.get("href"), current + 1, level)
	get_images(url)

def	save_images(path="data/") -> None:
	for image in IMAGES:
		name = os.getcwd()+ "/" + path + (image.split("/")[-1])
		if not os.path.exists(name):
			file = open(name, "wb")
			file.write(requests.get(image).content)
			file.close()

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-r", action="store_true", help="Recursively downloads the images in a URL received as a parameter")
	parser.add_argument("-l", metavar="level", type=int, nargs=1, help="Indicated the depth level of the recursion", default=1)
	parser.add_argument("-p", metavar="path", type=str, nargs=1, help="Indicates the path where the download files will be saved", default="data/")
	parser.add_argument("url", metavar="URL", type=str, nargs=1, help="URL")

	args = parser.parse_args()
	parse_web(args.url[0], current=1, level=args.l[0])
	save_images(args.p)
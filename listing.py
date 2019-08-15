import os


def make_place_directories(places):
	for place in places:
		os.mkdir(place)


def extract_place(filename):
#version1	return  filename[filename.find("_") + 1 : filename.find("_", filename.find("_") + 1)]
#version2
	return filename.split("_")[1]


os.chdir("photos")
places = []
originals = os.listdir()
#print(extract_place("2016-11-04_Berlin_09/42/22.jpg"))
for file in originals:
	place = extract_place(file)
	if place not in places:
		places.append(place)
print(places)
make_place_directories(places)

import os





def extract_place(filename):
#version1	return  filename[filename.find("_") + 1 : filename.find("_", filename.find("_") + 1)]
#version2
	return filename.split('_')[1]


os.chdir("photos")
places = []
originals = os.listdir()
for file in originals:
	places.append(extract_place(file))
print(places)

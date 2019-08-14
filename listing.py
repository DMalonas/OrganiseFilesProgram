import os





def extract_place(filename):
#version1	return  filename[filename.find("_") + 1 : filename.find("_", filename.find("_") + 1)]
#version2
	return filename.split('_')[1]


os.chdir("photos")
originals = os.listdir()
print(extract_place("2016-11-04_Berlin_09/42/22.jpg"))


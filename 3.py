import os
def filename_generator(path_name):
    for folderpaths, folders, files in os.walk(path_name):
        for file in files:
            yield os.path.join(folderpaths, file)

print("Содержимое ")
gen1 = filename_generator('C:\\Users\\Admin\\Desktop\\folder1')
for path in gen1:
    print(path)

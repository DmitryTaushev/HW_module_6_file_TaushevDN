import os

path_learning = os.path.normpath(r'C:/Users/123mo/Desktop/HW_module_6_file_TaushevDN')
print(path_learning)

for path,dirnames,filenames in os.walk(path_learning):
    print(f"path - {path}")
    print(f"dirnames - {dirnames}")
    print(f"filenames - {filenames}")

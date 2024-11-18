import os

path_learning = os.path.normpath(r'C:/Users/123mo/Desktop/HW_module_6_file_TaushevDN')
print(path_learning)

for path,dirnames,filenames in os.walk(path_learning):
    print(f"path - {path}")
    print(f"dirnames - {dirnames}")
    print(f"filenames - {filenames}")

disk = 'C:\\'
dir_1 = 'Users'
dir_2 = '123mo'
dir_3 = 'Desktop'
dir_4 = 'HW_module_6_file_TaushevDN'
dir_5 = 'data_path_2'
dir_6 = 'test_file_3.txt'

path_module = os.path.join(disk,dir_1,dir_2,dir_3,dir_4,dir_5,dir_6)
print(path_module)
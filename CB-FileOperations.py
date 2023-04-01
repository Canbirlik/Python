import shutil
import os
import re

#pwd
#os.listdir()

#zipped_file = "zipped_file.zip"
#shutil.unpack_archive(zipped_file,"unzipped_dir","zip")

#f = open('unzipped_dir\\extracted_content\\Instructions.txt','r')
#f.read()
#f.close()

my_pattern = r'\d{3}-\d{3}-\d{4}'

def searching(file,folder):
    file_path = os.getcwd()+"\\"+folder+"\\"+"\\"+file
    my_file = open(file_path,'r')
    my_string = my_file.read()
    result = re.search(my_pattern,my_string)
    if result:
        print("There is a match for file {} and match is {}".format(file,result.group()))
        my_file.close()
    else:
        print ("No Match for file {}!".format(file))
        my_file.close()

for folder , sub_folders , files in os.walk(os.getcwd()):
    
    print("Currently looking at folder: "+ folder)
    print('\n')
    print("THE SUBFOLDERS ARE: ")
    for sub_fold in sub_folders:
        print("\t Subfolder: "+sub_fold )
        print('\n')
    print("THE FILES ARE: ")
    for f in files:
        print("\t File: "+f)
        print('\n')

import os
import string
import shutil
import time

# insert the message in secret message
secret_message="ineedsleep"
#make a empty dictionary to add mapping of alphabets to pictures in folder
mapping={}
index_count=0

#the path where you keep folder
path=r"c:/users/nones/desktop/alphabet"
folder_name="alphabet"
original_folder=os.path.join(path,folder_name)
file_name_list=os.listdir(os.path.join(path,folder_name))
# print file_name_list
# print file_name_list
#create a mapping of alphabet to picture
list_of_alphabets=list(string.ascii_lowercase)
for items in  file_name_list:
	print items 
	try:
	# print items
		mapping[list_of_alphabets[index_count]]=file_name_list[index_count+1]
		index_count+=1
		# print mapping
	except:
# 		for now
		pass 
print mapping

secret_folder=os.path.join(path,"secret")

if os.path.isdir(secret_folder):
	# delete the folder if already present
	shutil.rmtree(secret_folder)
	time.sleep(10)
	# inserting sleep because the folder becomes unresponsive after deleting for a while
	# and access denied error is thrown if script is run in quick succesions.
	# create the folder gain
	os.mkdir(secret_folder)
else:
	# cretae folder for first time
	os.mkdir(secret_folder)

r_counter=0
for items in secret_message:
	file_needed=mapping[items]
# 	print file_needed
# copy from original folder to the secret folder,all the files that is needed to encode message
	shutil. copyfile(os.path.join(original_folder,file_needed),os.path.join(secret_folder,file_needed))
# 	need to rename because files are sorted in alphabetical order in window,no idea about other os
	os.rename(os.path.join(secret_folder,file_needed),os.path.join(secret_folder,str(r_counter)+file_needed))
	r_counter+=1

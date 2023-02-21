import copy
import os

from KeyFolder import KeyFolder
from preflight_check import check_parameters


def s3_keys_to_dict(keys_list):
    # This function requires the keys to have a common root, like a directory.
    # One of the keys should be that root.
    check_parameters(keys_list)
    
    file_list, folder_list = sort_keys_to_files_and_folders(keys_list)
    add_files_to_folders(file_list, folder_list)
    final_folder = sort_folders_into_parent_folders(folder_list)
    return final_folder


##################################################
# Secondary Functions
##################################################

def sort_keys_to_files_and_folders(keys_list):
    file_list = []
    folder_list = []

    for key in keys_list:
        if isFolder(key):
            folder_obj = KeyFolder(key)
            folder_list.append(folder_obj)
        else:
            file_list.append(key)

    return file_list, folder_list


def add_files_to_folders(file_list, folder_list):
    file_ls = copy.deepcopy(file_list)

    for folder in folder_list:
        for idx, file in reversed(list(enumerate(file_ls))):
            if fileIsInFolder(file, folder):
                file_dict = get_key_name_type_of_file(file)
                folder.items.append(file_dict)
                del file_ls[idx] # safe to delete because loop is reversed
    

def sort_folders_into_parent_folders(folder_list):

    for idx, folder in reversed(list(enumerate(folder_list))):
        if folderIsRoot(folder.key):
            break # skip root folder
        for parent in folder_list:
            if isParentFolder(folder, parent):
                f_dict = folder.get_dict_of_object()
                parent.items.append(f_dict)
                del folder_list[idx] # safe to delete because loop is reversed
                break
    
    return folder_list[0].get_dict_of_object()


##################################################
# Tertiary Functions
##################################################

def isFolder(key):
    last_split = key.rsplit('/', 1)[-1]
    if last_split == "":
        return True
    else:
        return False


def fileIsInFolder(file, folder):
    file_path = os.path.dirname(file) +'/'
    if file_path == folder.key:
        return True
    else:
        return False


def folderIsRoot(key):
    if len(key.split('/')) == len(key.split('/',1)):
        return True
    else:
        return False


def isParentFolder(folder, parent):
    folder_parent = folder.key.rsplit('/',2)[0] + '/'
    if folder_parent == parent.key:
        return True
    else:
        return False
    

def get_key_name_type_of_file(file):
    file_dict = {}
    file_dict['key'] = file
    file_dict['name'] = file.split('/')[-1]
    file_dict['type'] = "file"
    return file_dict

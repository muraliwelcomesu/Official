import os

def get_files_dict(dir_name,p_list_files):
    for file_name in os.listdir(dir_name):
        if os.path.isdir(os.path.join(dir_name,file_name)):
            dir_name_1 = os.path.join(dir_name,file_name)
            get_files_dict(dir_name_1,p_list_files)
        elif os.path.isfile(os.path.join(dir_name,file_name)):
            if file_name.endswith('.spc') or file_name.endswith('.sql') or file_name.endswith('.prc'):
                p_list_files.append(os.path.join(dir_name,file_name))
                
def validateBackSlash(lst_files):
    lst_missing = []
    for file_name in lst_files:
        fp = open(file_name,'r')
        lst_lines = fp.readlines()
        fp.close()
        last = None
        for line in (line for line in lst_lines if line.rstrip()):
            last = line
        if (last.strip()  != '/'):
            #print(file_name,'last is ',last)
            lst_missing.append(file_name)
    #print('Completed')
    return lst_missing

if __name__ =='__main__':
    #dir_name = 'D:\\14.3_analysis\\ic-standalone\\ICJAVA_SVN\\APPLICATION'
    dir_name = input('Enter the Directory name :')
    if os.path.isdir(dir_name):
        os.chdir(dir_name)
        lst_files = []
        get_files_dict(dir_name,lst_files)
        lst_missing = validateBackSlash(lst_files)
        if len(lst_missing) > 0:
            print('Backslash missing in following files')
            for i in lst_missing:
                print(i)
        else:
            print('File verification complete.No issues detected')
    else:
        print('Invalid Directory given')
import os
''' Get directory name as input and prepare a script to compile all the files in the directory and 
its subdirectories. The files will be taken in the order of modification order in each folder.
'''
def get_files_dict(dir_name,p_dict_files):
    print('processing',dir_name)
    for file_name in os.listdir(dir_name):
        if os.path.isdir(os.path.join(dir_name,file_name)):
            dir_name_1 = os.path.join(dir_name,file_name)
            p_dict_files[dir_name_1] = []
            get_files_dict(dir_name_1,p_dict_files)
        elif os.path.isfile(os.path.join(dir_name,file_name)):
            if dir_name in p_dict_files: 
                l_list = p_dict_files[dir_name]       
                l_list.append(os.path.join(dir_name,file_name))
                p_dict_files[dir_name] = l_list
            else:
                p_dict_files[dir_name]  = os.path.join(dir_name,file_name)
                
def prepare_script(p_dict):
    file_write = open("C:\\Users\\MURENGAR\\Desktop\\Output\\Latest\\Compilation_Script.sql",'w')
    for key,value in p_dict_files.items():
        value.sort(key=lambda x: os.path.getmtime(x))

        for i in value:
            l_Str1 = 'prompt " executing ' + i + '"'
            l_Str2 = '@"' + i +'"; \n'
            file_write.write(l_Str1 + '\n')
            file_write.write(l_Str2)
            #print(l_Str1)
            #print(l_Str2)
    file_write.close()


if __name__ =='__main__':
    #dir_name = 'D:\\14.3_analysis\\ic-standalone\\ICJAVA_SVN\\APPLICATION'
    dir_name = input('Enter the Directory name :')
    print('Directory entered is '+ dir_name)
    if os.path.isdir(dir_name):
        os.chdir(dir_name)
        p_dict_files = {}
        get_files_dict(dir_name,p_dict_files)
        prepare_script(p_dict_files)
        print('Completed File Compilation_Script.sql created in working dir')
    else:
        
        print('Invalid Directory Given... ')
        
    
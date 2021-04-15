import os
import send2trash,shutil
''' Get directory name as input and  get all the files from all subdirectories in a folder Consolidated'''

def get_files_dict(dir_name,p_dict_files):
    print('processing',dir_name)
    exclude_list = ['.svn']
    for file_name in os.listdir(dir_name):
        if file_name in exclude_list:
            continue
        if os.path.isdir(os.path.join(dir_name,file_name)):
            dir_name_1 = os.path.join(dir_name,file_name)
            get_files_dict(dir_name_1,p_dict_files)
        elif os.path.isfile(os.path.join(dir_name,file_name)):
            #print(file_name)
            #print(p_dict_files)
            if dir_name in p_dict_files: 
                l_list = p_dict_files[dir_name]   
                #print(dir_name,file_name)    
                l_list.append(os.path.join(dir_name,file_name))
                p_dict_files[dir_name] = l_list
            else:
                lst_tmp = []
                lst_tmp.append(os.path.join(dir_name,file_name))
                p_dict_files[dir_name]  = lst_tmp
                lst_tmp = []
                
if __name__ =='__main__':
    print('Start of Program.. '+ '\n')
    print('This Program will get all files in a directory and its subdirectories in a Consolidated Directory \n')
    dirname = input('Enter the Source Directory Name :') #"D:\\Rajamanikam\\10-Mar-2021"
    
    #print(os.path.split(dirname))
    if not os.path.exists(os.path.join(dirname,'Consolidated')):
        print('Creating Consolidated Directory')
        os.mkdir(os.path.join(dirname,'Consolidated'))
    else:
        print('Clearing Consolidated Directory')
        for file  in os.listdir(os.path.join(dirname,'Consolidated')):
            send2trash.send2trash(os.path.join(dirname,'Consolidated',file))
            
        
    lst_dict = {}
    get_files_dict(dirname,lst_dict)
    print('#####################################')
    fp  = open(os.path.join(dirname,'Consolidated','List_Files.txt'),'w')
    for key,value in lst_dict.items():
        print(key,value)
        fp.write('Directory Name :{} \n'.format(key) )
        if len(value) > 0 :
            for file in value:
                fp.write(file + '\n')
                shutil.copy(file,os.path.join(dirname,'Consolidated'))

        else:
            fp.write('No files found in this directory')      
        fp.write('\n')
    fp.close()  
    print('Completed')
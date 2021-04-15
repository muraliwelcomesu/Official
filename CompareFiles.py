import os,filecmp

def file_compare(dir1,dir2):
    lst_files = os.listdir(dir1)
    matched,  mismatched, errors = filecmp.cmpfiles(dir1,dir2,lst_files)
    print('No.of.Files Compared is {}'.format(len(lst_files)))
    print('No.of.Files Matched  is {}'.format(len(matched)))
    print('Files having Error on comparision  is {}'.format(len(errors)))
    print('No.of.Files having Mismatch is {}'.format(len(mismatched)))
    if len(mismatched) > 0:
        print('following files have mismatch:')
        for i in mismatched:
            print(i)
    if len(errors) > 0:
        print('Following files have error on comparision...')
        for i in errors:
            print(i) 
    
    
    

if __name__ == "__main__":
    print('Start of Comparing files in two directories.... ')
    print('\n')
    l_dir1 = input('Enter First Directory :')
    print('\n')
    l_dir2 = input('Enter Second Directory :')
    print('\n')
    print('Files in {} will be compared with {}'.format(l_dir1,l_dir2))
    print('\n')
    file_compare(l_dir1,l_dir2)
    print('Completed..')
    
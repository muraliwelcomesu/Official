import os
'''
    For the given path, get the List of all files in the directory tree 
'''
def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles        


def main():
    
    tmp_dirName = input('Enter the DirectoryName (fullpath reqd) :')
    dirName  = os.path.join('\\\\'.join(tmp_dirName.split('\\')))
    print('Displaying the list of files in Directory {} \n'.format(dirName))
    # Get the list of all files in directory tree at given path
    listOfFiles = getListOfFiles(dirName)
    
    # Print the files
    '''for elem in listOfFiles:
        print(elem)

    print ("****************")'''
    
    # Get the list of all files in directory tree at given path
    listOfFiles = list()
    for (dirpath, dirnames, filenames) in os.walk(dirName):
        listOfFiles += [os.path.join(dirpath, file) for file in filenames]
        
    listOfFiles = [x.replace(dirName,'') for x in listOfFiles]    
    # Print the files
    fp = open('C:\\Users\\MURENGAR\\Desktop\\ListofFiles.txt','w')
    fp.write('List of Files in Directory (and its subdirectories) of  {} \n '.format(tmp_dirName)) 
    fp.write('\n')   
    for elem in listOfFiles:
        if elem.endswith('.html'):
            fp.write(elem + '\n')
    fp.close()
    print('Completed')
        
        
        
        
if __name__ == '__main__':
    main()

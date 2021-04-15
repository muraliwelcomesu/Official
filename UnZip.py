import os
from zipfile import ZipFile

def UnZip():
    print(' ******** Extract Specific Files from ZipFile  ***************************')
    
    Zip_dir_name = input('Enter Directory Name:Eg: [D:\\tmp:')
    ZipFile = input('Enter ZipFile :')
    StartFilter   = input('Fetch files begining with :')
    EndFilter  = input('Fetch files Ending with :')
    if len(StartFilter.strip()) == 0:
        StartFilter = '*'
    if len(EndFilter.strip()) == 0:
        EndFilter = '*' 
    os.chdir(Zip_dir_name)
    File = os.path.join(Zip_dir_name,ZipFile)
    with ZipFile(File, 'r') as zipObj:
        listOfFileNames = zipObj.namelist()
        if StartFilter != '*':
            listOfFileNames = [x.startswith(StartFilter) for x in listOfFileNames]
        if EndFilter != '*':
            listOfFileNames = [x.endswith(EndFilter) for x in listOfFileNames]
        for fileName in listOfFileNames:
            zipObj.extract(fileName)
    print(' ******** Extract Specific Files from ZipFile  Completed ***************************')


if __name__ == "__main__":
    UnZip()

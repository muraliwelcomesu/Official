#Format XML using BeautifulSoup and write it to text file so as to compare using any compare tools.
from bs4 import BeautifulSoup
import os,sys
def  fn_format_file(files):
    for xmlfile in files:

        bs = BeautifulSoup(open(xmlfile), 'xml')
        bs = bs.prettify()
        filename, file_extension = os.path.splitext(xmlfile)
        l_out_file = filename + '_f.txt'
        print('processed {} Outfile - {}'.format(xmlfile,l_out_file))
        with open(l_out_file, 'w') as f:
            for line in bs:
                f.write(str(line))
        
if __name__ == "__main__":
    print('Start of Format_xml..')
    print('Ensure files are placed in D:\work_dir')
    dir_name = 'D:\\work_dir'
    os.chdir(dir_name)
    files = []
    for file_name in os.listdir(dir_name):
        if file_name.upper().endswith('.XML'):
            files.append(file_name)
    fn_format_file(files)
    print('Completed')
    
    
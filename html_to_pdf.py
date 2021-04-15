import pdfkit 
import os

def convert_html_pdf(url,pdfname):
    pdfkit.from_url(url,pdfname) 


def prepare_pdf():
    print('Start of prepare_pdf')
    base_folder = 'D:\\knowledge\\Medium_output'
    lst_dir = os.listdir(base_folder)
    for dirs in lst_dir:
        print('Processing {}'.format(dirs))
        os.chdir(os.path.join(base_folder,dirs))
        lst_files = [x for x in os.listdir() if x.endswith('.html')]
        print(lst_files)
        pdfname = '{}.pdf'.format(dirs)
        pdfkit.from_file(lst_files, pdfname)
        print('Directory {} Completed'.format(dirs))

def convert_pdf():
    os.chdir('C:\\PDFs')
    l_continue = 'Y'
    while l_continue != 'N':
        l_url = input('Enter the URL that needs to be converted to PDF:')
        l_pdfname = input('Enter the PDF Name :')
        convert_html_pdf(l_url,l_pdfname)
        l_continue = input('Convert another File? Y/N')
        print('completed..')
            
        
if __name__ == '__main__':
    convert_pdf()

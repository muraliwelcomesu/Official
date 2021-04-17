import cx_Oracle
import numpy as np
import openpyxl,os, sys,re

def execute_query(p_conn_Str,p_query_str):
    connection1 = cx_Oracle.connect(p_conn_Str)
    cur1 = connection1.cursor()
    result1 = []
    rs1 = cur1.execute(p_query_str)
    for res1 in cur1:
        result1.append(res1[0])
    cur1.close()
    connection1.close()
    return result1

def get_files_dict(dir_name,p_list_files):
    for file_name in os.listdir(dir_name):
        if os.path.isdir(os.path.join(dir_name,file_name)):
            dir_name_1 = os.path.join(dir_name,file_name)
            get_files_dict(dir_name_1,p_list_files)
        elif os.path.isfile(os.path.join(dir_name,file_name)):
            if file_name.endswith('.spc') or file_name.endswith('.sql') or file_name.endswith('.prc'):
                p_list_files.append(os.path.join(dir_name,file_name))

def get_referenced_names(p_search_object):
    #print('Start of get_referenced_names')
    p_search_object = p_search_object.upper()
    p_path = 'D:\\14.3_analysis\\ic-standalone\\ICJAVA_SVN\\APPLICATION'
    os.chdir(p_path)
    l_conn_str = 'ICUAT/ICUAT@DLY1221_FC124R2'
    l_query = 'SELECT synonym_name  from user_synonyms  where table_name = ' + "'" + p_search_object  + "'"
    #print(l_query)
    l_out_results = execute_query(l_conn_str,l_query)
    l_lst_search = []
    lst_files = []
    l_lst_search.append(p_search_object)
    for i in l_out_results:
        l_lst_search.append(i)
    get_files_dict(p_path,lst_files)
    l_dict_results = {}
    for file_name in lst_files:
        fp = open(file_name,'r')
        lines = fp.readlines()
        l_output = []
        for l_search_str in l_lst_search:
            lst_indexes = [n for n,x in enumerate(lines) if l_search_str in x.upper()]
            l_sel_lines = []
            for i in lst_indexes:
                l_sel_lines.append(lines[i])
            for i in l_sel_lines:
                l_tmp_list = i.split()
                for j in l_tmp_list:
                    if l_search_str in j.upper():
                        l_str = re.sub(r'.*' + l_search_str,l_search_str, j)
                        l_output.append(l_str)
        if len(l_output) > 0:
            l_dict_results[file_name] = list(set(l_output))
        fp.close()
    return l_dict_results
    #print('Completed')

def pr_write_file(p_search_object,l_dict_results):
    os.chdir('C:\\Users\\MURENGAR\\Desktop\\Output')
    file_name = p_search_object + '.txt'
    fp = open(file_name,'w')
    for key,values in l_dict_results.items():
        fp.write('FileName  :: ' + key + '\n')
        for i in values:
            fp.write(i + '\n')
        fp.write('\n')

if __name__ =='__main__':
    print('Starting')
    print('Given a list of objects, each will be searched in all files in specific folders from SVN and result will be written separatly for each object')
    l_Search_string= ['CSPKES_MISC','CSPKS_OS_PARAM','CSPKS_REQ_GLOBAL','CSPKS_REQ_UTILS','CSTB_PARAM','CSTBS_DEBUG','CSTM_PRODUCT','CYPKS','CYTM_CCY_DEFN','CYTMS_RATES','ERTBS_MSGS','GLOBAL','GWPKS_UTIL','SMTBS_CURRENT_USERS','SMTBS_USER','STTBS_VALUE_DESC','STTM_CORE_ACCOUNT','STTM_CORE_BRANCH_STATUS','STTM_CORE_EL_LIAB','STTM_CORE_EL_LIAB_CUST','STTM_DATES','STTMS_BRANCH','STTMS_CCY_HOL_MASTER','STTMS_CCY_HOLIDAY','STTMS_DATES','STTMS_LCL_HOL_MASTER','STTMS_LCL_HOLIDAY','TRSQ_JOB_SEQ']
    for  p_search_object in l_Search_string:
        l_dict_results = get_referenced_names(p_search_object)
        pr_write_file(p_search_object,l_dict_results)
    print('Completed.. Files available in Output Folder.')
    
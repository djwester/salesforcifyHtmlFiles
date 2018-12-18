from bs4 import BeautifulSoup
import os
import argparse
import fnmatch

def is_config_in_line(line_of_text):
    if 'd2l.' in line_of_text and line_of_text.count('.') > 2:
        return True
    return False

def get_config_substring(line_of_text):
    config = 'd2l.'
    config += line_of_text.split('d2l.')[1]
    rebuilt_config = ''
    for piece in config.split('.'):
        if ' ' in piece:
            #last element of the config
            piece = piece.split(' ')[0]
            rebuilt_config += piece
            break
        rebuilt_config += '%s.'%piece
    if rebuilt_config.endswith('.'):
        rebuilt_config = rebuilt_config[:-1]
    return rebuilt_config

def add_span_tags_to_config(line_of_text):
    spanned_config = ''
    config = get_config_substring(line_of_text)
    for piece in config.split('.'):
        spanned_config += '<span>%s</span>.'%piece
    #remove extra . from the end
    spanned_config = spanned_config[:-1]
    new_line_of_text = line_of_text.replace(config,spanned_config)
    return new_line_of_text

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-f' '--folder', dest='search_folder',
                   help='specify the folder containing the files to convert. The script will attempt to convert all .html files in this folder')

def get_file_list(root_dir, filter_list=['.html','.htm']):
    initial_files =  os.listdir(root_dir)
    files = []
    for each_filter in filter_list:
        filtered_files = fnmatch.filter(initial_files, '*%s'%each_filter)
        files += filtered_files

    file_list = []
    for filename in files:
        file_list.append(os.path.join(root_dir, filename))

    return file_list

args = vars(parser.parse_args())
root_dir = args['search_folder']

file_list = get_file_list(root_dir,['.html','.htm'])

for file in file_list:
    print ('converting %s...'%file)
    clean_html = ''
    with open(file) as f:
        soup = BeautifulSoup(f, 'html.parser')
    
    #remove everything except body
    html_body = soup.body
    clean_html = str(html_body)
    clean_html = clean_html.replace('<body>','')
    clean_html = clean_html.replace('</body>','')

    soup2 = BeautifulSoup(clean_html,'html.parser')

    #set the <h1> styles
    if soup2.h1:
        soup2.h1['style'] = "color: rgb(255, 255, 255); background-color: rgb(232, 117, 17);"
    
    #set the width of the <th> tags to 20%
    ths = soup2.thead.find_all('th')
    if ths:
        for th in ths:
            th['style'] = "width: 20%; text-align: left;"
    first_row_tds = soup2.tbody.tr.find_all('td')
    if first_row_tds:
        #assume the first column is 'impact of change'
        first_row_tds[0]['style'] = "width: 20%;"
        first_row_tds[0]['valign'] = "top"
        #assume the second column is 'technical details'
        first_row_tds[1]['style'] = "width: 50%;"
        first_row_tds[1]['valign'] = "top"

    prettified_html = soup2.prettify()
    html_with_spans_added = ''
    for line in prettified_html.split('\n'):
        if is_config_in_line(line):
            line = add_span_tags_to_config(line)
        html_with_spans_added += '%s\n'%line

    base,f = os.path.split(file)
    if not os.path.exists(os.path.join(base,'edited')):
        os.mkdir(os.path.join(base,'edited'))
    new_file_name = os.path.join(base,'edited',f)
    with open(new_file_name,'w') as new_file:
        new_file.write(html_with_spans_added)

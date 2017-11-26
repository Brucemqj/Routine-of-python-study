# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 18:48:21 2017

@author: qijiang.ma
"""
'''In this script I will propose some function to operate files'''

#Below function receives inputs from user and save as new file
def file_create_and_write(file_name):
    f = open(file_name, 'w')
    print('Please input your content and exit it by typing \'exit\'')
    
    while True:
        content = input('Input here: ')
        if content != 'exit':
            f.write('%s\n' % content)
        else:
            break
        
    f.close()
    
#Below function can replace contents in a file by stuff you give
def file_content_replace(file_name, old_word, new_word):
    f_read = open(file_name)
    
    content = []
    count = 0
    for each_line in f_read:
        if old_word in each_line:
            count = each_line.count(old_word)
            each_line.replace(old_word, new_word)
        content.append(each_line)
        
    decision = input('\nfile %s has %s of %d time(s), sure for option replace all?\n[yes\no]:' \ 
                     % (file_name, old_word, count))
    
    choice_y = ['YES', 'Yes', 'yes']
    if decision in choice_y:
        f_write = open(file_name, 'w')
        f_write.writelines(content)
        f_write.close()
        
        
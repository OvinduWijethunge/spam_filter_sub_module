# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 23:00:58 2020

@author: Acer
"""


import csv


def makes_csv(cid, sim_content,sin_comment ,word_count,duplicate_word_ratio,no_of_sentences,length_of_comment,num_of_punctuations,is_period_sequence,post_coment_gap,black_word_count,is_link,is_youtube_link,is_number,comment_duplication):
        
        list_values = [cid, sim_content,sin_comment ,word_count,duplicate_word_ratio,no_of_sentences,length_of_comment,num_of_punctuations,is_period_sequence,post_coment_gap,black_word_count,is_link,is_youtube_link,is_number,comment_duplication]
        
        stringList = [str(x) for x in list_values]  # convert all fields values to string value
        return stringList
        
    
def create_file(fields_list):
    
    
    fields =  ['cid', 'sim_content','sim_comment' ,'word_count','duplicate_word_ratio','no_of_sentences','length_of_comment','num_of_punctuations','is_period_sequence','post_coment_gap','black_word_count','is_link','is_youtube_link','is_number','comment_duplication']
    rows = fields_list
    
    filename = "data.csv"
    with open(filename, 'w') as csvfile:
        writer = csv.writer(csvfile) 
        writer.writerow(fields)  
        writer.writerows(rows)    
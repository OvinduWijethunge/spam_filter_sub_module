# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 10:04:15 2021

@author: Acer
"""

import re
from func_geting_features import check_black_words_list


def link_mob_mail_length_blckword(text):

    st = ' '.join(text)
  
    list_val = []
    com_length = len(st)
    list_val.append(com_length)

    word_count = len(text)

    list_val.append(word_count)

    isLink = 0
    isYoutubeLink = 0
    x = re.findall("\ https|http", st)
    if len(x)> 0:
        isLink = 1
        
        for i in text:
            
            y = re.search("youtu",i)
            if y is not None:
                
                isYoutubeLink = 1
                break

    list_val.append(isLink)
    list_val.append(isYoutubeLink)


    isTnumber = 0
    x = re.findall("\d{10}|\d{9}", st)
    if len(x) > 0:
        number = x[0]
        isTnumber = 1

    list_val.append(isTnumber) 
    
    #print("phone number is ",isTnumber)  
    
    
# =============================================================================
#     isMail = 0
#     x = re.findall(r'[\w\.-]+@[\w\.-]+(\.[\w]+)+', st)
#     #print(x)
# 
#     if len(x)!= 0:
#         
#         isMail = 1
#     list_val.append(isMail)    
# =============================================================================
    black_words_count = check_black_words_list(text)
    list_val.append(black_words_count)

    return list_val 
    






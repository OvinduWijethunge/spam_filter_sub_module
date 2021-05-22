# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 00:48:37 2020

@author: Acer
"""
from nltk.tokenize import word_tokenize
from func_vector_create import vectorize
from func_preprocessing import preprocess

def find_duplicate_comments(main_list, val):
    
    sub_list = main_list[val]
    channel_id = sub_list[4]
    comment = sub_list[3]
    maxv = 0
    #count = 0
    ct = 0
    for rowd in main_list:

               if val == ct: 

                   ct +=1
                   continue
               else:
                   
                   ct +=1 
                   if channel_id == rowd[4]:
                       

                       row_comment = rowd[3]
                        
                       dataset = [comment , row_comment]

                       Ne = len(dataset) 
                        
                       processed_text = []
    
                       for text in dataset[:Ne]:
                        
                           processed_text.append(word_tokenize(str(preprocess(text))))#this is a list in list which have tokenize strings duplicate words also here
                    
                       vectors_list = vectorize(processed_text)
                       

      
                       vec1 = vectors_list[0]
                       vec2 = vectors_list[1]
                       dot = sum(a*b for a, b in zip(vec1,vec2))
                       norm_a = sum(a*a for a in vec1) ** 0.5
                       norm_b = sum(b*b for b in vec2) ** 0.5
                            
                            
                       cos_sims = dot / (norm_a*norm_b)

                       if maxv <= cos_sims:
                            
                           maxv = cos_sims

    return maxv    
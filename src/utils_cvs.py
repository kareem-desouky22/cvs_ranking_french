# -*- coding: utf-8 -*-
"""
Created on Sun May 16 13:51:21 2021

@author: KHC
"""
from collections import Counter
from itertools import chain


# this function will return top most frequent elements of  a list
# we are using it for filtering of qualification and skills

def top_frequent(nums, k):
    
    
    # this if else condition will pad '' to list if elements of list are less
    # than the value of k
    
    if len(nums)>=k:
#        print ('we got enough elements')
            
        
            
        
            

        bucket = [[] for _ in range(len(nums) + 1)]
    
        Count = Counter(nums).items()  
    
        for num, freq in Count: 
            bucket[freq].append(num) 
    
            flat_list = list(chain(*bucket))
    
#            return flat_list[::-1][:k]
            return_list=flat_list[::-1][:k]
    
    else:
        nums=list(set(nums))
        nums += [''] * (k - len(nums))
        return_list=nums
    
    return (return_list)

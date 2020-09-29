# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 20:21:31 2020

@author: Sofia
"""
import hash_table_chain as htc 
import read_text_files as read_files
import os
import time 



def stopwords2List(s):
    f = open(s, 'r', encoding = "utf8")
    text = f.read()
    f.close()
    L = read_files.get_word_list(text)
    return L


def load_factor(h):
    count = 0 
    for i in range (len(h.bucket)): 
            count+= len(h.bucket[i])
    return count/len(h.bucket)

def empty_bucket_fraction(h): 
    count = 0 
    for i in range(len(h.bucket)):
        if len(h.bucket[i]) == 0: 
            count +=1
    return count/len(h.bucket)

def long_bucket_F(h): 
    long = 0
    lb = len(h.bucket[0])
    for i in range(len(h.bucket)): 
        if len(h.bucket[i]) > 1: 
            long +=1
        if len(h.bucket[i]) > lb:
            lb = len(h.bucket[i])
    print("Long bucket fraction in table: ", long/len(h.bucket))
    print("Length of the longest bucket in table:", lb)
    return 

def hash_Stats(L): 
    h = htc.HashTableChain(len(L))
    records  = 0
    for i in range(len(L)):
        if h.retrieve(L[i]) == None: 
            records +=1
        h.insert(L[i],L[i])
    print("Total buckets: ", len(h.bucket))
    print("Total records: ", records)
    print("Load factor: ", load_factor(h))
    print("Empy bucket fraction in table: ", empty_bucket_fraction(h))
    long_bucket_F(h)
    return h




    
    
def abstract_Stats(name,L,h): 
    new_list = []
    stop_words  = 0
    records = 0
    common_num = 0
    num = 0 
    for i in range(len(L)):
        if L[i] != h.retrieve(L[i]):
            new_list.append(L[i])
        else: 
            stop_words +=1
    print("Total words: ", len(L))
    print("Total non-stop words: ", len(L)-stop_words)
    print("Analysis of",name, "hash table")
    b = htc.HashTableChain(len(new_list))
    for j in range(len(new_list)):
        num = b.retrieve(new_list[j])
        if num is None:
            b.insert(new_list[j],1)
            records+=1
        else: 
            num+=1
            b.update(new_list[j],num)
            if b.retrieve(new_list[j]) > common_num :
                common_num = b.retrieve(new_list[j])
                common_word = new_list[j]
    print("Total buckets: ", len(b.bucket))
    print("Total records: ", records)
    print("Load factor: ", load_factor(b))
    print("Empy bucket fraction in table: ", empty_bucket_fraction(b))
    long_bucket_F(b)
    print("Most common word: ", common_word,"occurs -", common_num, "times")
    return 

#    
#import time
#start_time = time.time()
#main()
#print("--- %s seconds ---" % (time.time() - start_time))


def main(): 
    stop_words = stopwords2List("stop_words.txt")
#    start_time = time.time()
    stop = hash_Stats(stop_words)
#    print("this is the time for stop words", (time.time()-start_time))
#    stop.print_table()
    print()
    
    #abstracts file: 
    abs_dir = '.\\abstracts\\'
    file_list = sorted(os.listdir(abs_dir))
    file_list = file_list[:1]
    
    start_time = time.time()

    for i in file_list:
        print("File: ", i)
        f = open(abs_dir+ i, 'r', encoding = "utf8")
        text = f.read()
        f.close()
        abs_list = read_files.get_word_list(text)
        abstract_Stats(i,abs_list, stop)
        print()
    print("this is the time for stop words", (time.time()-start_time))
   
#        
        
 
main()




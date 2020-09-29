# -*- coding: utf-8 -*-
"""
Created on Fri May  8 23:11:04 2020

@author: Sofia
"""

import numpy as np
import time 
#backtracking algorithm 

def knapsack(W,D,v,w):
    # W is the remaining knapsack capacity, D is the remaining debt, v and w are lists of the
    # same length where item 0 has value v[0] and weight w[0], item 1 has value v[1] and
    # weight w[1], and so on.
    if len(v) == 0 and D > 0: 
        return False
    if W<0: # knapsack capacity exceeded
        return False
    if D<=0: # debt paid
        return True
    return knapsack(W-w[0],D-v[0],v[1:],w[1:]) or knapsack(W,D,v[1:],w[1:])
    
    
#greedy algorithm 
#sort the items by decreasing value to weight ratio (vwr=v/w),
#then go through the list of items sorted by vwr, adding the item to the knapsack 
#if there is still room for it.  If at the end the debt has been paid return True, otherwise return False

def knapsack_greedy(W,D,v,w):
    value = v.copy()
    weight = w.copy()
    ratio = v/w 
    # sort ratio will be me the indices of the ratio array 
    sort_ratio = np.argsort(ratio)
    # Descending order
    sort_ratio = sort_ratio[::-1]
    curr = 0 
    for i in sort_ratio: 
        value[curr] = v[i]
        weight[curr] = w[i]
        curr+=1
    for i in range(len(weight)):
        if D<=0: 
            return True
        elif weight[i] <= W: 
            W = W-weight[i]
            D = D-value[i]
    return False 
# 
    
# randomized algorithm 
#sort the items randomly, then go through the list of items
# adding the item to the knapsack if there is still room for it. 
# If at the end of the debt has been paid, return TRUE
# other wise try another random order
# keep trying for a fixed number of items, if none of the 
# orderings results in a solution return FALSE
def random_knapsack(W,D,v,w,steps): 
    value = v.copy()
    weight = w.copy() 
    orig_weight = W
    orig_debt = D
    for i in range(steps):
        orig_weight=W
        orig_debt=D
        random_value = np.random.permutation(value)
        random_weight = np.zeros(len(random_value))
    # find the indices of weight that correlate to the random_value
        for i in range(len(random_value)):
            for j in range(len(value)): 
                if random_value[i] == value[j]: 
                    random_weight[i] = weight[j]
        for k in range(len(random_weight)):
            if random_weight[k] <= orig_weight: 
                orig_weight = orig_weight-random_weight[k]
                orig_debt = orig_debt-random_value[k]
            if orig_debt<=0: 
                return True 
    return False 
            
    
    
    

#largers problems with greedy and random 
# smaller problems with backtracking 
    

    




def main(): 
    W =  35
    D = 40
    w = np.array([10,14,20,5])
    v = np.array([4,37,9,10])
#    print("Random algorithm with example: ", random_knapsack(W,D,v,w,5000))

    
    
    
    
    
    #first
    W =  35
    D = 270
    w = np.array([10,  6, 10,  6, 14,  8,  5, 13,  4,  1])
    v = np.array([39, 47, 47, 29, 71, 22, 50, 29, 51, 20])
    start = time.time()
#    print("Backtracking with first example: ",knapsack(W,D,v,w))
#    print("Greedy algorithm with first example: ", knapsack_greedy(W,D,v,w))

    print("Random algorithm with first example: ", random_knapsack(W,D,v,w,5000))
    print("end time", time.time()-start)

#    #second
#    W =  10
#    D = 130
#    w = np.array([10,  6, 10,  6, 14,  8,  5, 13,  4,  1])
#    v = np.array([39, 47, 47, 29, 71, 22, 50, 29, 51, 20])
#    print("Backtracking with second example: ", knapsack(W,D,v,w))
#    print("Greedy algorithm with second example:",knapsack_greedy(W,D,v,w))
#    print("Random algorithm with second example: ", random_knapsack(W,D,v,w,5000))
#
#    
#    #third
#    W = 102
#    D = 404
#    w = np.array([10,  8,  5,  6,  9, 13, 13, 14, 13, 14,  6, 11, 12,  5, 13, 11,  9,
#       10, 14,  9])
#    v = np.array([47, 15,  7, 17, 29, 12, 45, 24, 26, 10, 37, 38, 14, 35, 44, 37, 27,
#       45, 36, 40])
#    print("Backtracking with third example: ", knapsack(W,D,v,w))
#    print("Greedy algorithm with third example:",knapsack_greedy(W,D,v,w))
#    print("Random algorithm with third example: ", random_knapsack(W,D,v,w,15000))
#
#
#
#    
#    
#    
#    #fourth
#    W = 150
#    D = 600
#    w = np.array([10, 14,  4,  5,  8, 12,  5,  7,  7, 11,  9,  5, 10, 14,  4,  4, 14,
#        7,  8,  9])
#    v = np.array( [39, 49, 47, 40, 20, 27, 31, 34, 17, 10, 29, 36, 41, 48, 45, 24, 15,
#       17, 14, 40])
#    print("Greedy algorithm with fourth example:",knapsack_greedy(W,D,v,w))
#    print("Random algorithm with fourth example: ", random_knapsack(W,D,v,w,5000))
#
#    
#    
#    #fifth
#    W = 200
#    D = 960
#    w = np.array([ 8, 13, 13,  9,  5, 14, 13,  4,  8,  7, 13,  8, 12,  9, 13,  8,  5,
#        9,  5,  7,  4,  7, 13, 13,  6,  8,  4,  5,  9, 10,  5,  4,  6, 10,
#        7,  9, 13, 14, 12,  5, 10,  7,  9, 12,  9, 10,  5,  8, 11,  9])
#    v = np.array([21, 26, 25, 23, 42, 32, 45, 33, 40, 20, 44, 13,  9, 31, 47, 21, 31,
#       18, 41, 36, 32, 43, 20, 40, 23, 16, 10, 44, 38,  6, 11, 13, 43,  7,
#       35, 21,  7, 25, 47, 34, 33, 46, 26, 17, 23, 28, 42, 16, 28, 30])
#    print("Greedy algorithm with fifth example:",knapsack_greedy(W,D,v,w))
#    print("Random algorithm with fifth example: ", random_knapsack(W,D,v,w,5000))
#
#
#

    
    
#      
    
    
    
    
    
main()
    

     






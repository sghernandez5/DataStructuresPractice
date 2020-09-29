# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 16:27:37 2020

@author: Sofia
"""
import numpy as np
import graph_AL as graphAL
import graph_AM as graphAM
import graph_EL as graphEL
import random 
import time 



def matrix(s):
    f = open(s, 'r', encoding = "utf8")
    lines = f.readlines()
    f.close()
    f = open(s, 'r', encoding = "utf8")
    nums = f.read()
    f.close()
    size = get_size(nums,lines)
    G = graphAM.Graph(size)        
    for i in lines: 
        nums = i.split()
        G.insert_edge(int(nums[0]),int(nums[1]),1)
    return G
        


def get_size(text,lines):
    L = []
    for i in lines:
        num = i.split()
        num = [int(integer) for integer in num]
        L.append(num)
    # the true size is not the total length of the list but 
    # the last destination, at the end of the list, +1 inclusive
    return L[-1][1]+1


def adjacency_list(s):
    f = open(s, 'r', encoding = "utf8")
    #read lines 
    lines = f.readlines()
    f.close()
    f = open(s, 'r', encoding = "utf8")
    #read text 
    nums = f.read()
    f.close()
    # get size for the adjaceny list 
    size = get_size(nums,lines)
    G = graphAL.Graph(size)
    
    for i in lines: 
        digit_list = i.split()
        G.insert_edge(int(digit_list[0]),int(digit_list[1]),1)
    return G


            
def random_walk(g, steps = 50000): 
    random_vertex = random.randint(0,len(g.al))
    visited_list = np.zeros(((len(g.al)),),dtype = int)
    for i in range(steps): 
        visited_list[random_vertex] += 1
        neighbors = g.al[random_vertex]
        if len(neighbors) == 0: 
            neighbors = g.al
        else:
            # set u as the random vertex within my list of neighbors 
            random_element = random.randint(0,len(neighbors)-1)
            # get the value of index random element 
            r = neighbors[random_element]
            # set random_vertes as the destination from r
            random_vertex = r.dest
    p = visited_list/steps      
    return p

    
def iterative(g): 
    p = np.zeros(len(g.am))
    # populate p with how many visits per vertex
    for i in range(len(p)): 
         p[i]=1/len(p)
    out_degrees = []
    for r in range(len(g.am)):
        count = 0
        for s in range(len(g.am[r])):
            if g.am[r][s] != -1:
                count+=1
        out_degrees.insert(r,count)
        
    # populate T based on out_degrees
    T = np.zeros((len(g.am), len(g.am))) # t is a nxn array 
    for i in range(len(T)):
        for j in range(len(T[i])):
            if  out_degrees[i] == 0: 
                T[i][j] = 1/ len(g.am)  #T[i,|V|-1] = 1/|V|
            elif g.am[i][j] == 1:
                T[i][j] = 1/out_degrees[i]
            else: 
                T[i][j] = 0
    #convergence
    for c in range(1000):           
        p = np.dot(p,T)         
    return p
            


def most_important(g):
    for i in range(10): 
        p = random_walk(g)
        mvp = 0 
        for j in range(len(p)): 
            if p[j] > mvp: 
                mvp = p[j]
                vertex = j
        print("Iteration ", i+1," most important vertex ", vertex," with p = ", p[vertex])
        #delete all the edges within the g.al[vertex]
        for x in range(len(g.al[vertex])): 
            g.delete_edge_(vertex,x)
        #delete at any vertex the edges associated with the most important vertex
        for y in range(len(g.al)): 
            for z in range(len(g.al[y])): 
                if z < len(g.al[y]) and g.al[y][z].dest == vertex:
                    g.delete_edge_(y,vertex)
    return    


def most_important_iter(m):
    for i in range(10): 
        p = iterative(m)
        mvp = 0 
        vertex = 0 
        for j in range(len(p)): 
            if p[j] > mvp: 
                mvp = p[j]
                vertex = j
        print("Iteration ", i+1," most important vertex ", vertex," with p = ", p[vertex])
        #delete all the edges within the g.al[vertex]
        for x in range(len(m.am[vertex])): 
            m.delete_edge(vertex,x)
        #delete at any vertex the edges associated with the most important vertex
        for y in range(len(m.am)): 
            for z in range(len(m.am[y])): 
                if z < len(m.am[y]) and m.am[y][z] != -1:
                    m.delete_edge(y,vertex)
    return 

def main(): 
#    g = adjacency_list("facebook_combined.txt")
#    g.display()
#    most_important(g)
   
    
    
#    random_walk(g)
     m = matrix("facebook_combined.txt")
#    m.display()
     start = time.time()
     most_important_iter(m)
     print("Total", time.time()- start)

  
                
main()
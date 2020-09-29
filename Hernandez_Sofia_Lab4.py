# Implementation of binary search trees using lists
#author: Sofia Hernandez
# CS 2302 Lab 4

import matplotlib.pyplot as plt
import numpy as np
import math 



# T(n) = 2T(n-1)+1
# O (2^n)
#ex: 2^2-1 = 3
def size(T):
    count = 0
    if T == None: 
        return count 
    #count each node
    if T[0] != None: 
        count +=1
    #go left and right of the tree
    if T[1] != None: 
        count = count + size(T[1])
    if T[2] != None: 
        count = count + size(T[2])
    return count





# T(n) = T(n/2)+1 
# log(n) + 1
# O(log(n))
def minimum(T):
    if T == None: 
        return -math.inf
    smallest = None
    # go to the left of the BST
    if T[1]!= None: 
        smallest = minimum(T[1]) 
    else:
        #if there is no left then we dont make the call and return the 
        # current node
        return T[0]
    return smallest




# T(n) = T(n/2)+1 
# log(n) + 1
# O(log(n))
def maximum(T):
    if T== None: 
        return 
    largest = None
    # go to the right of the BST
    if T[2] != None: 
        largest = maximum(T[2])
    else: 
        #if there is no right then we dont make the call and return the 
        # current node
        return T[0]
    return largest





# T(n) = 2T(n/2)+1
# n ^log2(2)
# O(n)   
def height(T):
    hleft =0
    hright =0 
    if T == None: 
        return -1 
    else: 
        #keep track of the largest height 
        hleft =  height(T[1])
        hright = height (T[2])
    # return the largest height as that is the true height of the BST
    if hleft > hright:
        return hleft+1 
    return hright+1






#T(n)= T(n/2) +1
#n^0 * log(n)
#O(log(n))
def inTree(T,i):
    if T == None: 
        return False
    if T[0] == i: 
        return True
    #to check if i in the tree we can make the recursive call to work 
    # as we are checking the tree by hand, example
    #is i less than T[0] then we go left and vice versa
    if i <T[0]:
        return inTree(T[1],i)
    if i > T[0]: 
        return inTree(T[2],i)
  




# T(n) 
# the list lenght is T, so T(n) to go through the while loop      
def printByLevel(T): 
    if T == None: 
        return 
    Q = [T]
    
    while len(Q)>0:
        T = Q.pop(0)
        if T!=None:
            #prints in order 
            print(T[0],end = ' ')
            #appends left to right, by level
            Q.append(T[1])
            Q.append(T[2])
   
    
    
    
# 2T(n-1)+1
# O(2^n)          
def tree2List(T):
    L =  [] 
    if T == None: 
        return L
    # in order tree 2 list
    # Left, root, Right
    if T[1] != None:
        L = L + tree2List(T[1])
    L.append(T[0])
    if T[2] != None: 
        L = L + tree2List(T[2])
    return L 




#2T(n-1)+1
# O(2^n)
def leaves(T):
    if T == None: 
        return 
    L = []
    # the 'node' is a leaf it it contains no pointer or T[1] AND T[2]
    if T[1] is None and T[2] is None: 
        L.append(T[0])
    # we go the left and right subtree
    if T[1] != None: 
        L = L + leaves(T[1])
    if T[2] != None: 
        L = L + leaves(T[2])
    return L 
 



# T(n) = 2T(n-1)+1
# O(2^n)
def itemsAtDepthD(T,d):
    if T==None:
        return []
    #each recurisve call we reach the base case and items at depth D
    if d == 0:
        return [T[0]]
    return itemsAtDepthD(T[1],d-1) + itemsAtDepthD(T[2],d-1)

# T(n/2)+1
#O(log(n))
def depthOfK(T,k):
    if T==None:
        return -1
    if T[0]==k:
        return 0
    #check the left first  based is k < T[0]
    child = T[1]
    # if not we make the recursive call to the right, T[2]
    if T[0]<k:
        child = T[2]
    d = depthOfK(child,k)
    #returns the depth when k is found
    if d>=0:
        d+=1
    return d


# 2T(n-1)+1
# O(2^n)
def draw2(T,ax, x0, y0, delta_x, delta_y):
    if T == None: 
        return 
    #draws left and right of the tree
    if T[1] !=  None:
        ax.plot([x0-delta_x,x0],[y0-delta_y,y0],linewidth=1,color='k')
        draw2(T[1],ax, x0-delta_x, y0-delta_y, delta_x/2, delta_y)        
    if T[2] !=  None:
        ax.plot([x0+delta_x,x0],[y0-delta_y,y0],linewidth=1,color='k')
        draw2(T[2],ax, x0+delta_x, y0-delta_y, delta_x/2, delta_y)
    ax.text(x0,y0, str(T[0]), size=14,ha="center", va="center",bbox=dict(facecolor='w',boxstyle="circle"))

#1+2^n 
# O(2^n)
def draw(T):

    if T != None:
        fig, ax = plt.subplots()
        draw2(T,ax, 0, 0, 1000, 120)  #O(2^n)
        ax.axis('off')
        plt.show()
   
         
def insert(T,newItem): # Insert newItem to BST T
    if T == None:  # T is empty
        T = [newItem,None,None]
    else:
        if newItem< T[0]:
            T[1] = insert(T[1],newItem) # Insert newItem in left subtree
        else:
            T[2] = insert(T[2],newItem) # Insert newItem in right subtree
    return T

def inOrder(T):
    if T!=None:
        inOrder(T[1])
        print(T[0],end=' ')
        inOrder(T[2])
    
if __name__ == "__main__":
    A =[11, 6, 7, 16, 17, 2, 4, 18, 14, 8, 15, 1, 20, 13]  
    B = []
    C = [2]           
    D = [0,2]
    E = [2,0,5,4,6,7]
    
    T = None
    Z = None
    X = None
    Y = None
    U = None

    for a in A:
        T = insert(T,a)  
    for b in B: 
        Z = insert (Z,b)
    for c in C: 
        X = insert(X,c)
    for d in D: 
        Y = insert(Y,d)
    for e in E: 
        U = insert(U,e)
        
    print("************************")
    print("This is the size:",size(Y))
    print("************************")
    print("Min ", minimum(Y))
    print("************************")
    print("Max", maximum(Y))
    print("************************")
    print("Height ", height(Y))
    print("************************")
    print("inTree: ", inTree(Y,0))
    print("************************")
    printByLevel(Y)
    print("************************")
    print(tree2List(Y))
    print("************************")
    print("Leaves", leaves(Y))
    print("************************")
    print("At depth: " , itemsAtDepthD(Y,0))
    print("************************")
    print("Depth of K: " , depthOfK(Y,20))
    print("************************")
    draw(Z)
   
    
    
    
    
    



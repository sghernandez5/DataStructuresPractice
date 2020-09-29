
# Class: [CS2302] Data Structures
# Assignment: Lab 1 
# Authors: Sofia Hernandez <sghernandez5@miners.utep.edu>
# Last Modified: January 30, 2020

import numpy as np
import matplotlib.pyplot as plt
import math

def circle(center,rad):
    # Returns the coordinates of the points in a circle given center and radius
    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    return x,y

def draw_squares(ax,n,p,w):
    if n>0:
        ax.plot(p[:,0],p[:,1],linewidth=0.5,color='k') 
        # corresponding points, to p 
        i1 = [1,2,3,0,1]
        #q puts the fist coordinate of the new square and follows through
        q = p*(1-w) + p[i1]*w  
        draw_squares(ax,n-1,q,w)

def draw_four_circles(ax,n,center,radius):
    if n>0:
        x,y = circle(center,radius)
        ax.plot(x,y,linewidth=0.5,color='red')
        draw_four_circles(ax,n-1,[center[0],center[1]+radius],radius/2)
        draw_four_circles(ax,n-1,[center[0],center[1]-radius],radius/2)
#        draw_four_circles(ax,n-1,[center[0]+radius,center[1]],radius/2)
#        draw_four_circles(ax,n-1,[center[0]-radius,center[1]],radius/2)
        
        
        

        
def draw_orbit_circle(ax,n,center,radius):
    if n>1:
        x,y = circle(center,radius)
        ax.plot(x,y,linewidth=1.0,color='blue')
        draw_orbit_circle(ax,n-1,[center[0],center[0]],radius/(3/2))
            
def draw_triangles(ax,n,p,w):
    if n>0:
        ax.plot(p[:,0],p[:,1],linewidth=0.5,color='purple') 
        # will need four to close the triangle
        #indices of the row shifted up to change coordinates, 
        i1 = [1,2,3,1]
        #print("THIS IS P",p)
        #the equation below will change the coordinates of the triangle 
        # i1 is what i will multiply to shift the coordiantes of p, * w to get a smaller triangle
        # p*w we get half of the p coordinates so 500,1000 goes to [250,500]
        q = p*w + (p[i1])*w
        draw_triangles(ax,n-1,q,w)
        
def pyramid(ax,n,p,w):
    if n>0:
        ax.plot(p[:,0],p[:,1],linewidth=0.5,color='red') 
        #having a copy of p we can modify and 1000 to get thr right most 
        # coordinate of the right most triangle
        p*=w
        q = p.copy()
        r = p.copy()
        q[:,0] += 500
        q[:,1] += 250
        r[:,0] += 0
        r[:,1] += 250
        
        q[:,0]-250
        r[:,0]+250
        
        
        
        pyramid(ax,n-1,r,w)
        pyramid(ax,n-1,q,w)
        
def waffles(ax,n,p,w):
    if n>0:
        ax.plot(p[:,0],p[:,1],linewidth=1,color='purple') # Draw rectangle
        p = p*w
        left  =p.copy()
        right = p.copy()
        top = p.copy()
        
        left[:,0]+=750
        left[:,1]-=250
        right[:,0]-=250
        right[:,1]-=250
        top[:,0]+=250
        top[:,1]+=750
        
        waffles(ax,n-1,left,w)
        waffles(ax,n-1,right,w)
        waffles(ax,n-1,top,w)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#     if n>0:
#        ax.plot(p[:,0],p[:,1],linewidth=0.5,color='purple')
#    #my first square center is [500,500] the right point is [1000,0]
#        p = p*w
#        r = p.copy()
##        q = p.copy()
##        l = p.copy()
#        
#        p[:,0]=p[:,0]+250
#        p[:,1]=p[:,1]+750
#         # q = bottom right square
##        q = q + 750
#        # r = bottom left sqaure
#        r[:,0] = r[:,0]+ 250
#        r[:,1] = r[:,1]-250
#        # l modifies the top left quare
##        l[:,0] = l[:,0]-250
##        l[:,1] = l[:,1]+750
#        
#        waffles(ax,n-1,p-500,w)
#        waffles(ax,n-1,r+500 ,w)
##        waffles(ax,n-1,q,w)
##        waffles(ax,n-1,l,w)
        
def binary_tree(ax,n,p,w):
    if n>0:
        ax.plot(p[:,0],p[:,1],linewidth=2,color='orange')
        r = p.copy() *w
        q = p.copy() *w
        
        #right subtree
        r[:,0] = r[:,0]+1
        
        #left subtree
        q[:,0] = q[:,0]-1
        
        q[:,1], r[:,1] = q[:,1]-.5, r[:,1]-.5 # ys remain negative 
        
        binary_tree(ax,n-1,r,w)
        binary_tree(ax,n-1,q,w)

def pecan_tree(ax,n,p,w): 
    if n>0: 
        ax.plot(p[:,0],p[:,1],linewidth=2,color='green')
        r = p.copy()
        r = r*w
        
        # right subtree
        #add unto the original line the new created line for the right 
        # 
        print("this is r",r)
        r[:,1] = r[:,1] +.5
        
        r[:,0] = r[:,0] + .5
        print("this is mod r",r)
        
#        r = r *     
        #switch the left line and flip it 
        
        pecan_tree(ax, n-1,r,w)

        
    
        


if __name__ == "__main__":  
    
    plt.close("all") # Close all figures
    
    orig_size = 1000.0
    p = np.array([[0,0],[0,orig_size],[orig_size,orig_size],[orig_size,0],[0,0]])


#    #by diving the radius we are creating a smaller circle
#    fig, ax = plt.subplots() 
#    draw_orbit_circle(ax, 4, [0,0], 100)
#    ax.set_aspect(1.0)
#    ax.axis('off')
#    plt.show()
#    fig.savefig('orbit_a.png')
#    
#    
#    fig, ax = plt.subplots() 
#    draw_orbit_circle(ax, 7, [0,0], 100)
#    ax.set_aspect(1.0)
#    ax.axis('off')
#    plt.show()
#    fig.savefig('orbit_b.png')
#    
#    fig, ax = plt.subplots() 
#    draw_orbit_circle(ax, 13, [0,0], 100)
#    ax.set_aspect(1.0)
#    ax.axis('off')
#    plt.show()
#    fig.savefig('orbit_c.png')
#    
#   # triangles method 
#    fig, ax = plt.subplots()
    k= np.array([[500,orig_size],[orig_size,0],[0,0],[500,orig_size]])
#    draw_triangles(ax,3,k,(1/2))
#    ax.set_aspect(1.0)
#    ax.axis('off') 
#    plt.show()
#    fig.savefig('trianglesa.png')
#    
#    fig, ax = plt.subplots()
#    draw_triangles(ax,6,k,(1/2))
#    ax.set_aspect(1.0)
#    ax.axis('off') 
#    plt.show()
#    fig.savefig('trianglesb.png')
#    
#    fig, ax = plt.subplots()
#    draw_triangles(ax,9,k,(1/2))
#    ax.set_aspect(1.0)
#    ax.axis('off') 
#    plt.show()
#    fig.savefig('trianglesc.png')
#    
#    fig, ax = plt.subplots()
#    r = np.array([[0,0],[500,0],[250,500],[0,0]])
#    pyramid(ax,8,k,(1/2))
#    ax.set_aspect(1.0)
#    ax.axis('off') 
#    plt.show()
#    fig.savefig('pyramida.png')
#    
#    fig, ax = plt.subplots()
#    r = np.array([[0,0],[500,0],[250,500],[0,0]])
#    pyramid(ax,4,k,(1/2))
#    ax.set_aspect(1.0)
#    ax.axis('off') 
#    plt.show()
#    fig.savefig('pyramidb.png')
#    
#    fig, ax = plt.subplots()
#    r = np.array([[0,0],[500,0],[250,500],[0,0]])
#    pyramid(ax,6,k,(1/2))
#    ax.set_aspect(1.0)
#    ax.axis('off') 
#    plt.show()
#    fig.savefig('pyramidc.png')
#    
#    #waffles 
#    fig, ax = plt.subplots()
#    square = np.array([[0,0],[1000,0],[1000,1000],[0,1000],[0,0]])
#    waffles(ax,2,square,(1/2))
#    ax.set_aspect(1.0)
#    ax.axis('off')
#    plt.show()
#    fig.savefig('wafflesa.png')
#    
#    #waffles 
#    fig, ax = plt.subplots()
#    square = np.array([[0,0],[1000,0],[1000,1000],[0,1000],[0,0]])
#    waffles(ax,3,square,(1/2))
#    ax.set_aspect(1.0)
#    ax.axis('off')
#    plt.show()
#    fig.savefig('wafflesb.png')
#    
    #waffles 
    fig, ax = plt.subplots()
    square = np.array([[0,0],[1000,0],[1000,1000],[0,1000],[0,0]])
    waffles(ax,6,square,(1/2))
    ax.set_aspect(1.0)
    ax.axis('on')
    plt.show()
    fig.savefig('wafflesc.png')
#    
#    #binary tree
#    fig, ax = plt.subplots()
#    start_point = np.array([[-1,0],[0,1],[1,0]])
#    binary_tree(ax,3,start_point,.5)
#    ax.set_aspect(1.0)
#    ax.axis('off')
#    plt.show()
#    fig.savefig('treeA.png')
#    
#    #binary tree
#    fig, ax = plt.subplots()
#    start_point = np.array([[-1,0],[0,1],[1,0]])
#    binary_tree(ax,4,start_point,.5)
#    ax.set_aspect(1.0)
#    ax.axis('off')
#    plt.show()
#    fig.savefig('treeA.png')
#    
#    #binary tree
#    fig, ax = plt.subplots()
#    start_point = np.array([[-1,0],[0,1],[1,0]])
#    binary_tree(ax,6,start_point,.5)
#    ax.set_aspect(1.0)
#    ax.axis('off')
#    plt.show()
#    fig.savefig('treeA.png')
#    
#    
#    #pecan tree
#    fig, ax = plt.subplots()
#    start_line = np.array([[1,0],[1,1]])
#    pecan_tree(ax,2,start_line,.5)
#    ax.set_aspect(1.0)
#    ax.axis('on')
#    plt.show()
#    fig.savefig('pecanA.png')
#    
    
    
    

    
# Code to implement and display singly-linked lists
# Programmed by Olac Fuentes
# Last modified February 17, 2020
# Author: Sofia Hernandez
# CS 2302
# Lab 3 

import matplotlib.pyplot as plt
import numpy as np
import math

class ListNode:
    # Constructor
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class List:
    # Constructor. Creates empty list
    def __init__(self):
        self.head = None
        self.tail = None

    def print(self):
        t = self.head
        print('[',end ='')
        while t is not None:
            print(t.data,end='')
            t = t.next
            if t!= None:
                print(', ',end='')
        print(']')

    def append(self,x):
        if self.head is None: #List is empty
            self.head = ListNode(x)
            self.tail = self.head
        else:
            self.tail.next = ListNode(x)
            self.tail = self.tail.next

    def extend(self,python_list):
        for d in python_list:
            self.append(d)
            

    def insert(self,i,x): 
        #if the list is empty we still insert the node 
        if self.head == None: 
            self.head = ListNode(x)
            self.tail = self.head
        else: 
            #if not we insert item x at index i 
            temp = self.head
            node_position = 0
            #before we go to our while we check if i
            # is the head index
            if i == 0: 
                self.head = ListNode(x)
                self.head.next = temp
            else:
                # t will be one step higher than temp
                t = temp.next
                while node_position != i:
                    #insert the new node if the new node is after tail
                    if  temp == self.tail and t == None:
                        temp.next = ListNode(x)
                        self.tail = temp.next
                        break
                    if node_position == i-1: 
                        temp.next = ListNode(x)
                        temp.next.next = t
                        break 
                    node_position+=1
                    t = t.next
                    temp = temp.next
          
            
     
    def remove(self,x): 
        if self.head != None and self.tail != None:
            t = self.head
            tail = self.tail 
            # if my data matches x immediately then I remove the head 
            # and set my next pointer as my head
            if t.data == x :
                self.head = t.next 
                #if it is only one node then we update the tail too 
                if t.next == None: 
                    self.tail = t.next
            # if not we check through the list if x is included 
            else:
                t = self.head 
                while t != None and t.next!= None: 
                    if t.next == None: 
                        raise ValueError("Value is not on list")
                        break
                    if t.next == tail and tail.data == x: 
                        self.tail = t
                        t.next = None
                        break
                    if t.next.data == x: 
                        t.next = t.next.next
                        break 
                    t = t.next 
               

    
    def pop(self, i = None): 
        if self.head != None and self.tail != None: 
            t = self.head
            if i == 0: 
                self.head = t.next 
                return t.data
          
            else: 
                position = 0
                # if there is no value given I immediately pop the tail
                # I still need to go through the list to pop the tail 
                if i == None: 
                    while t != None: 
                        if t.next == self.tail and i==None:
                            last = t.next.data
                            self.tail = t
                            t.next = None
                            return last
                        t = t.next
                else:   
                    # i need  one temp to keep track of the one i will pop and make sure i return 
                    #the value that I popped
                    while t.next != None and position<i:
                         #check if it is the tail index
                        if t.next == self.tail and position == i-1:
                            last = t.next.data
                            self.tail = t
                            t.next = None
                            return last
                        #check if it the index is within the list and not tail index
                        if position == i-1: 
                            last = t.next.data
                            t.next = t.next.next 
                            return last
                        t = t.next 
                        position +=1
                    #if the index given is bigger than the list length i return a value error 
                    raise ValueError("Index is out of bounds for the list, cannot pop.")


    
    def clear(self): 
        self.head = None
        self.tail = None
        
    def index (self,x,start = 0,end = math.inf):
        # set head to smallest value which will be 0 
       if self.head != None:
           t = self.head
           index = 0 
           # my start has to be always less than end, if the user passes a larger value for start and 
           #end then a Value Error will appear 
           while t!= None and start < end:
               if  t == self.tail and t.data is not x:
                   raise ValueError(" There is no such item in the list")
                   break
               if t.data ==x and index >= start and index < end :
                   return index
               t = t.next 
               index+=1
           raise ValueError(" Start cannot be larger than end") 

                    
    
    def count(self,x):
        count = 0 
        if self.head != None: 
            t = self.head
            while t!= None: 
                if t.data == x: 
                    count +=1
                t = t.next
            return count
        
    def sort(self):
        if self.head != None: 
            t = self.head
            #outer while loops through the list until unsorted == False 
            # if false then the list is sorted 
            while True: 
                unsorted = False
                # i need to reset t as my head else it wont reorder the next time 
                #it is called 
                t = self.head
                while t.next != None: 
                    # swap nodes
                    if t.data > t.next.data:
                        # since i swapped unsorted becomes True meaning the list is unsorted
                        # because the first node is larger than the next node
                        unsorted  = True
                        temp = t.data
                        t.data = t.next.data
                        t.next.data = temp
                        t = t.next
                    # move temp
                    else:
                        #else i move
                        t = t.next
                # once my inner loop is finished i check if unsorted is true, meaning it
                # is stil unsorted else else i order again with the inner while loop
                if unsorted == False:
                    break

    def reverse(self):
        if self.head != None: 
            t = self.head
            #if it is one node
            if t.next == None: 
                self.head.data = self.head.data
                self.tail.data = self.tail.data
                return
            #reverse in place if two nodes
            if t== self.head and t.next == self.tail: 
                self.head.data, self.tail.data = self.tail.data, self.head.data
            else: 
#                # to keep track of the data 
#                # and reverse in place we need previous and next
                prev = self.head
                t = prev.next
                next_node = self.tail
                #we need t to reach the next_node, 
                #until then the loo[ stops 
                while t!= next_node :
                    # when we reach this case, t will be be before next_node
                    # so we know we can swap both the tail and head,
                    # we then can update our pointer
                    # at some point, prev and next will be pointing to the
                    #same node which will stop the loop cause 
                    # we then know everything has been reversed
                    if t.next == next_node:
                        prev.data, next_node.data = next_node.data, prev.data
                        prev = prev.next 
                        next_node = t
                        t = prev.next
                        #at some point for even number of nodes, t and next will point at the same node
                        # so we know we can just swap the data and break
                        if t== next_node:
                            next_node.data, prev.data = prev.data,next_node.data
                            return
                    # this case will be for odd number of nodes when prev reaches next_node
                    if prev == next_node:
                        return
                    if t.next != next_node:
                        t = t.next
                        
                     
                    
                
    def copy(self):
       return self
#        if self.head != None: 
#            new_ll = List()
#            t = self.head
#            while t != None: 
#                if new_ll.head == None: 
#                    new_ll.head = ListNode(t.data)
#                    #if there is only one node on the original list 
#                    if t.next == None: 
#                        new_ll.tail = new_ll.head 
#                        break 
#                    temp = new_ll.head
#                    t = t.next
#                else: 
#                    temp.next = ListNode(t.data)
#                    # I was missing this line :()
#                    new_ll.tail = temp.next
#                    t = t.next
#                    temp = temp.next
#        return new_ll
        

    def _rectangle(self,x0,y0,dx,dy):
        # Returns the coordinates of the corners of a rectangle
        # with bottom-left corner (x0,y0), dx width and dy height
        x = [x0,x0+dx,x0+dx,x0,x0]
        y = [y0,y0,y0+dy,y0+dy,y0]
        return x,y

    def draw(self,figure_name=' '):
        # Assumes the list contains no loops
        fig, ax = plt.subplots()
        x, y = self._rectangle(0,0,20,20)
        ax.plot(x,y,linewidth=1,color='k')
        ax.plot([0,20],[10,10],linewidth=1,color='k')
        ax.text(-2,15, 'head', size=10,ha="right", va="center")
        ax.text(-2,5, 'tail', size=10,ha="right", va="center")
        t = self.head
        x0 = 40
        while t !=None:
            x, y = self._rectangle(x0,0,30,20)
            ax.plot(x,y,linewidth=1,color='k')
            ax.plot([x0+15,x0+15],[0,20],linewidth=1,color='k')
            ax.text(x0+7,10, str(t.data), size=10,ha="center", va="center")
            if t.next == None:
                ax.text(x0+22,10, '/', size=15,ha="center", va="center")
            else:
                ax.plot([x0+22,x0+40],[10,10],linewidth=1,color='k')
                ax.plot([x0+37,x0+40,x0+37],[7,10,13],linewidth=1,color='k')
            t = t.next
            x0 = x0+40
        if self.head == None:
            ax.text(12,15, '/', size=10,ha="center", va="center")
        else:
            ax.plot([10,40],[15,15],linewidth=1,color='k')
            ax.plot([37,40,37],[12,15,18],linewidth=1,color='k')

        if self.tail == None:
            ax.text(12,5, '/', size=10,ha="center", va="center")
        else:
            xt = 40
            t = self.head
            while t!= self.tail:
                t = t.next
                xt+=40
            ax.plot([10,10,xt+15,xt+15],[5,-10,-10,0],linewidth=1,color='k')
            ax.plot([xt+12,xt+15,xt+18],[-3,0,-3],linewidth=1,color='k')

        ax.set_title(figure_name)
        ax.set_aspect(1.0)
        ax.axis('off')
        fig.set_size_inches(1.2*(x0+200)/fig.get_dpi(),100/fig.get_dpi())
        plt.show()

if __name__ == "__main__":
    # It won't execute when this file is imported 

    plt.close('all')
#    L1 = List()
#    L1.draw('Empty list')
#    L1.extend(list(np.random.permutation(10)))
#    L1.draw('Unsorted list')
#    L1 = List()
#    L1.extend(list(np.arange(10)))
#    L1.draw('Sorted list')
#    L1.tail = L1.head.next.next
#    L1.draw('Bad list!')
#    L1.tail = None
#    L1.draw('Another bad list!')
    
    print("*******")
    test = List()
    
    test.append(1)
    test.append(2)
    test.append(3)
    test.append(4)
    test.append(5)
    test.append(6)
    test.append(7)
    test.append(8)
#    test.append(9)
#    test.append(10)
#    test.append(11)
#    test.append(12)
    print(test.index(5,2,5))
    test.draw("index")
    

    
    


  

    
    
    
    




# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 13:49:48 2024

@author: Tate
"""

from tabulate import tabulate # Import tabulate to form table
import random # import random to generate random integers

SECONDS_PER_ITEM = 4
OVERHEAD_SECONDS = 30  # Given time intervals
CHECKOUT_TIME = 45

class Queue: # copied queue class
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    
class Register():
    
    def __init__(self):
        self.queue = Queue()
        self.total_customers = 0
        self.total_items = 0
        self.total_idle_time = 0
        self.avg_wait_time = 0
        self.currentCustomer = None
        self.time_remaining = 0
 
    def tick(self) :
        if not(self.idle()):
            self.time_remaining -= 1
            if self.time_remaining <= 0: # If time remaining reaches or falls below 0, 
                self.currentCustomer = None
                
    def idle(self):
        return (self.currentCustomer == None)                
        
    def startNext(self, newCustomer) :
        self.currentCustomer = newCustomer
        self.time_remaining = \
             newCustomer.getStamp()*30 # Simulation, loop, new customer enters a checkout line every 30 seconds

    
class Customer():
    def __init__(self, time) :
        self.timestamp = time
        self.num_items = random.randrange(6,20) # the number of items purchased per customer is between 6 and 20
    
    def getStamp(self) :
        return self.timestamp # Get the timestamp of the job
        
    def getNumItems(self) :
        return self.num_items # Get the number of items
        
    def waitTime(self, currentTime) :
        return currentTime - self.timestamp # Record the wait time for the job

def main():
    
    register_1 = queue.Queue()
    register_2 = queue.Queue()
    register_3 = queue.Queue()
    register_4 = queue.Queue()
    express = queue.Queue()
    # data = [
    #     ["1"],
    #     ["2"],
    #     ["3"]]

    # headers = ["Register", "total customers", "total items", "total idle time (min)", "average wait time (sec)"]

    # table = tabulate(data, headers, tablefmt="grid")
    # print(table)

# main()
    



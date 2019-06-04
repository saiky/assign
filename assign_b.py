"""
description:
    getting total runways

author: Saikat Paul <saikat.it2006@gmail.com>

optional arguments:
  -h, --help show this help message and exit
  -a, --Length of the runway 2
  -b, --Number of different runways available 3
  
example: python assign_b.py 2 3
"""
import os
import argparse


class ProcessorTask:
    
    def __init__(self):
        self.a = ""
        self.b = ""

    def get_args(self):
        ## get from date arument if exists else current date
        parser = argparse.ArgumentParser()
        parser.add_argument("a", help="enter total students i.e 2",type=int)
        parser.add_argument("b", help="enter students group i.e 3",type=int)
        args = parser.parse_args()
        if args.a is not None:
            self.a = args.a
        if args.b is not None:
            self.b = args.b


    def gcd(self, a, b): 
      
        if (a == 0 or b == 0): 
            False

        # base case 
        if (a == b): 
            return a 

        if (a > b):
            return self.gcd(a-b, b)

        return self.gcd(a, b-a)


    def coprime(self, a, b) : 
        return (self.gcd(a, b) == 1)

    def numOfPairs(self, arr, n) : 
        count = 0
      
        for i in range(0, n-1) : 
            for j in range(i+1, n) : 
      
                if (self.coprime(arr[i], arr[j])) : 
                    count = count + 1
      
        return count

    def output_runways(self):
        i = 1
        arr = []
        while i <= self.a:
            arr.append(i)
            i += 1
        self.numOfPairs(arr,self.b)            

if __name__ == "__main__":
    ProcessorTask = ProcessorTask()
    ProcessorTask.get_args()
    print(ProcessorTask.output_runways())

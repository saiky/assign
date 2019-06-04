"""
description:
    getting output the numbers in the sequence

author: Saikat Paul <saikat.it2006@gmail.com>

optional arguments:
  -h, --help show this help message and exit
  -a, --total students 12
  -b, --students group [2, 5]
  
example: python assign_a.py 12 [2,5]
"""
import os
import argparse


class ProcessorTask:
    
    def __init__(self):
        self.a = ""
        self.b = []

    def get_args(self):
        ## get from date arument if exists else current date
        parser = argparse.ArgumentParser()
        parser.add_argument("a", help="enter total students i.e 12",type=int)
        parser.add_argument("b", help="enter students group i.e [2,6]",type=str)
        args = parser.parse_args()
        if args.a is not None:
            self.a = args.a
        if args.b is not None:
        	b = args.b
        	self.b = map(int, b.strip('[]').split(',')) 

    def output_groups(self):
        i = 1
        rolls = []
        output = []
        while i <= self.a:
        	rolls.append(str(i))
        	i += 1
        rolls.sort()

        for i in self.b: 
        	try:
        	    output.append(int(rolls[i-1]))
        	except:
        	    output = "wrong input" 
        return output
            

if __name__ == "__main__":
    ProcessorTask = ProcessorTask()
    ProcessorTask.get_args()
    print(ProcessorTask.output_groups())


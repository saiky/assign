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
from math import gcd as bltin_gcd

class ProcessorTask:
    
    def __init__(self):
        self.a = ""
        self.b = ""

    def get_args(self):
        ## get from date arument if exists else current date
        parser = argparse.ArgumentParser()
        parser.add_argument("a", help="Length of the runway i.e 2",type=int)
        parser.add_argument("b", help="Number of different runways available i.e 3",type=int)
        args = parser.parse_args()
        if args.a is not None:
            self.a = args.a
        if args.b is not None:
            self.b = args.b

    def is_coprime(self, a, b):
        return bltin_gcd(a, b) == 1

    def getCombinations(self, seq):
        combinations = list()
        for i in range(0,len(seq)):
            for j in range(i+1,len(seq)):
                if self.is_coprime(seq[i],seq[j]):
                    combinations.append([seq[i],seq[j]])
                    combinations.append([seq[j],seq[i]])
        return combinations

    def output_runways(self):
        i = 1
        arr = []
        while i <= self.b:
            arr.append(i)
            i += 1
        return len(self.getCombinations(arr))+1

if __name__ == "__main__":
    ProcessorTask = ProcessorTask()
    ProcessorTask.get_args()
    print(ProcessorTask.output_runways())

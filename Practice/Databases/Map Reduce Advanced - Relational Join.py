'''
Task Details
    Platform: HackerRank
    Name: Map Reduce Advanced - Relational Join 
    Link: https://www.hackerrank.com/challenges/map-reduce-advanced-relational-join/problem
'''

import sys
from collections import OrderedDict
class MapReduce:
    def __init__(self):
        self.intermediate = OrderedDict()
        self.result = []
   

    def emitIntermediate(self, key, value):
   	self.intermediate.setdefault(key, [])       
        self.intermediate[key].append(value)

    def emit(self, value):
        self.result.append(value) 

    def execute(self, data, mapper, reducer):
        for record in data:
            mapper(record)

        for key in self.intermediate:
            reducer(key, self.intermediate[key])

        self.result.sort()
        for item in self.result:
            print item

mapReducer = MapReduce()

def mapper(record):
    parts = record.rstrip().split(',')
    result = None
    key = None
    if parts[0] == 'Employee':
        key = parts[2]
        result = ('E,'+parts[1])
    elif parts[0] == 'Department':    
        key = parts[1]
        result = ('D,'+parts[2])
    mapReducer.emitIntermediate(key, result)

    
def get_employee_name(values):
    return [val[2:] for val in values if val[0] == 'E'][0]    
    
def reducer(key, list_of_values):
    emp = get_employee_name(list_of_values)
    dept = None
    
    for val in list_of_values:
        if val[0] == 'D':
            dept = val[2:]
            result = (key, emp, dept)
            mapReducer.emit(result)

if __name__ == '__main__':
  inputData = []
  for line in sys.stdin:
   inputData.append(line)
  mapReducer.execute(inputData, mapper, reducer)
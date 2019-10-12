#deque: list-like container with fast appends and pops on either end
#namedtuple: function for creating tuple subclasses with named fields
from collections import deque, namedtuple

#Make the default value for node distance infinity
infinity = float('inf')

#Define a namedtuple 'Edge'
Edge = namedtuple('Edge', 'start, end, cost', verbose = True)

#Setup a function that returns an edge namedtuple
def make_edge(start, end, cost = 1):
    return Edge(start, end, cost)
    
#Creation of main class
class Metric:
    #Always define __init__ first in a class
    def __init__(self, edges):
        #Should be empty unless an edge is entered incorrectly
        wrong_edges = [e for e in edges if len(e) not in [2,3]]
        #Shows which inputs led to an issue
        if wrong_edges:
            raise ValueError('Wrong edge data input: {}'.format(wrong_edges))
        #(*edge) passes a variable length argument list (*args)
        self.edges = [make_edge(*edge) for edge in edges]    

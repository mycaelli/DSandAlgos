'''
INPUT: 
        queries = [3, 2, 1, 2, 6]
OUTPUT:
        Minimum waiting time queries is executed

EXAMPLE
        INPUT: 
                queries = [3, 2, 1, 2, 6]
        OUTPUT:
                17
        
        Explanation 
                Minimum waiting time -> queries has to be sorted
                [1, 2, 2, 3, 6]
                waiting time for queries[0] to be executed = 0
                waiting time for queries[1] to be executed = 0 + 1
                waiting time for queries[2] to be executed = 0 + 1 + 2 
                waiting time for queries[3] to be executed = 0 + 1 + 2 + 2
                waiting time for queries[4] to be executed = 0 + 1 + 2 + 2 + 3
                Total = 17

O(nlogn) T | O(1) S
'''

def minimumWaitingTime(queries):
    queries.sort()
    prevSum = 0
    minT = 0
    for i in queries:
      minT += prevSum
      prevSum += i
    return minT

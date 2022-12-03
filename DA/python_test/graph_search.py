#граф  
graph = {}

#узлы со списком соседей и стоимостью продвижения к этим соседям 
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2

graph['a'] = {}
graph['a']['fin'] = 1

graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5 

graph['fin'] = {}

print(graph)

infinity = float('inf')
print(infinity)

costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity


parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

processed = []





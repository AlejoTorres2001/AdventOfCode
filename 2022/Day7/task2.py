from task1 import get_data,build_graph,add_weights,Node
TOTAL_DISK_SIZE=70000000
UPDATE_SIZE=30000000

def find_node(graph:list):
  free_space = TOTAL_DISK_SIZE - graph[0].weight
  space_needed = UPDATE_SIZE - free_space
  possible_nodes = [node for node in graph if node.weight >= space_needed]
  return min(possible_nodes, key=lambda node: node.weight)

if __name__ == "__main__":
  graph = []
  data = get_data() 
  build_graph(data,graph)
  add_weights(graph)
  
  print(find_node(graph))

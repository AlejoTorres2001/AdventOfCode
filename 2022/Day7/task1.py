class Node :
    def __init__(self, name, weight,to_nodes=[],from_node=None):
        self.name = name
        self.weight = weight
        self.to_nodes = to_nodes
        self.from_node = from_node
    def set_node_from(self,from_node):
        self.from_node = from_node
    def add_node_to(self,node):
        self.to_nodes.append(node)
        
    def __str__(self):
      return f'Node: {self.name} Weight: {self.weight} From: {self.from_node.name if self.from_node else None} To: {[node.name for node in self.to_nodes]}'
        
        
def get_directive(line_content):
  if line_content[0] == '$' and line_content[1] == 'cd' and line_content[2] != '..':
    return 'NEW_NODE'
  if line_content[0] == '$' and line_content[1] == 'cd' and line_content[2] == '..':
    return 'BACK_TO_PARENT'
  if line_content[0] == '$' and line_content[1] == 'ls':
    return 'READ_COMMAND'
  if line_content[0] != '$' and line_content[0] != 'dir':
    return 'READ_DIR'

def update_weights(graph:list):
  for node in graph[::-1]:
    for node_to in node.to_nodes:
      node.weight += node_to.weight
def sum_weights(graph:list):
  filtered_graph = [node for node in graph if node.weight <= 100000]
  return sum([node.weight for node in filtered_graph])


def get_data():
  with open('./data.txt', 'r') as input:
      return [line.removesuffix('\n') for line in input]

def build_graph(data,graph:list):
  parent_node = None
  for line in data:
    line_content = line.split(' ')
    directive = get_directive(line_content)
    
    if directive == 'NEW_NODE':
      new_node = Node(line_content[2], 0, [], parent_node)
      parent_node.add_node_to(new_node) if parent_node else None
      graph.append(new_node)
      parent_node = new_node
      
    if directive == 'READ_COMMAND':
      pass
    
    if directive == 'READ_DIR':
      parent_node.weight += int(line_content[0]) 
      
    if directive == 'BACK_TO_PARENT':
      parent_node = parent_node.from_node
    
if __name__ == "__main__":
  graph = []
  data = get_data()
  build_graph(data,graph)
  update_weights(graph)
  for node in graph:
    print(node)
  print(sum_weights(graph))

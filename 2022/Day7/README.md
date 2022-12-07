## Day 7 

## Part 1 

The first graph problem! well, at least the first graph-related problem. I have to say this one felt pretty natural to me, probably because using the file system as an example helped me understand the problem.

Although I've said this is a graph problem, there is no need to path-finding algorithms.

Our input data is the output of a console where ````cd```` and ````ls```` commands were run, this sort of unveils the file system we need to work with. our first goal is to find the total size of it by adding up the sizes of the nodes, but because the file system is a tree, we can't just add up the sizes of the nodes, we need to add up the sizes of the nodes and their children.

But first of all, we need a way to sequentially read the input data and commands and somehow decide what action to execute, this here is the main concept of a state machine, and it's a very good fit for this problem.

As always we start by reading and parsing the data 

```python
def get_data():
  with open('./data.txt', 'r') as input:
      return [line.removesuffix('\n') for line in input]
```

The state of our machine will be determined by the current line of our input data, there are only 4 possible states in which our machine can be, and they are:
 - ````NEW_NODE```` means we've just ````cd```` into a new node
 - ````BACK_TO_PARENT```` means we've just ````cd ..```` and we need to go back to the parent node
 - ````READ_COMMAND```` means we've just ran a ````ls```` command and we need to read the next line
 - ````READ_DIR```` means we've just read a file and we need to add it's weight to the current node

```python
def get_directive(line_content):
  if line_content[0] == '$' and line_content[1] == 'cd' and line_content[2] != '..':
    return 'NEW_NODE'
  if line_content[0] == '$' and line_content[1] == 'cd' and line_content[2] == '..':
    return 'BACK_TO_PARENT'
  if line_content[0] == '$' and line_content[1] == 'ls':
    return 'READ_COMMAND'
  if line_content[0] != '$' and line_content[0] != 'dir':
    return 'READ_DIR'
```

Setting these states reduces the complexity of our problem by a lot because we can now focus on the logic of each state.

Let's start with the ````build_graph```` function

```python
def build_graph(data,graph:list):
  parent_node = None
  for line in data:
    line_content = line.split(' ')
    directive = get_directive(line_content)
```
here we are just asking for the directive based on every line of our input data

```python
 if directive == 'NEW_NODE':
      new_node = Node(line_content[2], 0, [], parent_node)
      parent_node.add_node_to(new_node) if parent_node else None
      graph.append(new_node)
      parent_node = new_node
```
the ````NEW_NODE```` state creates a new node with its name, size and parent, updates de adjacency list of the parent node and adds the new node to the graph, finally it becomes the new parent node

````Quick side note: we will  be working with an adjacency list representation of the graph, each node will be an instance of the following Node class````

```python
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
```


The read command state in our machine is useless in this case 


```python
 if directive == 'READ_COMMAND':
      pass
```

The ````BACK_TO_PARENT```` state is pretty simple, it just sets the parent node to the parent of the current node

```python
 if directive == 'BACK_TO_PARENT':
      parent_node = parent_node.from_node
```

The ````READ_DIR```` state is the most important one, it adds the size of the file to the current node and updates the size of the parent node

```python
 if directive == 'READ_DIR':
      parent_node.weight += int(line_content[0]) 
```

With this, we've just built our graph, but now we need to update the weights, at this point, each node is only considering the weight of the files in its directory, but we need to add the weight of the files in the subdirectories as well, so we need to ````traverse the graph```` and update the weights of the nodes

Now here comes the part where this approach might not be the most optimal or the cleanest to some people, we indeed need to traverse the graph to update the weights, but because of the problem's nature and thanks to our adjacency list and Node class we DON'T need to use any path-finding algorithms, we can just traverse the graph using a simple ````for```` loop, the catch here is that we need to traverse if from bottom to top, or from the outer nodes to the Root node, hence we are going to invert our adjacency list

```python
def update_weights(graph:list):
  for node in graph[::-1]:
    for node_to in node.to_nodes:
      node.weight += node_to.weight
```

with this, in place we just need to add up the weights of the nodes in the graph that fit the challenge criteria and we are done

```python
def sum_weights(graph:list):
  filtered_graph = [node for node in graph if node.weight <= 100000]
  return sum([node.weight for node in filtered_graph])
```

```python
if __name__ == "__main__":
  graph = []
  data = get_data()
  build_graph(data,graph)
  update_weights(graph)
  print(sum_weights(graph))
```

## Part 2

Part 2 might seem a bit more complicated at first, but it's actually easier. We are looking for the perfect node, sort of speak that when deleted free-up enough space to fit the system's update


We need to borrow some things from part 1 and define some constants as well
```python
from task1 import get_data,build_graph,update_weights

TOTAL_DISK_SIZE=70000000
UPDATE_SIZE=30000000

``` 
for the ````find_node```` function first we need to know how much free space we actually have in our FS, this we can get by subtracting the total disk size from the sum of the weights of the nodes in the graph which is equivalent to subtracting the weight of the root node ````/````

```python
free_space = TOTAL_DISK_SIZE - graph[0].weight
```
Now we need to know how much space is needed to be freed up to fit the update, this is just the difference between the free space and the update size

```python
space_needed = UPDATE_SIZE - free_space
```

We will find the possible nodes that might fit the criteria by filtering the graph and getting the nodes that have a weight bigger than the space needed

```python
possible_nodes = [node for node in graph if node.weight >= space_needed]
```

From those nodes, we are going to get the smallest of them all

```python
return min(possible_nodes, key=lambda node: node.weight)
```

finally, the complete function looks like this

```python
def find_node(graph:list):
  free_space = TOTAL_DISK_SIZE - graph[0].weight
  space_needed = UPDATE_SIZE - free_space
  possible_nodes = [node for node in graph if node.weight >= space_needed]
  return min(possible_nodes, key=lambda node: node.weight)
```
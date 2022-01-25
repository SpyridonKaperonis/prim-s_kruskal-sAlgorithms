# Project 02

## 44-349 Survey of Algorithms

For this project you will implement both Prim's and Kruskal's algorithm.

### Graph Libraries

If you wish, you may use a preexisting graph library for your language of choice.
Some common/popular graph libraries for various programming languages include:
* `networkx` (Python)
* `JGraphT` (Java)
* `nauty` (C/C++)

You are not required to use one of these libraries; you may instead implement a simple adjacency list or adjacency matrix (the required graph storage is very simple for this project)

### Requirements:

You MUST implement both Prim's and Kruskal's algorithms (you may not use an implementation that is part of a preexisting graph library).
Additionally you should create a way to *either*
* Read in graphs from a file
* Generate random graphs

### Included random graph files
The included files all contain 100 nodes in the graph.  The filename indicates the number of edges in the weighted graph.
Each file has the form of a weighted edge list, where a line in the file is of the form
`n1 n2 w`
meaning there is an edge connecting node `n1` to `n2` with a weight of `w`

You may choose to use these graph files for your timings if you so desire.  
They were generated using `networkx` and Python using guidance from 
* https://networkx.github.io/documentation/stable/reference/generated/networkx.generators.random_graphs.fast_gnp_random_graph.html#networkx.generators.random_graphs.fast_gnp_random_graph
* https://stackoverflow.com/questions/31804117/how-to-create-a-random-networkx-graph-with-random-weights

## Output expectations

You are expected to time your implementations of Prim's and Kruskal's algorithms for various graphs (you may find it easiest to fix the number of vertices and change the number of graphs).
In part 2 of this project you will need to create graphs showing how Prim's and Kruskal's algorithms scale (in performance) for graphs of various sizes.

## Submission
You MUST include all files to run your code in this repository.
If you use Python and `networkx` you may assume the graders have access to the Anaconda python distribution.
If you juse Java you should include your entire project (Netbeans, IntelliJ Idea) with any libraries you choose to use included (or have Maven/Gradle handle it for you).

If you use other languages please provide any run instructions to run your code so the graders/instructor can efficiently run your code.

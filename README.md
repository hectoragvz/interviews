# DSA interview prep w/ Python

as inspired by https://github.com/kdn251/interviews

View "basic" prerequisite video [here](https://www.youtube.com/watch?v=0K_eZGS5NsU), by Neetcode.io.

Definitely read throughout [this](https://haseebq.com/how-to-break-into-tech-job-hunting-and-interviews/) article by Haseeb Qureshi to feel motivated, guided (and pumped!), specially if you come from a non-cs specific background like me.

View basic algorithms/data structures/techniques roadmap [here](https://neetcode.io/roadmap). This is the base for the leetcode folder.


## Data Structures

---
### Arrays
An array, also called a list in other programming languages, is a data structure allowing the storage of values in continuous spaces of memory.
You can store different types of values such as integers, floats, objects or even other arrays (creating 2D or nd arrays) in them.
In PYTHON, lists are implemented as DYNAMIC ARRAYS, meaning you dont´t need to specify the size of the arrays when declaration is performed.

_Time Complexity:_

- Lookup notation by index = O(1)
- Lookup by value = O(n)
- Array traversal = O(n)
- Array insertion = O(n)
- Array deletion = O(n)

### Linked Lists
Best explanation I found on topic (https://www.youtube.com/watch?v=8hly31xKli0) - Intro to data structures section

Contrary to arrays, which store values on continuous memory location, linked lists store values on random memory locations but each of those also store a reference to the next value in memory.
When we add elements for example, we would just need to change the address located in the element prior to the one we are adding.
We don´t need to preallocate space and insertio is easier.

A <em>double link list</em> would have elements store an address for the element before and after their location.

Link lists are not built in for Python, so there is a need to implement them.

_Time Complexity:_

- Add last element = O(1)
- Remove las element = O(n)
- Linked list traversal = O(n)
- Insert/delete at beginning = O(1)
- Insert/delete at an iterator position O(1)
- Lookup by value = O(n)

### Stacks
The stack data structure is a collection of elements that highlight two basic operations: push (adding elements to the stack) and pop (deleting elements from the stack).

Implements the last-In, First-Out approach, also called LIFO, which states the most recently added element will be removed frist from the strucutre.

_Time Complexity:_

- Search = O(n)
- Access = O(n)
- Insert and Delete (push and pop) - O(1)

### Queues
Consider the stack data structure but now, the element we aim to remove is the first on a queue - FIFO (First In, First Out approach). 
We now call push-add as <em>enqueue</em> and pop-delete as <em>dequeue</em>. The end were elements are added is called tail or back of the queue and the end where elements are removed is called as front or head of the queue.
You can think about a queue as a line of customers waiting for a service.

_Time Complexity:_

- Search = O(n)
- Access = O(n)
- Insert and Delete (enqueue and dequeue) - O(1)

<em>Linear</em> data structures (linked lists, queues, and stacks) are formed by sequential data. We can access each element inside of them in a single pass and have as single level of information. In <em>non-linear</em> data structures (trees and graphs), we have multiple levels of information and we may not be able to access all the elements of the ds in a single pass.

### Tree

Trees are non-linear data structures (opposite to those mentioned above). Trees have a collection of entities called nodes, and their objective is to represent the relantionships between these. The connections between nodes are called edges.

The key terms to understand trees are listed in the image below, as posted by <em>geeksforgeeks</em>:

![Tree data structure](./assets/Treedatastructure.png "Tree data structure")

### Binary Tree

In this type of tree, each node may have <em>at most</em> 2 children, or resulting nodes (called binary for this reason). These are the different types of binary trees:

* Full: every node has 0 or 2 children
* Complete: All the levels of the tree except for the last are filled, and are filled from left to right
* Perfect: All internal nodes have 2 children and all leaves are in the same level
* Pathological: Every parent has only 1 child node 

### Binary Search Tree

The traits that define a Binary Search Tree (BST) are:

1. The left subtree of a node contains only nodes with keys or values that are less than the parent´s value.
2. The right subtree of a node contains only nodes with keys or values that are greater than the parent´s value.
3. Both the left and the right subtree must be BSTs.

_Time Complexity:_

- Search = O(log (n))
- Access = O(log (n))
- Insert and Delete = O(log (n))

### Heap

A heap is a complete binary tree which satisfies the heap property: property of a node in which the key of every parent node to be lesser than or equal to OR greater than or equal to the child´s node key.

* min heap / min binary heap
complete binary tree where the key of every parent node is less than or equal to the cild node´s key
* max hap / max binary heap
complete binary tree where the key of every parent node is greater than or equal to the cild node´s key

You can construct binary heap via Python lists:

*  ith element -> list[i]
*  parent of ith element -> (i-1)//2
*  children of ith element -> left: (2*i)+1 / right: (2*i)+2

### Graphs


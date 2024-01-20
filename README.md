# DSA interview prep w/ Python

as inspired by https://github.com/kdn251/interviews

View "basic" prerequisite video [here](https://www.youtube.com/watch?v=0K_eZGS5NsU), by Neetcode.io.

Definitely read throughout [this](https://haseebq.com/how-to-break-into-tech-job-hunting-and-interviews/) article by Haseeb Qureshi to feel motivated, guided (and pumped!), specially if you come from a non-cs specific background like me.

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
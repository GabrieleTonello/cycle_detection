# Cycle Detection Challenge
*** 

The Challenge consists in developing a function called _has\_cycle_ , which has a parameter _SinglyLinkedListNode_ and point to the list's head and the function returns 1 if there's a cycle, 0 otherwise.
[Challenge](https://www.vgen.it/it/cycle-detection-challenge/)

## Function
The function is defined in the file main.py, while in LinkedList.py is defined the class List that the function needs to be implemented.

## Algorithm to Solve the Problem

The solution is an implementation of the _Floyd's tortoise and hare algorithm_, which works with two pointer moving at different speeds and, if the two pointer eventually are the same, it means there's a cycle. The algorithm stops when it's found this cycle, or when a pointer reaches "None" node, that indicates the end of the Linked List.
[For further explanation](https://www.isa-afp.org/browser_info/devel/AFP/TortoiseHare/document.pdf) 

## Technologies used to implement the function

The function has been written in Python 3.9 and tests have been run using unittest.
Testing has demonstrated the correctness of the solution, testing with large lists, lists with cycles, lists wituout cycles and empty lists.

### Gabriele Tonello




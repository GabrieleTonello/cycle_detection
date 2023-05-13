from LinkedList import List


def has_cycle( SinglyLinkedListNode: List) -> int:
    """ The function is an implementation Floyd's cycle-finding algorithm.

    :param SinglyLinkedListNode (List): pointer to the list's head
    :return (int): 1 if the list has a cycle, 0 otherwise
    """
    slow_pointer = SinglyLinkedListNode.head # it refers to a node and its velocity it's the slowest one
    fast_pointer = SinglyLinkedListNode.head # it refers to a node and its velocity it's the fastest one
    move_slow_pointer = 0 # flag to make slow_punt move
    while fast_pointer:
        fast_pointer = fast_pointer.next
        if move_slow_pointer: # moves the pointer only if the variable equals 0 and then assigns 0 to it
            slow_pointer = slow_pointer.next
            move_slow_pointer = 0
        else: # if the variable is 0, assigns 1 to it
            move_slow_pointer = 1
        if fast_pointer == slow_pointer: # if the two pointer are equal, it means there's a cycle, so it returns 1 
            return 1
    return 0



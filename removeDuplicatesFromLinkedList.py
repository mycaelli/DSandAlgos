'''
INPUT
    ordered linked list
    linkedList = 1 -> 1 -> 3 -> 4 -> 4 -> 4 -> 5 -> 6 -> 6

OUTPUT
    1 -> 3 -> 4 -> 5 -> 6

    IMPORTANT: The linked list should be modified in place (dont create a new linked list)
'''

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n) Time | O(1) Space
def removeDuplicatesFromLinkedList(linkedList):
    current = linkedList
    while current.next is not None:
      if current.value == current.next.value:
        current.next = current.next.next
        continue
      current = current.next
    return linkedList

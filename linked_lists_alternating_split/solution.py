class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    if head is None or head.next is None:
        raise Exception

    first = head
    second = head.next

    a = first
    b = second

    while b is not None and b.next is not None:
        a.next = b.next
        a = a.next

        b.next = a.next
        b = b.next

    a.next = None

    return Context(first, second)

from preloaded import Node

def swap_pairs(head):
    if head is None or head.next is None:
        return head

    new_head = head.next
    prev = None
    current = head

    while current is not None and current.next is not None:
        next_pair = current.next.next
        second = current.next

        second.next = current
        current.next = next_pair

        if prev is not None:
            prev.next = second

        prev = current
        current = next_pair

    return new_head

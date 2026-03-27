from preloaded import Node

def linked_list_from_string(list_repr: str) -> Node | None:
    if list_repr == "None":
        return None

    parts = list_repr.split(" -> ")
    head = None

    for value in reversed(parts[:-1]):
        head = Node(int(value), head)
    return head

from LinkedList import LinkedList


def loop_detection(ll):
    fast = slow = ll.head

    while fast and fast.__next__:
        fast = fast.next.__next__
        slow = slow.__next__
        if fast is slow:
            break

    if fast is None or fast.__next__ is None:
        return None

    slow = ll.head
    while fast is not slow:
        fast = fast.__next__
        slow = slow.__next__

    return fast

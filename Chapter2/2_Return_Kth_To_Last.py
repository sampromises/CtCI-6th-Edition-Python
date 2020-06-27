from LinkedList import LinkedList


def kth_to_last(ll, k):
    runner = current = ll.head
    for i in range(k):
        if runner is None:
            return None
        runner = runner.__next__

    while runner:
        current = current.__next__
        runner = runner.__next__

    return current

ll = LinkedList()
ll.generate(10, 0, 99)
print(ll)
print((kth_to_last(ll, 3)))

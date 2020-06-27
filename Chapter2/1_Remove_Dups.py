from LinkedList import LinkedList


def remove_dups(ll):
    if ll.head is None:
        return

    current = ll.head
    seen = set([current.value])
    while current.__next__:
        if current.next.value in seen:
            current.next = current.next.__next__
        else:
            seen.add(current.next.value)
            current = current.__next__

    return ll


def remove_dups_followup(ll):
    if ll.head is None:
        return

    current = ll.head
    while current:
        runner = current
        while runner.__next__:
            if runner.next.value == current.value:
                runner.next = runner.next.__next__
            else:
                runner = runner.__next__
        current = current.__next__

    return ll.head

ll = LinkedList()
ll.generate(100, 0, 9)
print(ll)
remove_dups(ll)
print(ll)

ll.generate(100, 0, 9)
print(ll)
remove_dups_followup(ll)
print(ll)

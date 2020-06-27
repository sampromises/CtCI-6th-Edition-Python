from LinkedList import LinkedList


def is_palindrome(ll):
    fast = slow = ll.head
    stack = []

    while fast and fast.__next__:
        stack.append(slow.value)
        slow = slow.__next__
        fast = fast.next.__next__

    if fast:
        slow = slow.__next__

    while slow:
        top = stack.pop()

        if top != slow.value:
            return False

        slow = slow.__next__

    return True


ll_true = LinkedList([1, 2, 3, 4, 5, 4, 3, 2, 1])
print((is_palindrome(ll_true)))
ll_false = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
print((is_palindrome(ll_false)))

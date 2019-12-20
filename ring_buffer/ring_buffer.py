from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # if storage is empty define oldest value in self.current
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            if self.storage.length == 1:
                self.current = self.storage.tail
        # when storage equals to capacity overwrites the oldest value
        elif self.storage.length == self.capacity:
            self.current.value = item
            # define new oldest item
            if self.current.next:
                self.current = self.current.next
            else:
                self.current = self.storage.head

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        current_node = self.storage.head
        while current_node:
            list_buffer_contents.append(current_node.value)
            current_node = current_node.next
        return list_buffer_contents


        # TODO: Your code here

        return list_buffer_contents


ring = RingBuffer(3)
ring.append('a')
ring.append('b')
ring.append('c')
ring.append('d')


# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass

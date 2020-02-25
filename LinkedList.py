from weakref import ref


class LinkedList:
    class Node:
        def __init__(self, prev_node=None, next_node=None, data=None):

            if prev_node is not None and not isinstance(prev_node, type(self)):
                raise TypeError('prev_node must be Node or None')

            if next_node is not None and not isinstance(next_node, type(self)):
                raise TypeError('next_node must be Node or None')

            self.prev_node_ = ref(prev_node) if prev_node is not None else None
            self.next_node_ = next_node
            self.data = data

        @property
        def prev_node(self):
            return self.prev_node_() if self.prev_node_ is not None else None

        @prev_node.setter
        def prev_node(self, value):
            if value is not None and not isinstance(value, type(self)):
                raise TypeError('Value must be Node or None')
            self.prev_node_ = ref(value) if value is not None else None

        @property
        def next_node(self):
            return self.next_node_

        @next_node.setter
        def next_node(self, value):
            if value is not None and not isinstance(value, type(self)):
                raise TypeError('Value must be Node or None')
            self.next_node_ = value

    def __init__(self):
        self.size = 0
        self.head = self.Node()
        self.tail = self.Node(self.head)
        self.head.next_node = self.head

    def insert_next_node(self, current_node, data):
        new_node = self.Node(current_node, current_node.next_node, data)
        current_node.next_node.prev_node = new_node
        current_node.next_node = new_node
        self.size += 1

    def insert_node(self, index, data):
        if not isinstance(index, int):
            raise TypeError('index must be int')

        if index >= 0:
            if not 0 <= index < self.size:
                raise ValueError('Invalid index')
            current_node = self.head.next_node
            for _ in range(self.size):
                current_node = current_node.next_node

            self.insert_next_node(current_node, data)

        if index < 0:
            ...


ll = LinkedList()

ll.insert_node(0, 'Привет')
ll.insert_node(1, 'Python')












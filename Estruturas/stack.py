class StackWithArray:
    # Builder
    def __init__(self, max_length=1000):
        self.items = [0]*max_length
        self.max_length = max_length
        self.pointer = 0

    # Add Items
    def push(self, item):
        self.items[self.pointer] = item
        self.pointer += 1

    # Remove Items
    def pop(self):
        if self.pointer == 0:
            raise IndexError("Empty list")
        
        result = self.items[self.pointer]
        self.pointer -= 1
        return result
    
    # Just return the item
    def peek(self):
        if self.pointer == 0:
            raise IndexError("Empty list")
        
        return self.items[self.pointer-1]
    
    # Return stack size
    def size(self):
        return self.pointer
    
    def print_stack(self):
        return self.items, self.pointer



# st = Stack(max_length=5)

# st.push(5)
# st.push(3)
# st.pop()
# st.push(4)
# st.pop()
# # st.pop()

# arr, pointer = st.print_stack()

# print(f'Ponteiro = {pointer} | Size: {st.size()} | -> {arr}')

# print(f'Peek: {st.peek()}')

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class StackWithLinkedList:
    # Builder
    def __init__(self):
        self.top = None
        self._size = 0

    # Add Items
    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self._size += 1
        # self.items[self.pointer] = item
        # self.pointer += 1

    # Remove Items
    def pop(self):
        if self.top is None:
            raise IndexError("Empty stack")
        
        popped_node = self.top
        self.top = popped_node.next
        self._size -= 1
        
        # result = self.items[self.pointer]
        # self.pointer -= 1
        return popped_node.value
    
    # Just return the item
    def peek(self):
        if self.top is None:
            raise IndexError("Empty stack")
        
        return self.top.value
    
    # Return stack size
    def size(self):
        return self._size
    
    # def print_stack(self):
    #     return self.items, self.pointer

stack = StackWithLinkedList()

stack.push(1)
stack.push(2)
stack.push(3)
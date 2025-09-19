# Definição de um nó
class Node:
    def __init__(self, data):
        self.data = data   # valor armazenado
        self.next = None   # referência para o próximo nó


# Implementação de uma LinkedList
class LinkedList:
    def __init__(self):
        self.head = None   # cabeça da lista

    # Inserir no final
    def append(self, data):
        new_node = Node(data)
        if not self.head:   # se lista está vazia
            self.head = new_node
            return
        last = self.head
        while last.next:    # percorre até o último
            last = last.next
        last.next = new_node

    # Inserir no início
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Remover por valor
    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:  # se for o primeiro nó
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.data != data:
            current = current.next
        if current.next:
            current.next = current.next.next

    # Mostrar elementos
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")



ll = LinkedList()

ll.append('Julia')
ll.append('Eduardo')
ll.prepend('Yasmim')

ll.delete('Eduardo')

ll.print_list()
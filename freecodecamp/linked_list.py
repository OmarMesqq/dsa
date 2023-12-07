class Node:
    """
    An object for storing a single node of a linked list
    Models two attributes - its data and 
    link to the next node in the list
    """
    data = None 
    next_node = None 

    # Constructor
    def __init__(self, data) -> None:
        self.data = data   

    # Specifies object representation when running type()
    def __repr__(self) -> str:
        return "<Node data: {}>".format(self.data)
    
    # Index

class LinkedList:
    """
    Singly linked list 
    """ 

    # Initially, set the list's head to nothing
    def __init__(self) -> None:
        self.head = None

    # True if there is no head in the list 
    # False otherwise
    def is_empty(self): 
        return self.head == None 


    def size(self):
        """  
        Returns number of nodes in the list 
        Takes O(n) time (linear)
        """ 
        currentNode = self.head 
        count = 0 

        while currentNode != None:
            count += 1 
            currentNode = currentNode.next_node 
        
        return count
    

    def add(self, data): 
        """ 
        Adds new Node containing data at the head of the list 
        Takes constant time O(1)
        """
        new_node = Node(data) 
        new_node.next_node = self.head 
        self.head = new_node


    def search(self, key):
        """
        Searches for the first node containing data that matches the key
        Return the Node or `None` if not found
        Takes O(n) time
        """
        current = self.head

        while current != None: 

            if current.data == key:
                return True 
            else: 
                current = current.next_node
        return False


    def insert(self, data, index):
        """
        Inserts a new Node containing data at index postion 
        Insertion takes O(1) time but finding the Node at
        the insertion point takes O(n) time 
        Therefore, takes an overall linear time
        """ 
        if index == 0:
            self.add(data)
        elif index > 0:
            new_node = Node(data)

            position = index 
            current = self.head

            while position > 1:
                current = current.next_node
                position -= 1 
            
            previous = current
            next = current.next_node

            previous.next_node = new_node 
            new_node.next_node = next


    def remove_index(self, index):
        """
        Removes data in the Node that matches the index
        Returns the Node or None if the index is out of the list
        Takes O(n) time
        """
        if index < 0 or index >= self.size():
            return None

        current = self.head
        if index == 0:
            self.head = current.next_node
        else:
            position = 0
            previous = None

            while current and position < index:
                previous = current
                current = current.next_node
                position += 1

            previous.next_node = current.next_node

        return current


    def __repr__(self) -> str:

        nodes = [] 
        current = self.head 

        while current != None: 
            if current is self.head: 
                nodes.append("[Head: {}]".format(current.data))
            elif current is None: 
                nodes.append("[Tail: {}]".format(current.data))
            else:
                nodes.append("[{}]".format(current.data))
            
            current = current.next_node 

        return '-> '.join(nodes)

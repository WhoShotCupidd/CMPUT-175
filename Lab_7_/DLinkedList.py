class DLinkedListNode:
    # An instance of this class represents a node in Doubly-Linked List
    def __init__(self,initData,initNext,initPrevious):
        self.data = initData
        self.next = initNext
        self.previous = initPrevious
        
        if initNext != None:
            self.next.previous = self
        if initPrevious != None:
            self.previous.next = self
            
    def getData(self):
        return self.data
    
    def setData(self,newData):
        self.data = newData
        
    def getNext(self):
        return self.next
    
    def getPrevious(self):
        return self.previous
    
    def setNext(self,newNext):
        self.next = newNext
        
    def setPrevious(self,newPrevious):
        self.previous = newPrevious


class DLinkedList:
    # An instance of this class represents the Doubly-Linked List
    def __init__(self):
        self.__head=None
        self.__tail=None
        self.__size=0        
           
    def search(self, item):
        current = self.__head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found= True
            else:
                current = current.getNext()
        return found
        
    def index(self, item):
        current = self.__head
        found = False
        index = 0
        while current != None and not found:
            if current.getData() == item:
                found= True
            else:
                current = current.getNext()
                index = index + 1
        if not found:
                index = -1
        return index    
    







   
         
    def add(self, item):
        if self.__size == 0:
            node = DLinkedListNode(item, None, None)
            self.__head = node
            self.__tail = node
            
        else:
            node = DLinkedListNode(item, self.__head, None)
            self.__head.setPrevious(node)
            self.__head = node
        self.__size += 1
    
        
    def remove(self, item):
        
        prev = None
        current = self.__head
        index = 0
        
        while not current.getData() == item and not current == None:
            prev = current
            current = current.getNext()
        if not current == None:
            if prev == None:
                self.__head == current.getNext()
            else:
                prev.setNext(current.getNext())
            if not current.getNext() == None:
                current.getNext().setPrevious(prev)
            else:
                self.__tail = prev
            self.__size -= 1
        
    def append(self, item):
        
        last = self.__tail
        
        if self.__head == None:
            node = DLinkedListNode(item, None, None)
            self.__head = node
        else:
            node = DLinkedListNode(item, None, last)
            last.setNext(node)
        self.__tail = node
        self.__size += 1
        
        
    def insert(self, pos, item):
        
        node = DLinkedListNode(item, None, None)
        current = self.__head
        prev = None
        
        for i in range(pos):
            prev = current
            current = current.getNext()
        if self.__head == None:
            self.__tail = node
            self.__head = node
        else:
            if prev == None:
                self.__head = node
            else:
                node.setPrevious(prev)
                prev.setNext(node)
            if current == None:
                self.__tail = node
            else:
                node.setNext(current)
                current.setPrevious(node)
        self.__size += 1
        
    def pop1(self):
        
        current = self.__tail
        if self.__head == current:
            self.__head = None
            self.__tail = None
        else:
            current.getPrevious().setNext(current.getNext())
            self.__tail = current.getPrevious()
        self.__size -= 1
        return current
    
    
    
    
    
    
    
    def pop(self, pos=None):
        
        prev = None
        current = self.__head
        
        if pos == None or (pos + 1) == self.__size:
            item = self.pop1()
        elif pos == 1:
            current.getNext().setPrevious(prev)
            item = current 
            self.__size -= 1
        else:
            for i in range(pos):
                prev = current 
                current = current.getNext()
            prev.setNext(current.getNext())
            current.getNext().setPrevious(prev)
            item = current 
            self.__size -= 1
        return item.getData()
        
        
        
        
        
        
        
        
        
    def searchLarger(self, item):
        head = self.__head
        index = 0
        while not head.getData() > item and head != None:
            head = head.getNext()
            index += 1
        if head == None:
            index = -1
        return index
        

        
    def getSize(self):
        
        return self.__size
    
    
    def getItem(self, pos):
        
        assert type(pos) is int, "pos must be integer"
        if pos >= 0:
            current = self.__head
            for i in range(pos):
                current = current.getNext()
        else:
            current = self.__tail
            for i in range(abs(pos) - 1):
                current = current.getPrevious()
        return current.getData()
        
    def __str__(self):
        
        index = 0
        head = self.__head
        stri = ""
        
        while head != None:
            if index > 0:
                stri += " "
            data = head.getData()
            if data != None:
                stri += str(data)
                index += 1
            head = head.getNext()
        return stri









def test():
                  
    linked_list = DLinkedList()
                    
    is_pass = (linked_list.getSize() == 0)
    assert is_pass == True, "fail the test"
            
    linked_list.add("World")
    linked_list.add("Hello")    
        
    is_pass = (str(linked_list) == "Hello World")
    assert is_pass == True, "fail the test"
              
    is_pass = (linked_list.getSize() == 2)
    assert is_pass == True, "fail the test"
            
    is_pass = (linked_list.getItem(0) == "Hello")
    assert is_pass == True, "fail the test"
        
        
    is_pass = (linked_list.getItem(1) == "World")
    assert is_pass == True, "fail the test"    
            
    is_pass = (linked_list.getItem(0) == "Hello" and linked_list.getSize() == 2)
    assert is_pass == True, "fail the test"
            
    is_pass = (linked_list.pop(1) == "World")
    assert is_pass == True, "fail the test"     
            
    is_pass = (linked_list.pop() == "Hello")
    assert is_pass == True, "fail the test"     
            
    is_pass = (linked_list.getSize() == 0)
    assert is_pass == True, "fail the test" 
                    
    int_list2 = DLinkedList()
                    
    for i in range(0, 10):
        int_list2.add(i)      
    int_list2.remove(1)
    int_list2.remove(3)
    int_list2.remove(2)
    int_list2.remove(0)
    is_pass = (str(int_list2) == "9 8 7 6 5 4")
    assert is_pass == True, "fail the test"
                
    for i in range(11, 13):
        int_list2.append(i)
    is_pass = (str(int_list2) == "9 8 7 6 5 4 11 12")
    assert is_pass == True, "fail the test"
                
    for i in range(21, 23):
        int_list2.insert(0,i)
    is_pass = (str(int_list2) == "22 21 9 8 7 6 5 4 11 12")
    assert is_pass == True, "fail the test"
                
    is_pass = (int_list2.getSize() == 10)
    assert is_pass == True, "fail the test"    
                    
    int_list = DLinkedList()
                    
    is_pass = (int_list.getSize() == 0)
    assert is_pass == True, "fail the test"                   
                    
    for i in range(0, 1000):
        int_list.append(i)      
    correctOrder = True
            
    is_pass = (int_list.getSize() == 1000)
    assert is_pass == True, "fail the test"            
            
        
    for i in range(0, 200):
        if int_list.pop() != 999 - i:
            correctOrder = False
                            
    is_pass = correctOrder
    assert is_pass == True, "fail the test" 
            
    is_pass = (int_list.searchLarger(200) == 201)
    assert is_pass == True, "fail the test" 
            
    int_list.insert(7,801)   
        
    is_pass = (int_list.searchLarger(800) == 7)
    assert is_pass == True, "fail the test"
            
            
    is_pass = (int_list.getItem(-1) == 799)
    assert is_pass == True, "fail the test"
            
    is_pass = (int_list.getItem(-4) == 796)
    assert is_pass == True, "fail the test"
                    
    if is_pass == True:
        print ("=========== Congratulations! Your have finished exercise 2! ============")

                
if __name__ == '__main__':
    test()

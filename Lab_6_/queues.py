class BoundedQueueEmptyError(Exception):
    pass

class BoundedQueueFullError(Exception):
    pass

class CircularQueueEmptyError(Exception):
    pass

class CircularQueueFullError(Exception):
    pass

class BoundedQueue: 
    # Creates a new empty queue:
    def __init__(self, capacity): 
        assert isinstance(capacity, int), ('Error: Type error: %s' % (type(capacity))) # throws an assertion error on not true
        assert capacity >= 0, ('Error: Illegal capacity: %d' % (capacity))
        self._items = [] # init the  list / queue as empty
        self.__capacity = capacity
        
        
        
        
        
        
 
    # Adds a new item to the back of the queue, and returns nothing:
    def enqueue(self, item): 
        '''
        Enqueue the element to the back of the queue
        :param item: the element to be enqueued
        :return: No returns
        '''
        if self.is_full():
            raise BoundedQueueFullError("Error: Can not enqueue more than capacity=" + str(self.capacity()))
        self._items.insert(0, item)  
        
        
    # Removes and returns the front-most item in the queue.      
    # Returns nothing if the queue is empty.    
    def dequeue(self):        
        '''
        Dequeue the element from the front of the queue and return it
        :return: The object that was dequeued
        '''
        
        if self.is_empty():
            raise BoundedQueueEmptyError("Error: Can not dequeue empty bounded queue")
        else: 
            return self._items.pop()
    
    
    
    
    
    
    # Returns the front-most item in the queue, and DOES NOT change the queue.      
    def peek(self):        
        if len(self._items) <= 0:            
            raise Exception('Error: Queue is empty')        
        return self._items[0]
        
    # Returns True if the queue is empty, and False otherwise:    
    def is_empty(self):
        return len(self._items) == 0        
    
    # Returns True if the queue is full, and False otherwise:    
    def is_full(self):
        return len(self._items) == self.__capacity
    
    # Returns the number of items in the queue:    
    def size(self):        
        return len(self._items)        
    
    # Returns the capacity of the queue:    
    def capacity(self):        
        return self.__capacity
    
    # Removes all items from the queue, and sets the size to 0    
    # clear() should not change the capacity    
    def clear(self):        
        self._items = []

    # Returns a string representation of the queue: 
    def __str__(self):               
        str_exp = ""        
        for item in self._items:            
            str_exp += (str(item) + " ")                    
        return str_exp
        
    # Returns a string representation of the object bounded queue: 
    def __repr__(self):               
        return  str(self) + " Max=" + str(self.__capacity)      

class CircularQueue:
    # Creates a new empty queue:
    def __init__(self, capacity): 
        # Check validity of capacity type and value
        assert isinstance(capacity, int), ('Error: Type error: %s' % (type(capacity)))
        assert capacity >= 0, ('Error: Illegal capacity: %d' % (capacity))
        
        # Initialize private attributes
        self._items = []
        self.__capacity = capacity
        self.__count=0
        self.__head=0
        self.__tail=0
        
        # Allocate space for the circular queue
        for i in range(self.__capacity):
            self._items.append(None)
        
    
    
    
    
    
    
    # Adds a new item to the back of the queue, and returns nothing:    
    def enqueue(self, item): 
        '''
        This function enqueues the item into the back of the queue
        :param item: The  item to  be queued
        :return: No returns
        '''

        if self.is_full():
            raise CircularQueueFullError()
        self._items[self.__tail] = item
        self.__tail = (self.__tail + 1) % self.__capacity
        self.__count += 1
        
    # Removes and returns the front-most item in the queue.      
    # Returns nothing if the queue is empty.    
    def dequeue(self):        
        '''
        Dequeue the the element from the front of the queue and return the value
        :return: Returns the object that is dequeued
        '''

        if self.is_empty():
            raise CircularQueueEmptyError()
        item = self._items[self.__head]
        self._items[self.__head] = None
        self.__head = (self.__head + 1) % self.__capacity
        self.__count -= 1
        return item      
        
        
        
        
        
        
            
    
    # Returns the front-most item in the queue, and DOES NOT change the queue.      
    def peek(self):        
        if self.__count == 0:            
            raise Exception('Error: Queue is empty')        
        
        return self._items[self.__head]
    
    # Returns True if the queue is empty, and False otherwise:    
    def is_empty(self):
        return self.__count == 0        
    
    # Returns True if the queue is full, and False otherwise:    
    def is_full(self):
        return self.__count == self.__capacity
    
    # Returns the number of items in the queue:    
    def size(self):        
        return self.__count        
    
    # Returns the capacity of the queue:    
    def capacity(self):        
        return self.__capacity
    
    # Removes all items from the queue, and sets the size to 0    
    # clear() should not change the capacity    
    def clear(self):        
        self._items = []
        self.__count = 0
        self.__head = 0
        self.__tail = 0
    
    # Returns a string representation of the queue: 
    def __str__(self):               
        str_exp = "]"        
        i = self.__head
        for j in range(self.__count):            
            str_exp += str(self._items[i]) + " "
            i = (i+1) % self.__capacity
        return str_exp + "]"
        
    # Returns a string representation of the object CircularQueue    
    def __repr__(self):        
        return str(self._items) + " H= " + str(self.__head) + " T="+str(self.__tail) + " (" +str(self.__count)+"/"+str(self.__capacity)+")"  
 
 
 
    
def main():
    # Test bounded queue creation
    bq=BoundedQueue(3)
    print("My bounded queue is:", bq)
    print(repr(bq))
    print("Is my bounded queue empty?", bq.is_empty())
    print('----------------------------------')
    
    
    # 1. To Do
    # Test when we try to dequeue from an EMPTY queue
    try:
        bq.dequeue()

    except Exception as dequeueError:
        print(dequeueError)
        # To Do: Write a way to handle it

    print('----------------------------------')
    
    
    
    # 2. To Do
    # Test adding one element to queue
    
    bq.enqueue("bob")
    
    print(bq)
    print(str(bq))
    print("Is my bounded queue empty?", bq.is_empty())    
    print('----------------------------------')
    
    
    
    # 3. Uncomment and run
    # Test adding more elements to queue
    bq.enqueue("eva")
    bq.enqueue("paul")
    print(repr(bq))
    print("Is my bounded queue full?", bq.is_full())
    print("There are", bq.size(), "elements in my bounded queue.")
    print('----------------------------------')
    
 
    
    # 4. To Do
    # Test trying to add an element to a FULL queue
    
    try:
        bq.enqueue("extra")
    except Exception as enqueueError:
        print(enqueueError)
        
    print('----------------------------------')
    
    
    
    # 5. Uncomment and run
    # Test removing element from full queue
    item = bq.dequeue()
    print(repr(bq))
    print(item,"was first in the bounded queue:", bq)
    print("There are", bq.size(), "elements in my bounded queue.")
    print('----------------------------------')
    
    
    
    # 6. Uncomment and run
    # Test capacity of queue
    print("Total capacity is:", bq.capacity())
    

    
    # 7. To Do: Uncomment print statements, one at a time
    # Can we just access private capacity attribute directly outside of Class definition?
    #print(bq.capacity) Can access private capacity attribute directly outside of Class definition
    #print(bq.__capacity) Cannot access private capacity attribute directly outside of Class definition
    

    
if __name__ == '__main__':
    main()

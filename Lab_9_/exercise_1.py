import random
import time

#---------------------------------------#      
# Implement Recursive selection sort here. 

# n: size of array - index is index of starting element
def recursive_selection_sort(data, data_len, index = 0): 
  
    # TODO-Remove pass and fill out the rest. 
    #You may use additional user_defined functions if required.
    pass
    # Set the base case 
          
    # Find the minimum index 
      
    # Swap the data 
          
    # Recursively calling selection sort function 

#---------------------------------------#
#Implement the Recursive merge sort here
  
def recursive_merge_sort(data): 
    
    # split the list in 2 halfs 
    # recursion to sort each half
    # merge the two lists
    
    left = data[:len(data)//2]
    right = data[len(data)//2:]
    
    left = recursive_merge_sort(left)
    right = recursive_merge_sort(right)
    
    a_list = []
    left_index = 0
    right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            a_list.append(left[left_index])
            left_index += 1
        else:
            a_list.append(right[right_index])
            right_index += 1
            
            
    while left_index < len(left):
        a_list.append(left[i])
        
    while right_index < len(right):
        a_list.append(right[i])
                
        
    
    
    
    
   
    #You may use additional user_defined functions if required.

    # Set the base case 
    
    #Find the middle of the data list
    
    #Recursively calling merge sort function for both half of the data list
    
    # merge the two halves of the data list and return the data list
     
#---------------------------------------#
if  __name__== "__main__":
    # Define the list of random numbers
    random_list = [random.randint(1,1000) for i in range(500)]
    list_len = len(random_list) 
    ascending_list = sorted(random_list)
    descending_list = sorted(random_list, reverse=True)
      
    # Calculate the execution time to sort a list of random numbers #
    random_list_ = random_list.copy()  # make a copy to save the unsorted list
    start_sel = time.time()
    recursive_selection_sort(random_list_, list_len)
    end_sel = time.time()
    
    start_merge = time.time()
    recursive_merge_sort(random_list)
    end_merge = time.time()
    
    # Print the rsults execution time to sort a list of random numbers
    print('The execution time: to sort a random list of integers in descending order.')
    print(' - Recursive selection sort: {}'.format(end_sel - start_sel))
    print(' - Recursive merge sort: {}'.format(end_merge - start_merge))
    
    
    # Calculate the execution time to sort a list of intergers already sorted in ascending order #
    ascending_list_ = ascending_list.copy()
    start_sel = time.time()
    recursive_selection_sort(ascending_list_, list_len)
    end_sel = time.time()
    
    start_merge = time.time()
    recursive_merge_sort(ascending_list)
    end_merge = time.time()
    
    # Print the rsults execution time to sort a list of intergers already sorted in ascending order 
    print('The execution time: to sort a ascending list of integers in descending order.')
    print(' - Recursive selection sort: {}'.format(end_sel - start_sel))
    print(' - Recursive merge sort: {}'.format(end_merge - start_merge))      
    
    
    # Calculate the execution time to sort a list of intergers already sorted in descending order #
    descending_list_ = descending_list.copy()
    start_sel = time.time()
    recursive_selection_sort(descending_list_, list_len)
    end_sel = time.time()
    
    start_merge = time.time()
    recursive_merge_sort(descending_list)
    end_merge = time.time()
    
    # Print the rsults execution time to sort a list of intergers already sorted in descending order 
    print('The execution time: to sort a descending list of integers in descending order.')
    print(' - Recursive selection sort: {}'.format(end_sel - start_sel))
    print(' - Recursive merge sort: {}'.format(end_merge - start_merge))    



      


import random
import time


def recursive_selection_sort(data, data_len, index = 0): 

    if index == data_len:
        return -1

    max_value = max(data[index:])
    max_index = data.index(max_value)
    
    if max_index != index:
        data[max_index], data[index] =  data[index], data[max_index]
        
    recursive_selection_sort(data, data_len, index + 1)

            

def recursive_merge_sort(data): 
    
    if len(data) < 2:
        return data

    middle = len(data) // 2
    left = recursive_merge_sort(data[:middle])
    right = recursive_merge_sort(data[middle:])

    left_index, right_index, data_index = 0, 0, 0
   
    while left_index < len(left) and right_index < len(right):
        if left[left_index] >= right[right_index]:
            data[data_index] = left[left_index]
            left_index += 1
        else:
            data[data_index] = right[right_index]
            right_index += 1
        data_index += 1

    while left_index < len(left):
        data[data_index] = left[left_index]
        left_index += 1
        data_index += 1

    while right_index < len(right):
        data[data_index] = right[right_index]
        right_index += 1
        data_index += 1
        
    return data
    
"""
if  __name__== "__main__":
    # Define the list of random numbers
    random_list = [random.randint(1,1000) for left_index in range(500)]
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
    
    # Print the results execution time to sort a list of intergers already sorted in descending order 
    print('The execution time: to sort a descending list of integers in descending order.')
    print(' - Recursive selection sort: {}'.format(end_sel - start_sel))
    print(' - Recursive merge sort: {}'.format(end_merge - start_merge))    
"""
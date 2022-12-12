def my_search(a_list, item):
    if len(a_list) <= 3:
        return a_list.index(item)
    x = len(a_list)//3 + 1
    if item < a_list[x]:
        return my_search(a_list[:x], item)
    elif item >= a_list[-x]:
        return my_search(a_list[x:x*2], item) + x
    else:
        return my_search(a_list[x:x*2], item) + x
    
    
a_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]


print(my_search(a_list, 4))
            
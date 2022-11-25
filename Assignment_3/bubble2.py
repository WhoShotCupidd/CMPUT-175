def bubble2(a_list):
    if a_list[0] > a_list[1]:
        a_list[0], a_list[1] = a_list[1], a_list[0]
    return a_list

def printFun(test):
    if (test < 1):
        return
    else:
        print(test, end = " ")
        printFun(test - 1)  # statement 2
        print(test, end = " ")
        return
test = 5
printFun(test)
# This code is contributed by Smitha Dinesh Semwal
# Source: https://www.geeksforgeeks.org/recursion/
#program to check if the symbols is balanced on both sides in an expression using the concept of stacks

from datastructs.stack import Stack
from timeit import default_timer as timer

def balanced_symbols(par_string):
    s = Stack()
    balanced = True
    index = 0
    while index < len(par_string) and balanced:
        symbol = par_string[index]
        if symbol in "[{(":
            s.push(symbol)
            print(s.items)
        else:
            if s.is_empty():
                balanced = False
            else:
                if symbol in ")}]":
                    s.pop()
        index+=1

    if balanced and s.is_empty():
        return True
    else:
        return False


if __name__ == '__main__':
    par_string = '[{()}]'
    start_time = timer()
    print("---Evaluating expression---")
    print("Is Balanced: ",balanced_symbols(par_string))
    end_time = timer()
    elapsed_time = end_time-start_time
    print("time taken to run: ", elapsed_time)


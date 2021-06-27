#program to check if the paranthesis is balanced on both sides in an expression using the concept of stacks

from datastructs.stack import Stack
from timeit import default_timer as timer


def balanced_par(par_string):
    """ function to check for balanced paranthesis.
        par_string: string containing the expression to evaluate
    """
    s = Stack()
    balanced = True
    index=0
    while index <len(par_string) and balanced:
        symbol = par_string[index]
        if symbol == "(":
            s.push(symbol)
            print(s.items)
        else:
            if s.is_empty():
                balanced = False
            else:
                s.pop()
                print(s.items)
        index+=1

    print(balanced)
    print(s.is_empty())
    if balanced and s.is_empty():
        return True
    else:
        return False

    
if __name__ == '__main__':
    par_string = '((()))'
    start_time = timer()
    print("---Evaluating expression---")
    print("Is Balanced: ",balanced_par(par_string))
    end_time = timer()
    elapsed_time = end_time-start_time
    print("time taken to run: ", elapsed_time)

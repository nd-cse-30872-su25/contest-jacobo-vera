#!/usr/bin/env python3

# ChallengeC: Missing Operations
# Vera Casquero & Jacobo Weisner 

import sys 

#Global 
ops = ['+', '-', '*']
expression = "(((9 {} 8) {} 7) {} 6) {} (5 {} (4 {} (3 {} (2 {} 1))))"

#Functions 
def evaluate(options: list) -> int: 
    #Use a stack to evaluate a possible combination 
    stack = []

    #Push until )
    for symbol in options: 
        if symbol != ')': 
            stack.append(symbol)
        else: 
            try: 
                #Get right num, operator and left nom
                right = stack.pop()
                operator = stack.pop()
                left = stack.pop()
                stack.pop()
            except IndexError: 
                return None
            #Perform operations 
            if operator == '+': 
                res = right + left
            elif operator == '-': 
                res = left - right 
            else: 
                res = right * left 
            stack.append(res)
    #Return result
    return stack[0]

            
def build_options(target): 
    #Splitting the expression up & wrapping in parenthesis
    expression_list = (expression.replace('(', ' ( ').replace(')', ' ) ').split())
    expression_list = ['('] + expression_list + [')']

    #[(current op. index, list of chosen options)]
    ops_stack = [(0,[])]
    while ops_stack: 
        i, operations = ops_stack.pop()

        #If i == 8, all are filled so, evaluate
        if i == 8: 
            divided = []
            ops_i = 0
            #Replace placeholder 
            for j in expression_list: 
                if j == '{}': 
                    divided.append(operations[ops_i])
                    ops_i += 1
                #Convert digit to int for math
                elif j.isdigit(): 
                    divided.append(int(j))
                else: 
                    divided.append(j)
            #Call to evaluate and see if matches target
            if evaluate(divided) == target: 
                return operations 
        else: 
            #If not all filled, add other op option
            for op in ops: 
                ops_stack.append((i + 1, operations + [op]))
    return None 

    

#Main Execution 
def main(): 
    #Read from stdin & print
    for line in sys.stdin: 
        target = int(line)
        operations = build_options(target)
        print(f"{expression.format(*operations)} = {target}")
        


if __name__ == "__main__": 
    main()


def arithmetic_arranger(problems,*args):
    #                             ^ can handle if an argument is passed or not,
    #                               this above can also be handeled by a list as the above will generate a tuple named args

    #check for length of the problems list
    if( len(problems)>5 ):
        return "Error: Too many problems."
    else:
        #loop through each item in problems and obtain it as a string
        line1=list()
        line2=list()
        line3=list()
        line4=list()
        for i in problems:
            #split each item of problems into sub items of a string
            splited_list = i.split(" ")
            #below if check if the operator is not + or -
            if( (splited_list[1] != "+") and (splited_list[1] != "-") ):
                return "Error: Operator must be '+' or '-'."
            #below else runs when operator found to be either + or -
            else:
                #check if any of the equation has a non digit number in its opperand
                if( not(splited_list[0].isdigit()) or not(splited_list[2].isdigit()) ):
                    return "Error: Numbers must only contain digits."
                else:
                    #last condition: check if any of the operand in any equation has a max of four digits
                    if len(splited_list[0])>4 and len(splited_list[2])>4:
                        return "Error: Numbers cannot be more than four digits."
                    else:
                        #declaring output elements of each line in each iteration of problems and append it to console output lines list variable 
                        eq_l1 = ""
                        eq_l2 = ""
                        eq_l3 = ""
                        eq_l4 = ""
                        
                        #developing third line for output width   i.e use this as a reference width for other lines                    
                        #               _____________________________________________________/>will give integer value of max operand 
                        max_width = 1+1+int( max(len(splited_list[0]), len(splited_list[2])) )
                        #           ^_^_>padding for oprtators then a single space 
                        eq_l3 = "-"*max_width
                        
                        #developing first line 
                        padding = max_width - len(splited_list[0])
                        eq_l1 = " "*padding + str(splited_list[0])
                        
                        #developing second line
                        padding = max_width - (len(splited_list[2]) + 1)
                        #                                             ^>a single space consumed by one operator
                        eq_l2 = str(splited_list[1])+ " "*padding + splited_list[2]
                        
                        #developing fourth line
                        compute = ""
                        padding = ""
                        if splited_list[1] == '+':
                            compute = str(int(splited_list[0]) + int(splited_list[2]))
                            padding = max_width - int(len(compute))
                        
                        elif splited_list[1] == '-':
                            compute = str(int(splited_list[0]) - int(splited_list[2]))
                            padding = max_width - len(compute)
                        eq_l4=" "*padding + compute
                        
                        # print(eq_l1)
                        # print(eq_l2)
                        # print(eq_l3)
                        # print(eq_l4)
                        line1.append(eq_l1)
                        line2.append(eq_l2)
                        line3.append(eq_l3)
                        line4.append(eq_l4)
        #if additional argument passed to the function as true then print arithimatic output
        if args[0] == True:
            arithmetic_arranger = "    ".join(line1)+"\n"+"    ".join(line2)+"\n"+"    ".join(line3)+"\n"+"    ".join(line4)
        #if only a list is passed to function then dont print the arithimatic output of two operands
        else:
            arithmetic_arranger = "    ".join(line1)+"\n"+"    ".join(line2)+"\n"+"    ".join(line3)
        print(arithmetic_arranger)
        return arithmetic_arranger
    
'''
    below are the test cases
'''    
# arithmetic_arrangers = arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"])
# print(arithmetic_arrangers)
# arithmetic_arrangers = arithmetic_arranger(['3801 - 2', '123 + 49'])
# print(arithmetic_arrangers)
# arithmetic_arrangers = arithmetic_arranger(['1 + 2', '1 - 9380'])
# print(arithmetic_arrangers)
# arithmetic_arrangers = arithmetic_arranger(['3 + 855', '3801 - 2', '45 + 43', '123 + 49'])
# print(arithmetic_arrangers)
# arithmetic_arrangers = arithmetic_arranger(['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380'])
# print(arithmetic_arrangers)
arithmetic_arrangers= arithmetic_arranger(['3 + 855', '988 + 40'], True)
# print(arithmetic_arrangers)

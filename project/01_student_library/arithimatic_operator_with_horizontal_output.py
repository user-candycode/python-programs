import re


def arithmetic_arranger(problems):
  first_line = str("")
  second_line = str("")
  third_line = str("")
  fourth_line = str("")

    
  fin_out_l1 = list()
  fin_out_l2 = list()
  fin_out_l3 = list()
  fin_out_l4 = list()
  for i in problems:
    # print(i)
    match = re.search( r'\d+\s[+-]\s\d+', str(i) )
    # print("match: ",match)
    if match:
        list1 = str(i).split()
        #first line
        padding = abs(len(list1[0]) - len(list1[2]))
        # print("padding:",padding)
        if(len(list1[0]) >= len(list1[2])):
            first_line = "  "+str(list1[0])
        else:
            spaces = " " * padding
            # print("spaces:",spaces,".")
            first_line = "  "+ spaces +str(list1[0])
        
        #spaces to stuff between operator and second operand
        space = len(list1[0]) - len(list1[2])
        #second line
        second_line = str(list1[1]) + " " + " "*space + str(list1[2])
        #third line
        third_line= "-"*len(second_line)
        computed_expression = eval(str(" ".join(list1)))
        padding = " " * int(len(third_line)-len(str(computed_expression)))
        fourth_line = f"{padding}{computed_expression}"
    else:
        # print("something went wrong")
        pass
    
    # print(f"{first_line}\n{second_line}\n{third_line}\n{fourth_line}\n")
    fin_out_l1.append(str(first_line)+"  ")
    fin_out_l2.append(str(second_line)+"  ")
    fin_out_l3.append(str(third_line)+"  ")
    fin_out_l4.append(str(fourth_line)+"  ")
  
  # for i,j,k,l in fin_out_l1,fin_out_l2,fin_out_l3,fin_out_l4:
  #       print(i,j,k,l)
  z = ""
  for i in fin_out_l1:
        z +=i
  z += "\n"
  for i in fin_out_l2:
        z +=i
  z += "\n"
  for i in fin_out_l3:
        z +=i
  z += "\n"
  for i in fin_out_l4:
        z +=i
  print(z)

arithmetic_arranger(["32 + 698", "2 - 3801", "45 \ 43", "123 + 49"])

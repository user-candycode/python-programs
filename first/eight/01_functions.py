
def percentage_calc(marks):
    percent=( sum(marks)/400 ) * 100  #( ( marks[0]+marks[1]+marks[2]+marks[3] )/400 ) * 100
    return percent


marks=[45,78,86,77]
result=percentage_calc(marks)
print(result)
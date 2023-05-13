'''
  https://www.hackerrank.com/challenges/python-lists
'''


if __name__ == '__main__':
    N = int(input())
    list1=[]
    for i in range(N):
        input_operation = input().split()
        if input_operation[0] == 'insert':
            list1.insert(int(input_operation[1]),int(input_operation[2]))
            #              ^position                ^data
        elif input_operation[0] == 'print':
            print(list1)
            
        elif input_operation[0] == 'remove':
            list1.remove(int(input_operation[1]))
        elif input_operation[0] == 'append':
            list1.append(int(input_operation[1]))
        elif input_operation[0] == 'sort':
            list1.sort()
        elif input_operation[0] == 'pop':
            list1.pop()
        elif input_operation[0] == 'reverse':
            list1.reverse()
        
        # print("O/P:",list1)
        
        
            
        
        

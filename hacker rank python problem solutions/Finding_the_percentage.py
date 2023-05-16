'''
  The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.

  I/P
  3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

  O/P
  56.00
  (explicitely define precision usin '%.2' % variable_name)
'''

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    if query_name in student_marks:
        list = student_marks[query_name]
        
        length = len(list)
        # print(length)
        avg = sum(list) / length
        print('%.2f' % avg )

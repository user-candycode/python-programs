def print_inverted_left_triangle(n):
    if n==1:
        return "*"
    else:
        print("* " * n)
        return print_inverted_left_triangle(n-1)
    
print(print_inverted_left_triangle(6))
import time
import threading

def calculate_square(numbers):
    print("Calculate square number")

    for n in numbers:
        time.sleep(0.5)
        print('square:',n*n)
    
def calculate_cube(numbers):
    print("Calculate cube of numbers")
    for n in numbers:
        time.sleep(0.5)
        print('cube:',n*n*n)

arr = [2,3,8,9]

t = time.time()
# calculate_square(arr)
# calculate_cube(arr)


t1 = threading.Thread(target = calculate_square, args=(arr,))
t2 = threading.Thread(target = calculate_cube, args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()

print("done in: ",time.time()-t)
print("program execution complete")
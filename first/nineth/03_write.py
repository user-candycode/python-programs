#write to a file with overide everithing everything in the file
#if file not present then it will create one
f= open('/home/candy/Documents/python/first/nineth/sample2.txt','wt')
f.write("I am writing to this file\n")
f.close()

#write to a file 
f= open('/home/candy/Documents/python/first/nineth/sample2.txt','at')
f.write("I am appending")
f.close()

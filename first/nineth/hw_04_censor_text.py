

#input a stream of words as string
input_string=input(" enter the words seperated by space\n")
#check and confirm the type of input variable
print(type(input_string))
#convert the stream of words to list using split() an assign it to new variable
user_list=input_string.split()
#print this new converted list also confirm its a list
print("bad word list: ",user_list," and its type is:", type(user_list))

#loop through the list
for i in range(len(user_list)):
    #convert into int it required in future
    #user_list[i] = int(user_list[i])
    with open("/home/candy/Documents/python/first/nineth/censor.txt",'rt') as f:
        content=f.read()
        censor_word=user_list[i]
        if len(censor_word) == 2:
            no_of_stars="**"
            content = content.replace(censor_word, f"{no_of_stars}")
            with open("/home/candy/Documents/python/first/nineth/censor.txt",'wt') as f:
                content=f.write(content)
        else:
            no_of_stars=str("*" * (len(censor_word)-2))
            content = content.replace(censor_word, f"{censor_word[0]}{censor_word[1]}{no_of_stars}")
            with open("/home/candy/Documents/python/first/nineth/censor.txt",'wt') as f:
                content=f.write(content)







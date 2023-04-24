text=input("copy the sms here\n")
spam=False

if("make a lot of money" in text):
    spam=True
elif("buy now" in text):
    spam=True
elif("click this" or "clicking this" in text):
    spam=True
elif("suscribe" in text):
    spam=True

if(spam):
    print("this is a spam sms")
else:
    print("its a regular sms")

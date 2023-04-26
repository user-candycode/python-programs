

def remove_and_strip(string,word):
    newStr= string.replace(word, "")
    return newStr.strip()


this= "    MrK is Amazing    "
n=remove_and_strip(this, "MrK")
print(n)
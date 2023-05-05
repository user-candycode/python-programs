def increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError("This is not good - MrK")

a = increment('def455')
print(a)
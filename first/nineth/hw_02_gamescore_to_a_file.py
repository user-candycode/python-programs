def game():
    return 69

score = game()

with open("/home/candy/Documents/python/first/nineth/highscore.txt",'rt') as f:
    highscore_str= f.read()

if highscore_str=="":
    with open("/home/candy/Documents/python/first/nineth/highscore.txt",'wt') as f:
        f.write(str(score))

elif int(highscore_str)<score:
    with open("/home/candy/Documents/python/first/nineth/highscore.txt",'wt') as f:
        f.write(str(score))

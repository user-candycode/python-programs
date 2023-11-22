cateogaries = ['Food','Auto','Clothing']
chart = "Percentage spent by category\n"
percentage = [10,70,30]

height = (len(max(cateogaries, key=len)))
padded = [names.ljust(height) for names in cateogaries]
# for names in cateogaries:
#     padded.append(names.ljust(height))

for i in reversed(range(0,110,10)):
    chart += f"{str(i) + '|':>4}"
    for percent in percentage:
        if percent>=i:
            chart += " o "
        else:
            chart+="   "
    chart += '\n'

chart += "    " + "-"*10 + ' \n'

for name in zip(*padded):
    # print(' '.join(name),end="\n")
    chart += "     "
    chart += ('  '.join(name)) + '  \n'

print(chart.rstrip('\n'))
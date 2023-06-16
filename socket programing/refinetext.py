
output_content=str()
with open("countries.txt", "r") as f:
	content = f.read()
	mod_content = content.replace(" - ","\n")
	mod_content = mod_content.replace(",","\n")
	output_content = str(mod_content)
	# print(mod_content)
	# print(type(mod_content))



print("===================================================")
	
# Split the string into lines
lines = output_content.splitlines()
print(type(lines))

# Remove leading spaces from each line
cleaned_lines = [line.lstrip() for line in lines]

# Print the cleaned lines
for line in cleaned_lines:
    	print(line)



# Open the file in append mode
with open("countries2.txt", "a") as file:
    for line in cleaned_lines:
    	# Append the word to the file
    	file.write(line + "\n")

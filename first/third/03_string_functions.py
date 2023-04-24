story='''this is because we cover installing things as they are needed in the tutorial
-- this is just an additional page that gathers all of the installation instructions in one place
(which is useful for some workshop formats). You can choose to install everything that is on this page
right now if you wish. But if you want to start learning things before installing a bunch of stuff on your computer,
skip this chapter and we will explain the installation parts to you later on, as they are needed.'''

#string functions
print(story)
print(len(story))
print(story.endswith("."))
print(story.startswith("This"))

print(story.count("."))
#capatilize inital character of a string
print(story.capitalize())
#find array index of first match
print(story.find("this"))
#replace all match with a string
print(story.replace("is","============"))

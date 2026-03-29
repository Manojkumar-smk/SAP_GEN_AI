story = """This is my kutty story"""

print(f"length of story is {len(story)}")
print(f"number of i is {story.find('i')} @character position")
print(f"position of i is {story.index('i')} @character position")

# string is immutable - cant change
# story.replace("t", "_replace_")

story = story.replace("t", "_replace_")
print(story)

print(story.lower())
print(story.upper())

words = story.split()
for word in words:
    print(word)

print(story.startswith("once"))
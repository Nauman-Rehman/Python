story = "once upon a time there was me named Nauman who watch python playlist to learn it"

# String function
print(len(story)) # it gives me length of the strings
print(story.endswith("learn it")) # it gives me true because story is ended with (learn it)
print(story.endswith("mguegt4gkr29 trt")) # it gives me false because story is not ended with (mguegt4gkr29 trt)
print(story.count("a")) # it gives me the number of occurence of a --> 8
print(story.count("b")) # it gives me the number of occurence of b --> 0
print(story.count("c")) # it gives me the number of occurence of c --> 2
print(story.count("d")) # it gives me the number of occurence of d --> 1
print(story.count("e")) # it gives me the number of occurence of e --> 7
print(story.count("ho")) # it gives me the number of occurence of ho. Yes it also gives the number of occurence of more than 1 character --> 2
print(story.count("me")) # it gives me the number of occurence of me --> 3
print(story.capitalize()) # it capitalize the first letter of the string --> once ..... => Once ....... but it is not permanent in story (o) of once remains small
print(story.find("time")) # it gives me the index of the first character of finding string --> 12
print(story.find("me")) # but in the case where our finding index is coming more than once, it don't gives the index for all it only give the index where it find it first --> 14
print(story.replace("Nauman","Nauman Rehman")) # it replace Nauman by Nauman Rehman wherever be it was written in the story
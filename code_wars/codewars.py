def disemvowel(string):

    for i in "aeiouAEIOU":
            string = string.replace(i,"")
    return string

print(disemvowel("This website is for losers LOL!"))
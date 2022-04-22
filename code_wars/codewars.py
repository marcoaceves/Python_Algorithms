def disemvowel(string):

    for i in "aeiouAEIOU":
            string = string.replace(i,"")
    return string

print(disemvowel("This website is for losers LOL!"))



def duplicate_encode(word):
    nw=''
    for i in word.lower():
        if word.lower().count(i)>1:
            nw+=')'
        if word.lower().count(i)==1:
            nw+='('
    return nw
print(duplicate_encode("recede"))
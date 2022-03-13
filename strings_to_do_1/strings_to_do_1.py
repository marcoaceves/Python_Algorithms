# remove blanks


string1 = " Pl ayTha tF u nkyM usi c "

def remove_blanks(string):
    remove=' '

    for i in remove:
	    string = string.replace(i, "")

    print(string)

remove_blanks(string1)


# get digits
digits1="0s1a3y5w7h9a2t4?6!8?0"

def get_digits(digits):

    array=[]
    new_arr=[]
    new_string=''
    for i in digits:
        array.append (ord(i))
    # print(array)

    for i in array:
        if i <= 57 and (i-48)>=0:
            new_arr.append(i - 48)

    new_arr.pop(new_arr[0])
    for i in new_arr :
        new_string= new_string + str(i)
    # print(new_arr)
    print(new_string)

get_digits(digits1)


# # Acronyms  Create a function that, given a string, returns the string’s acronym (first letters only, capitalized).
#             Given " there's no free lunch - gotta pay yer way. ", return "TNFL-GPYW".
#             Given "Live from New York, it's Saturday Night!", return "LFNYISN".

def acronym(string):

    acronym=string[0]
    remove=' '



    for i in range(1,len(string)):
        if string[i-1] == ' ':
            acronym += string[i]
        acronym = acronym.upper()


    for i in remove:
            acronym=acronym.replace(i,"")
    return acronym


print(acronym("Live from New York, it's Saturday Night!"))
print(acronym(" there's no free lunch - gotta pay yer way. "))



# Zip Arrays into Map

# Associative arrays are sometimes called maps because a key (string) maps to a value. Given two arrays, create an associative array (map) containing keys of the first, and values of the second. For arr1 = ["abc", 3, "yo"] and arr2 = [42, "wassup", true], return {"abc": 42, 3: "wassup", "yo": true}.

word = input("Please enter your word: ")

#wrong str function used
#islower() checks if the characters are lowercase
#lower() turns all characters into lowercase
word = word.lower()

#no such str function as "beginswith()"
begin_a = word.startswith("a")
end_a = word.endswith("a")

#there is no such thing as word("e")
#In this case, they want the value to be a boolean (True or False)
#Thus, we use ["e" in word] which returns a boolean 
contain_e = "e" in word

#no str function called "length()" use len instead
word_length = len(word)

# double equals should be used for checking conditions
# single equals is for definition
if not begin_a and not end_a and contain_e == -1:
    #logic error
    #short length words should be <= 4
    if word_length <= 4:
        print("The length of the word is short.")
    elif word <= 8:
        print("The length of the word is medium.")
        
    # elif needs to have a condition at the back to work.
    else:
        print("The length of the word is long.")

if begin_a:
    print("You entered a word that begins with 'a'.")
elif end_a:
    print("You entered a word that ends with 'a'.")

#remove "not"
#else it will print contains "e" when a word does not contain "e"
elif contain_e:
    #wrong statement printed
    # contains "a" --> contains "e"
    print("You entered a word that contains 'e'.")

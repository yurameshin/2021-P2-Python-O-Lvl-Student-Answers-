#defined constant to store vowels:
vowels = "aeiou"
#array to store words 
wordlist = []
#array to store vowel count
vowellist = []
#array to store words with more than two vowels
twolist = []
#total vowel count
total = 0
#variable to store word with highest vowel count
highest = -1
highestword = ""

for i in range(5):
    #variable to store vowel count
    count = 0
    user = input("Enter a word: ")
    #validating input
    while not(user.isalpha()):
        user = input("Input is not all letters, re-enter: ")
    #turn into lowercase
    user = user.lower()
    #run loop to count number of vowels
    for i in user:
        if i in vowels:
            count +=1
    #store word and vowel count in the lists
    wordlist.append(user)
    vowellist.append(count)
    #store word if >2 vowels
    if count >2:
        twolist.append(user)
    #total up vowel count
    total += count

#comparing highest vowel count
for index,value in enumerate(wordlist):
    if vowellist[index] > highest:
        highestword = value
        highest = vowellist[index]


        
#output word w/ highest no. of vowels
print("Word with highest no. of vowels:",highestword,"with",highest,"vowels.")
#output words w/ >2 vowels
if twolist == []:
    print("There are no words with more than 2 vowels")
else:
    print("Words with more than 2 vowels", twolist)
#output total no. of vowels
print("Total no. of vowels:",total)


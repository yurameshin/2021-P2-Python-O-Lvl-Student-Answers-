#defined constant to store vowels:
vowels = "aeiou"
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

#output statements
if count == 0:
    print("There are no vowels in the word.")
elif count == 1:
    print("There is one vowel in the word.")
else:
    print("There are",count,"vowels in the word.")
    

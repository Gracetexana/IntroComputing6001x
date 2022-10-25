#Assume s is a string of lower case characters.

#Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print: "Number of vowels: 5"
s = "azcbobobegghakl"
count = 0

for x in s:
    for y in "aeiou":
        if x==y:
            count += 1

print("Number of vowels: " + str(count))

#Assume s is a string of lower case characters.

#Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

s = "azcbobobegghakl"
count = 0

for i in range(len(s)-2): #I can actually make the range len(s) bc code below this in brackets does not care if it goes past the end of the string
    if s[i:i+3] == "bob":
        count += 1

print("Number of times bob occurs is: " + str(count))

#Assume s is a string of lower case characters.

#Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print: "Longest substring in alphabetical order is: beggh"

#In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print: "Longest substring in alphabetical order is: abc"

s = "wdujhzpoucdfks"

alph = "abcdefghijklmnopqrstuvwxyz"
nums = []
subs = s[0]
alts = s[0]

#make a list that represents s with numbers
for l in s:
    for i, letter in enumerate(alph):
        if l == letter:
            nums.append(i)

for x in range(1, len(nums)):
    if nums[x] >= nums[x-1]: #if s[x-1] and s[x] are in alphabetical order base on numerical order of nums
        alts += s[x]
    elif len(alts) > len(subs):
        subs = alts #subs stores the correct answer until alts finds a better answer
        alts = s[x] #alts resets
    else:
        alts = s[x] #alts resets

if len(alts) > len(subs):
    subs = alts #final check in case substring includes final letter

print("Longest substring in alphabetical order is: "+ subs)
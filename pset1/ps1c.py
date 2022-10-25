#Assume s is a string of lower case characters.

#Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print: "Longest substring in alphabetical order is: beggh"

#In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print: "Longest substring in alphabetical order is: abc"

s = "azcbobobegghakl"

subs = s[0]
alts = s[0]

for x in range(1, len(s)):
    if s[x] >= s[x-1]: #if s[x-1] and s[x] are in alphabetical order
        alts += s[x]
    else:
        alts = s[x] #alts resets
    if len(alts) > len(subs):
        subs = alts #subs stores the correct answer until alts finds a better answer

print("Longest substring in alphabetical order is: " + subs)
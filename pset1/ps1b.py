#Assume s is a string of lower case characters.

#Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

s = "azcbobobegghakl"
count = 0

for i in range(len(s)):
    if s[i:i+3] == "bob": # this code does not "care" if i+3 is after the end of the string
        count += 1

print("Number of times bob occurs is: " + str(count))
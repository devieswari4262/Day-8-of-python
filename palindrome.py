#palindrome
#check whether given number is pailndrome or not
'''number=int(input("enter the number:"))
reverse=""
b=str(number)
for i in b:
    reverse=i+reverse
if b ==reverse:
    print("palindrome")
else:
    print("not an palindrome")'''
    
#Findout the tgotal number of values of vowels and consonents in a string.
a= input("enter the string:")
vowels=0
const=0
for i in a:
    if i in "aeiou":
        vowels+=1
    else:
        const+=1
        print("vowels:",vowels)
        print("const:",const)
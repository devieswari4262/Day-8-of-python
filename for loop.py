#for loop
#From 100 to 200 print the even numbers
'''for i in range (101,201):
    if i%2==0:
        print(i)

#write  a code to print even number 1 to 100 
for i in range(0,100,2):
    print(i)

#print the 5 table
for i in range(1,11):
    print(f"5*{i}={5*i}")

#find the sum of first 10 numbers
sum=0
for i in range(1,11):
    sum+=i
    print(i)

#Findout the given number is prime or not
n=int(input("enter the number:"))
for i in range(2,n):
    if n%i==0:
        print("not a prime number")
        break
    else:
        print("prime number")


#Find the total sum in the given number
number= int(input("enter the number"))
sum=0
b=str(number)
for i in b:
    c=int(i)
    sum+=c
    print(sum)'''

#Reverse of the number
number=int(input("enter the number:"))
reverse=""
b=str(number)
for i in b:
    reverse=i+reverse
    print(reverse)
#find number is prime or not

num = int(input("Enter a number: "))

if num == 1 :
    print("Not prime")

flag = 0

for i in range (2,num+1):
    if num%i==0:
        # print("Not prime")
        flag = flag+1
        # break

if flag == 1:
    print("Number is prime")
else:
    print("Not prime")

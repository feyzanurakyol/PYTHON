#Decides can the given number is armstrong number or not

print("""**********************
ARMSTRONG NUMBER
**********************""")

number=input("Number: ") #I get the number from the user.
list1=list(number) #Then I stored is as an array

hey=len(list1) #Found the number of digits and also power
power=len(list1)

sum=0

for i in range(hey):
    sum+=(int(list1[i])**power)

if sum==int(number):
    print(number,"Sayisi armstrong sayısıdır.")
else:
    print(number,"Sayisi armstrong sayısı değildir.")

import random
leng=int(input("enter the length of the password"))
upper_case="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case=upper_case.lower()
numbers="0123456789"
symbols="()[]{},;_/\?@#"
upper,lower,nums,syms= True,True,True,True
all=""

if upper:
    all+=upper_case
if lower:
    all+=lower_case
if nums:
    all+=numbers
if syms:
    all+=symbols
amo=10

for x in range(amo):
    pswrd="".join(random.sample(all,leng))
    print(pswrd)
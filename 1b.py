num=int(input("Enter a number"))
val=str(num)
rev=val[::-1]
if(val==rev):
    print("The number",num,"is palindrome")
else:
    print("Not Palindrome")
for i in range(10):
 if(val.count(str(i))>0):
    print(str(i),"appears",val.count(str(i)),"times")
L= int(input())
C= int(input())
if (L%2==0 and C%2==0):
    print("#FFFFFF")
elif(L%2!=0 and C%2!=0):
    print("#FFFFFF")
elif (L%2==0 and C%2!=0):
    print ("#000000")
elif(L%2!=0 and C%2==0):
    print("#000000")
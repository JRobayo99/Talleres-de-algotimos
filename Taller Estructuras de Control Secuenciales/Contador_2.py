n=int(input())
c=0
suma=0
while True:
    if(c==n):
        break
    c=c+1
    led=input("")
    for i in led:
        if(i=="1"):
            sumatoria= suma+=2
        elif(i=="2"):
            suma= suma+=5
        elif(i=="3"):
            suma=suma+=5
        elif(i=="4"):
            suma=suma+=4
        elif(i=="5"):
         suma=suma+=5
        elif(i=="6"):
         suma=suma+=6
        elif(i=="7"):
         suma=suma+=3
        elif(i=="8"):
         suma=suma+=7
        elif(i=="9"):
         suma=suma+=6
        elif(i=="0"):
          suma=suma+=6
         

        

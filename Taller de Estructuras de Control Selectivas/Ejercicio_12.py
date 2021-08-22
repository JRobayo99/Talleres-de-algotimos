num1=int(input("introduce el valor en pesos: "))

if(num1>= 0 and num1>=100000 ):
    num2= (num1//100000)*100000
    tmp = num1%100000
    if(tmp>=0 and tmp<100000):
         num3 = (tmp // 10000)*10000
         tmp2 = tmp%10000
         if(tmp2>=0  and tmp2<10000):
             num4 = (tmp2//1000)*1000
             tmp3 = tmp2%1000
             if(tmp3>= 0 and tmp3<1000):
                 num5 = (tmp3//100)*100
                 tmp4 = tmp3%100
                 if(tmp4>=0 and tmp4 <=50):
                     num6= (tmp4//10)*10
if(num1>= 0 and num1 <100000 ):
    num2= (num1//10000)*10000
    tmp = num1%10000
    if(tmp>=0 and tmp<10000):
        num3= (tmp//1000)*1000
        tmp2= tmp%1000
        if(tmp2>=0 and tmp2<1000):
            num4= (tmp2//100)*100
            tmp3= tmp2%100
            if(tmp3>=0 and tmp3<1000):
              num5= (tmp3//10)*10
             

    
      



print(num2," COP")
print(num3," COP")
print(num4," COP")
print(num5," COP")
print(num6," COP")


#positional argumrnt
def add(a,b):
    return a+b
result=add(2,5)
print("sum=",result)

def check_valuc(no):
    if(no>0):
     print ("positive")
elif (no<0):
print("negative")
else:
print("zero")

#calling function
check_valuc(o)
check_valuc(90)
check_valuc(-15)

#keyword arguments

def simpal_interest(p:float,t:float,r:float):
   si=(p*R*t)/100
   print("simple interest:",si)
   #calling function
   simpal_interest(p=10000,t=2.5,r=3.5)

#defauit argument

   def sqr (num,exp=2)
      etun num**exp
      print(sqr(3))#use default exp=2
      print(sqr(3,3))#overrides default
      print(sqr(2,4))

      def add_numbers(*args):
         total=0
         for num in args
         total+=num
         return total
      #calling function
      print(add_numbers(10,20))
      print(add_numbers(5,10,15,20))
         



    
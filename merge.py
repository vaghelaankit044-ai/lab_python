with open ("1hello.txt","r") as f1,open ("ankit1.txt","r")as f2
open("hi.text","w")as f3:
    f3.write(f1.read())
    f3.write("\n")
    f3.write(f2.read())
    
     print("files merged successfully!")
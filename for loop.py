Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
for i in range (1,6):
    print(i)

    
1
2
3
4
5
 for i in range(3):
     
SyntaxError: unexpected indent
for i in range (3):
    print("hello")

    
hello
hello
hello
for i in range (1,11):
    print(i)

    
1
2
3
4
5
6
7
8
9
10
for i in range (1,21):
    if i%2>=0
    
SyntaxError: expected ':'
for i in range (1,21):
    if i%2>=0:
        print(i)

        
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
for i in range (1,16):
    if i%2 !=0:
        print(i)

        
1
3
5
7
9
11
13
15

for i in range (1,11):
    print("5x,i,"=",5*i)
          
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?

for i in range (1,11):
          print("5x",i,"=",5*i)

          
5x 1 = 5
5x 2 = 10
5x 3 = 15
5x 4 = 20
5x 5 = 25
5x 6 = 30
5x 7 = 35
5x 8 = 40
5x 9 = 45
5x 10 = 50
 for latter  in name:
          
SyntaxError: unexpected indent
for latter  in name
          
SyntaxError: expected ':'
for latter in name:
          print(letter)

          
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    for latter in name:
NameError: name 'name' is not defined
name="atmiya"
          
for latter in name:
          print(letter)

          
Traceback (most recent call last):
  File "<pyshell#34>", line 2, in <module>
    print(letter)
NameError: name 'letter' is not defined. Did you mean: 'latter'?
total=0
          
for i in range (1,6):
          total=total+i
          print("sum is!", total)

          
sum is! 1
sum is! 3
sum is! 6
sum is! 10
sum is! 15

number=(10,20,30,40)
          
for n in number
          
SyntaxError: expected ':'
for n in number:
          print(n)

          
10
20
30
40

+
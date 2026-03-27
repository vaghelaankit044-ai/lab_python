Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> from array import*
>>> arr=array('i',[10,20,30,40,50])
>>> print(arr[0])#first element
10
>>> print(arr[2])#third element
30
>>> print(arr[4])#fifth element
50
>>> 
>>> print(arr[-1])#last element
50
>>> print(arr(-2))#second last element
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print(arr(-2))#second last element
TypeError: 'array.array' object is not callable

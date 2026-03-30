src=open("ankit.txt","r")
data=src.read()
src.close()


dst=open("hi.txt","w")
dst.write(data)
dst.close()
print("file copied successfully.")
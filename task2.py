f=open("sampletext.txt","w")
f.write(input("enter text to write to the file"))
print("data succesfully written")

f=open("sampletext.txt","a")
f.write(input("enter text to be appended"))
print("data sucessfully appended")

f=open("sampletext.txt","r")
read=f.read()
print("final content of output is")
print(read)
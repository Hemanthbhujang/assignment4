try:
    f=open("sampletext.txt","r")
    read=f.read()
    print(read.strip())

except FileNotFoundError:
    print("file not found")


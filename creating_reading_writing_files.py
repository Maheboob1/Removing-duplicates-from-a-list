f=open("sample.txt","a")
f=open("sample.txt","w")
str="i am a python automation engineer, i work on python language, python is an interpreter language"
f.write(str)

print(str.count("python"))
print(str.count("language"))
f=open("sample.txt","r")
f.seek(0)
f.read()
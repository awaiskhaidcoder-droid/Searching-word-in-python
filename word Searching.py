import os
def changeWord(data,search,change):
    newData=data.replace(search,change)
    print(newData)
    return newData



with open("Text.txt","a+") as f:
    f.write("this is writing file")
    f.seek(0)
    data=f.read()
    new=changeWord(data,"this","that")

    
with open("Text.txt","w") as f:
    f.write(new)

# os.remove("Text.txt")






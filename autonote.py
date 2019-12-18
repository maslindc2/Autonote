import sys
import os


python = ".py"
text = ".txt"
java = ".java"



extensions = {
    "python" : python,
    ".py" : python,
    "text" : text,
    ".txt" : text,
    "java" : java
}


def create():
    
    extension = str(sys.argv[3])
    folderName = str(sys.argv[2])
    fileName = str(sys.argv[1])
    os.chdir("./Notes")

    # Checks to see if the specified file type is in our dictionary of extensions
    # If it isn't then let the user know and default it to a txt file
    try:
        extension = extensions[extension]
    except Exception:
        print(extension)
        print("The given extensions is not in the programs dictionary")
        print("I have instead created it as a text file")
        extension = ".txt"
    
    #Gets the file name and appends the extension to it
    fileName = fileName + extension
    
    if os.path.isdir("./" + folderName):
        os.path.chdir("./" + folderName)
    
    else:
        os.mkdir(folderName)
        os.chdir("./" + folderName)
    
    if not os.path.isfile("./" + fileName):
        open(fileName, "a").close()
    
    os.system("subl " + fileName)

    print(sys.argv)
    #         Gets the file name  Gets the extension
    fileName = str(sys.argv[1]) + str(sys.argv[3])
    #Open fileName specified from above and open for writing and then close
    open(fileName, "a").close()
    #Opens the file name in atom
    os.system("atom " + fileName)
    



if __name__ == "__main__":
    create()
